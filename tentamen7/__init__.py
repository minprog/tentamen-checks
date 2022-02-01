import check50
import check50.c
import check50.internal
import contextlib
import os
import sys
import re
import glob

from collections import Counter

@check50.check()
def convert():
    """convert werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("convert") as run_check:

        (run_check()
            .stdin("0")
            .stdin("8")
            .stdout("16\s?g bloem"))

        (run_check()
            .stdin("1")
            .stdin("0")
            .stdout("125\s?g bloem"))

        (run_check()
            .stdin("1")
            .stdin("2")
            .stdout("188\s?g bloem"))



@check50.check()
def filter():
    """filter werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("filter") as run_check:

        (run_check("a")
            .stdin("aards")
            .stdout("aards\n")
            .stdin("bramen")
            .stdin("artikel")
            .stdout("artikel\n")
            .stdin("corvee")
            .stdin("STOP")
            .exit(0))

        (run_check("b")
            .stdin("aards")
            .stdin("bramen")
            .stdout("bramen\n")
            .stdin("artikel")
            .stdin("corvee")
            .stdin("STOP")
            .exit(0))


@check50.check()
def autocorrect():
    """autocorrect werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("autocorrect") as run_check:

        (run_check()
            .stdin("Fuzzy Wuzzy was a bear . Fuzzy Wuzzy had no hair.Fuzzy Wuzzy wasn't fuzzy , was he ?")
            .stdout("Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair. Fuzzy Wuzzy wasn't fuzzy, was he?"))


@check50.check()
def wachtwoord():
    """wachtwoord werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("wachtwoord") as run_check:

        (run_check()
            .stdin("geheim")
            .stdout("Niet sterk genoeg!")
            .stdin("aardbei121")
            .stdout("Niet sterk genoeg!")
            .stdin("roomboter")
            .stdout("Niet sterk genoeg!")
            .stdin("kruipluik291")
            .stdout("Sterk genoeg!")
            .exit(0))

        (run_check()
            .stdin("geheim")
            .stdout("Niet sterk genoeg!")
            .stdin("kruipluik")
            .stdout("Sterk genoeg!")
            .exit(0))

        (run_check()
            .stdin("mamamama")
            .stdout("Sterk genoeg!")
            .exit(0))

@check50.check()
def maskers():
    """maskers werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("maskers") as run_check:

        (run_check("XC")
            .stdout("Na maximaal 0.5 uur is voldoende virus overgedragen voor een besmetting."))

        (run_check("FF")
            .stdout("Na maximaal 25.0 uur is voldoende virus overgedragen voor een besmetting."))

        (run_check("CX")
            .stdout("Na maximaal 0.5 uur is voldoende virus overgedragen voor een besmetting."))

        (run_check("FX")
            .stdout("Na maximaal 2.5 uur is voldoende virus overgedragen voor een besmetting."))

        (run_check()
            .stdout("Usage: ./maskers CODES"))


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

    def create_check(*args):
        x=list(args)
        x.insert(0,command)
        x = " ".join(x)
        check = check50.run(x)
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

        files = {n.lower():n for n in glob.glob("*.c")}
        real_name = f"{name}.c"
        submitted_name = files.get(real_name, False)
        if submitted_name != False:
            os.rename(submitted_name, real_name)
            check50.c.compile(real_name, "-lcs50")
            return f"./{name}"

    raise check50.Failure(f"{' en/of '.join(names)} {'is' if len(names) == 1 else 'zijn'} niet aanwezig")
