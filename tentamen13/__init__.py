import check50
import check50.c
import check50.internal
import contextlib
import os
import sys
import glob

from collections import Counter


@check50.check()
def reistijd():
    """reistijd werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("reistijd") as run_check:

        (run_check()
            .stdin("2.6")
            .stdin("200")
            .stdin("B")
            .stdin("4.2")
            .stdout("reis kost je ongeveer 205 minuten"))

        (run_check()
            .stdin("5.5")
            .stdin("50.5")
            .stdin("F")
            .stdin("3")
            .stdout("reis kost je ongeveer 73 minuten"))

@check50.check()
def veldje():
    """veldje werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("veldje") as run_check:
            (run_check()
                .stdin("100")
                .stdin("20")
                .stdout("13")
                .stdout("200"))

            (run_check()
                .stdin("0")
                .stdin("7")
                .stdout("17")
                .stdout("70"))

            (run_check()
                .stdin("50")
                .stdin("1")
                .stdout("0")
                .stdout("10"))

@check50.check()
def pijl():
    """pijl werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("pijl") as run_check:

        answer5 = (
            "# #\s*\n"
            " # #\s*\n"
            "  # #\s*\n"
            " # #\s*\n"
            "# #\s*"
        )

        answer3 = (
            "# #\s*\n"
            " # #\s*\n"
            "# #\s*"
        )

        answer7 = (
            "# #\s*\n"
            " # #\s*\n"
            "  # #\s*\n"
            "   # #\s*\n"
            "  # #\s*\n"
            " # #\s*\n"
            "# #\s*"
        )

        check = run_check("5")
        check.stdout(answer5)

        check = run_check("3")
        check.stdout(answer3)

        # zelfde output als 5!
        check = run_check("6")
        check.stdout(answer5)

        check = run_check("7")
        check.stdout(answer5)

        check = run_check("2")
        check.stdout("Dat kan niet")

        check = run_check("1")
        check.stdout("Dat kan niet")

@check50.check()
def startletters():
    """startletters werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("startletters") as run_check:
        (run_check()
            .stdin("aardappel koolraap winterpeen")
            .stdout("Top!"))

        (run_check()
            .stdin("Aardappel koolraap Winterpeen")
            .stdout("Top!"))

        (run_check()
            .stdin("andijvie aardbei")
            .stdout("Probeer het nog eens!")
            .stdin("A besotted camel departed early Friday going home")
            .stdout("Top!"))

@check50.check()
def klinkers():
    """klinkers werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("klinkers") as run_check:

        (run_check()
            .stdout("volgende woord")
            .stdout("1 klinker bevat")
            .stdin("de")
            .stdout("volgende woord")
            .stdout("2 klinkers")
            .stdin("woord")
            .stdout("volgende woord")
            .stdout("3 klinkers")
            .stdin("oeps")
            .stdout("bevat niet precies 3 klinkers"))
        
        (run_check()
            .stdin("dit")
            .stdout("volgende woord")
            .stdin("is")
            .stdout("bevat niet precies 2 klinkers"))

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
        check50.data(output=(stream.text+"\n\n"))


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
