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
def dobbelsteen():
    """dobbelsteen werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("dobbelsteen") as run_check:

        # check long input
        inputs = [1,3,5,5,2,6,3,1,2,3,6,5,3]
        output = dict(Counter(inputs))

        run = run_check()
        for i in inputs:
            run = run.stdin(str(i))
        run = run.stdin("0")
        run.stdout("(Totalen:)?[\s\n]*" + "\n".join([f"{k}: {output.get(k,0)}\s*" for k in [1,2,3,4,5,6]]), "Totalen:\n" + "\n".join([f"{k}: {output.get(k,0)}" for k in [1,2,3,4,5,6]]))

        # check length 0 input
        run = run_check()
        run = run.stdin("100")
        run.stdout("Je hebt niet gegooid\.?", "Je hebt niet gegooid.")

        # check length 0 input
        run = run_check()
        run = run.stdin("0")
        run.stdout("Je hebt niet gegooid\.?", "Je hebt niet gegooid.")



@check50.check()
def absoluut():
    """absoluut werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("absoluut", "som") as run_check:

        (run_check("2 -5 -3 1")
            .stdout("11"))

        (run_check("0")
            .stdout("0"))

        (run_check()
            .stdout("Usage: ./absoluut num..."))


@check50.check()
def samenvatten():
    """samenvatten werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("samenvatten") as run_check:

        (run_check()
            .stdin("Nederlanders worden steeds ouder, vooral doordat ze na hun 65ste langer in leven blijven.")
            .stdout("Ns wn ss or, vl dt ze na hn 6e lr in ln bn."))

        (run_check()
            .stdin("Verloren! Zaterdag 5 september. Gouden armband met papa erin.")
            .stdout("Vn! Zg 5 sr. Gn ad mt pa en."))


@check50.check()
def splits():
    """splits werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("splits", "splitsen") as run_check:

        (run_check()
            .stdin("hvealkea nftiijen!e!")
            .stdout("hele fijne")
            .stdout("vakantie!!"))

        (run_check()
            .stdin("twhaes  ghreirnec h")
            .stdin("vhreite satl ?")
            .stdout("vriest ")
            .stdout("het al?"))


@check50.check()
def arrays():
    """arrays werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("arrays", "array") as run_check:

        (run_check()
            .stdout("....\n.XX.\n.XX.\n....\n"))


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
