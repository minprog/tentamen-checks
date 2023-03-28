import check50
import check50.c
import check50.internal
import contextlib
import os
import sys
import glob

from collections import Counter

@check50.check()
def wachtwoord():
    """wachtwoord werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("wachtwoord", "wachtwoorden") as run_check:

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
def spraaksynthese():
    """spraaksynthese is correct"""
    with logged_check_factory("spraaksynthese", "synthese") as run_check:

        # check example 1
        (run_check("123")
            .stdout("een,\s?twee,\s?drie\n"))

        # check example 2
        (run_check("4210")
            .stdout("vier,\s?twee,\s?een,\s?nul\n"))

        # check example 3
        (run_check()
            .stdout("Usage"))

@check50.check()
def mario51():
    """mario51 werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("mario51") as run_check:

        # check example 1
        check = run_check("5", "4")
        answer = (
            "#####(\s)*\n"
            "#(\s)*\n"
            "#(\s)*\n"
            "#(\s)*\n"
        )
        check.stdout(answer)

        # check example 2
        check = run_check("2", "2")
        answer = (
            "##(\s)*\n"
            "#(\s)*\n"
        )
        check.stdout(answer)

        # check example 3
        check = run_check("1", "2")
        check.stdout("Dat kan niet")

        # check example 4
        check = run_check("1")
        check.stdout("Dat kan niet")

@check50.check()
def klinkers():
    """klinkers werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("klinkers") as run_check:
        (run_check()
            .stdin("Equal")
            .stdin("renal")
            .stdout("equal"))

        (run_check()
            .stdin("aye")
            .stdin("abide")
            .stdout("aye\nabide"))

        (run_check()
            .stdin("retina")
            .stdin("AwesOmE")
            .stdout("awesome"))

@check50.check()
def raden():
    """getal raden is correct"""
    with logged_check_factory("raden") as run_check:

        # check example 1
        (run_check()
            .stdin("10")
            .stdout("te hoog")
            .stdin("3")
            .stdout("te laag")
            .stdin("6")
            .stdout("goed"))

        # check example 1
        (run_check()
            .stdin("-2")
            .stdout("te laag")
            .stdin("10")
            .stdout("te hoog")
            .stdin("1")
            .stdout("te laag")
            .stdin("6")
            .stdout("goed"))

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
        check = check50.run(" ".join([command] + list(args)))
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
