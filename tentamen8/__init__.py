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
def collatz():
    """collatz werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("collatz") as run_check:

        (run_check()
            .stdin("3")
            .stdout("\w+:\s+1\s+\w+:\s+10")
            .stdout("\w+:\s+2\s+\w+:\s+5")
            .stdout("\w+:\s+3\s+\w+:\s+16")
            .stdout("\w+:\s+4\s+\w+:\s+8")
            .stdout("\w+:\s+5\s+\w+:\s+4")
            .stdout("\w+:\s+6\s+\w+:\s+2")
            .stdout("\w+:\s+7\s+\w+:\s+1"))

        (run_check()
            .stdin("16")
            .stdout("\w+:\s+1\s+\w+:\s+8")
            .stdout("\w+:\s+2\s+\w+:\s+4")
            .stdout("\w+:\s+3\s+\w+:\s+2")
            .stdout("\w+:\s+4\s+\w+:\s+1"))

@check50.check()
def makelaar():
    """makelaar werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("makelaar") as run_check:

        (run_check()
            .stdin("55")
            .stdin("1")
            .stdin("1")
            .stdin("1")
            .stdout("295000,-"))

        (run_check()
            .stdin("150")
            .stdin("3")
            .stdin("3")
            .stdin("1")
            .stdout("826200,-"))

        (run_check()
            .stdin("150")
            .stdin("3")
            .stdin("3")
            .stdin("2")
            .stdout("930000,-"))

@check50.check()
def morse():
    """morse werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("morse") as run_check:

        (run_check()
            .stdin("156")
            .stdout(".---- ..... -...."))

        (run_check()
            .stdin("92316")
            .stdout("----. ..--- ...-- .---- -...."))

@check50.check()
def korting():
    """korting werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("korting") as run_check:

        (run_check("3.35", "2")
            .stdout("[^:]+: 3.35\s*\n", "Elke avocado kost: 3.35")
            .stdout(".*2.*1\s*\n", "Korting! 2 avocado's voor de prijs van 1")
            .stdout("\?", "Hoeveel avocado's?")
            .stdin("4")
            .stdout(".*4.*6\.70\s*\n", "Besparing voor 4 avocado's is: 6.70")
            .stdout("\?", "Hoeveel avocado's?")
            .stdin("0")
            .exit())

        (run_check("2.35", "3")
            .stdout("[^:]+: 2.35\s*\n", "Elke avocado kost: 2.35")
            .stdout(".*3.*2\s*\n", "Korting! 3 avocado's voor de prijs van 2")
            .stdout("\?", "Hoeveel avocado's?")
            .stdin("2")
            .stdout(".*2.*0\.00\s*\n", "Besparing voor 2 avocado's is: 0.00")
            .stdout("\?", "Hoeveel avocado's?")
            .stdin("3")
            .stdout(".*3.*2\.35\s*\n", "Besparing voor 3 avocado's is: 2.35")
            .stdout("\?", "Hoeveel avocado's?")
            .stdin("7")
            .stdout(".*7.*4\.70\s*\n", "Besparing voor 7 avocado's is: 4.70")
            .stdout("\?", "Hoeveel avocado's?")
            .stdin("0")
            .exit())

@check50.check()
def alfa():
    """alfa werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("alfa") as run_check:

        (run_check()
            .stdin("ABDEUW")
            .stdout("Deze tekst staat op al(f|ph)abetische volgorde."))
        (run_check()
            .stdin("ABEDUW")
            .stdout("Deze tekst staat niet op al(f|ph)abetische volgorde."))
        (run_check()
            .stdin("ABD EUW")
            .stdout("Deze tekst staat op al(f|ph)abetische volgorde."))
        (run_check()
            .stdin("ABE DUW")
            .stdout("Deze tekst staat niet op al(f|ph)abetische volgorde."))
        (run_check()
            .stdin("AbD euw")
            .stdout("Deze tekst staat op al(f|ph)abetische volgorde."))
        (run_check()
            .stdin("Abe Duw")
            .stdout("Deze tekst staat niet op al(f|ph)abetische volgorde."))


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
