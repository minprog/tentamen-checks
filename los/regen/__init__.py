import check50
import check50.c
import check50.internal
import contextlib
import os
import sys
import re
import glob

@check50.check()
def regen():
    """regen is waarschijnlijk correct"""
    with logged_check_factory("regen") as run_regen:

        (run_regen()
            .stdin("12")
            .stdin("12")
            .stdin("999")
            .stdout("Gemiddeld 12(?!\d)", str_output="Gemiddeld 12 millimeter"))

        (run_regen()
            .stdin("12")
            .stdin("6")
            .stdin("3")
            .stdin("999")
            .stdout("Gemiddeld 7(?!\d)", str_output="Gemiddeld 7 millimeter"))

        (run_regen()
            .stdin("999")
            .stdout("Dat kan niet"))

        (run_regen()
            .stdin("12")
            .stdin("11")
            .stdin("999")
            .stdout("Gemiddeld 11(?!\d)", str_output="Gemiddeld 11 millimeter"))


class Stream:
    """Stream-like object that stores everything it receives"""
    def __init__(self):
        self.entries = []

    @property
    def text(self):
        return "".join(self.entries)

    def write(self, entry):
        entry = entry.replace("\r\n", "\n").replace("\r", "\n")
        self.entries.append(entry)

    def flush(self):
        pass

    def reset(self):
        self.entries = []


@contextlib.contextmanager
def logged_check_factory(*names):
    """
    A factory of checks that logs everything on stdin/stdout.
    The log is written to the data.output field of check50's json output.
    """
    command = make_runnable(*names)
    stream = Stream()

    def create_check():
        check = check50.run(command)
        check.process.logfile = stream
        return check

    try:
        yield create_check
    finally:
        check50.data(output=stream.text)


def make_runnable(*names):
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

        files = glob.glob("*.c")
        if len(files) > 0:
            check50.c.compile(f"{files[0]}", "-lcs50")
            return f"./{files[0][0:-2]}"

    raise check50.Failure(f"{' en/of '.join(names)} {'is' if len(names) == 1 else 'zijn'} niet aanwezig")
