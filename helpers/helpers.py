import contextlib
import re
import string
import check50
import os
import sys
import glob

from typing import Generator, Callable

__all__ = ["logged_check_factory", "replace_main", "set_stdout_limit"]


class Stream:
    """Stream-like object that stores everything it receives"""
    def __init__(self):
        self.entries = []

    @property
    def text(self) -> str:
        return "".join(self.entries)

    def write(self, entry) -> None:
        entry = entry.replace("\r\n", "\n").replace("\r", "\n")
        self.entries.append(entry)

    def flush(self) -> None:
        pass

    def reset(self) -> None:
        self.entries = []


@contextlib.contextmanager
def logged_check_factory(*names: str) -> Generator[Callable[[tuple[str, ...]], check50.run], None, None]:
    """
    A factory of checks that logs everything on stdin/stdout.
    The log is written to the data.output field of check50's json output.
    """
    command = make_runnable(*names)
    stream = Stream()

    def create_check(*args: str) -> check50.run:
        x = list(args)
        x.insert(0,command)
        x = " ".join(x)
        check = check50.run(x)
        check.process.logfile = stream
        return check

    try:
        yield create_check
    finally:
        check50.data(output=stream.text)


def make_runnable(*names: str) -> str:
    """
    Get a runnable C/Python command for a check.
    Prefers C files over Python files.
    """
    for name in names:
        if os.path.exists(f"{name}.c"):
            check50.c.compile(f"{name}.c", "-lcs50")
            return f"./{name}"

        if os.path.exists(f"{name}.py"):
            return f"{sys.executable} {name}.py"

        files = {n.lower():n for n in glob.glob("*.c")}
        real_name = f"{name}.c"
        submitted_name = files.get(real_name, False)
        if submitted_name != False:
            os.rename(submitted_name, real_name)
            check50.c.compile(real_name, "-lcs50")
            return f"./{name}"

    raise check50.Failure(f"{' en/of '.join(names)} {'is' if len(names) == 1 else 'zijn'} niet aanwezig")


def set_stdout_limit(char_limit: int) -> None:
    from pexpect.exceptions import EOF
    import check50._api

    def _raw(s):
        """Get raw representation of s, truncating if too long."""

        if isinstance(s, list):
            s = "\n".join(_raw(item) for item in s)

        if s == EOF:
            return "EOF"

        s = f'"{repr(str(s))[1:-1]}"'
        if len(s) > char_limit:
            s = s[:char_limit] + "...\""  # Truncate if too long
        return s

    check50._api._raw = _raw


@contextlib.contextmanager
def replace_main(filename: str, main: str) -> Generator[None, None, None]:
    """replace or insert main into file"""
    main = "\n" + main + "\n"

    with open(filename) as f:
        content = f.read()

    indices = find_main(content)
    if indices:
        start, end = indices
        # always append main to eof instead of in-place. This way
        # a commented out main does not stay commented out after replacing
        new_content = content[:start] + "\n" + content[end + 1:] + main
    else:
        new_content = content + main

    try:
        with open(filename, "w") as f:
            f.write(new_content)
        yield
    except Exception as e:
        with open(filename, "w") as f:
            f.write(content)
        raise e


def find_main(content: str) -> tuple[int, int] | None:
    match = re.compile("int\s+main\s*\(", re.MULTILINE).search(content)
    if match:
        index = match.start()
        index_closing_bracket = find_closing_bracket(content[index:])
        return (index, index + index_closing_bracket)
    return None


def find_closing_bracket(content: str) -> int:
    n_open_brackets = -1
    for i, char in enumerate(content):
        # No brackets, but statement is closed through ;
        if char == ";" and n_open_brackets == -1:
            return i

        if char == "{":
            if n_open_brackets == -1:
                n_open_brackets = 1
            else:
                n_open_brackets += 1

        if char == "}":
            n_open_brackets -= 1

        if n_open_brackets == 0:
            return i

    return -1


def encode_unprintable(s: str) -> str:
    encoded_string = ""
    for char in s:
        # note: str.isprintable() has a different definition of printable :(
        if char in string.printable:
            encoded_string += char
        else:
            encoded_string += "\\x{:02x}".format(ord(char))
    return encoded_string
