import check50
import check50.c
import os
import sys


@check50.check()
def rechthoeken():
    """rechthoeken is waarschijnlijk correct"""
    with logged_check_factory("rechthoeken") as run_rechthoeken:

        # check example 1
        (run_rechthoeken()
            .stdin("45")
            .stdin("33")
            .stdin("22")
            .stdin("12")
            .stdin("V")
            .stdout("1221(?!\d)", str_output="1221"))

        # check example 2
        (run_rechthoeken()
            .stdin("1")
            .stdin("43")
            .stdin("39")
            .stdin("31")
            .stdin("S")
            .stdout("1252(?!\d)", str_output="1252"))

        # check example 3
        (run_rechthoeken()
            .stdin("1")
            .stdin("43")
            .stdin("39")
            .stdin("31")
            .stdin("1")
            .stdout("43(?!\d)", str_output="43"))

        # check example 4
        (run_rechthoeken()
            .stdin("1")
            .stdin("43")
            .stdin("39")
            .stdin("31")
            .stdin("X")
            .stdout("is geen geldige keuze"))

        # check example 5
        (run_rechthoeken()
            .stdin("1")
            .stdin("43")
            .stdin("39")
            .stdin("31")
            .stdin("0")
            .stdout("is geen geldige keuze"))



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

    raise check50.Failure(f"{' en/of '.join(names)} {'is' if len(names) == 1 else 'zijn'} niet aanwezig")
