import check50
import check50.c
import check50.internal
import contextlib
import os
import sys
import glob


@check50.check()
def langste_woord():
    """langste_woord werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("langste_woord") as run_check:

        (run_check()
            .stdin("dit is een zin met meerdere woorden erin")
            .stdout("meerdere")
            .stdout("8 letters lang"))

        (run_check()
            .stdin("het langste woord staat helemaal achteraan")
            .stdout("achteraan")
            .stdout("9 letters lang"))

        (run_check()
            .stdin("twee drie vier")
            .stdout("twee")
            .stdout("4 letters lang"))


@check50.check()
def header():
    """header werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("header") as run_check:
            (run_check()
                .stdin("Jelle van Assema")
                .stdin("02/10/2023")
                .stdin("Prints hello world")
                .stdout("/[\*#]{50,}")
                .stdout("\* ?Author: Jelle van Assema {30,}\*")
                .stdout("\* ?Date: 02/10/2023 {30,}\*")
                .stdout("\* ?D[ei]scription: Prints hello world {20,}\*")
                .stdout("[#\*]{50,}/?"))

            (run_check()
                .stdin("Dit is een veel te lange naam van meer dan zestig karakters waardoor het niet zou passen")
                .stdin("Dit is weer een veel te lange naam van meer dan zestig karakters waardoor het niet zou pa")
                .stdin("Dit is ook een veel te lange naam van meer dan zestig karakters waardoor het niet zou pas")
                .stdin("Martijn Reus")
                .stdin("Dit is een veel te lang antwoord van meer dan zestig karakters voor de datum vraag")
                .stdin("Dit is een veel te lang antwoord van meer dan zestig karakters voor de datum vraag")
                .stdin("02-10-2023")
                .stdin("Ook deze beschrijving is meer dan zestig karakters lang waardoor het niet zou passe")
                .stdin("Prints a pyramid for mario")
                .stdout("/[\*#]{50,}")
                .stdout("\* ?Author: Martijn Reus {30,}\*")
                .stdout("\* ?Date: 02-10-2023 {30,}\*")
                .stdout("\* ?D[ei]scription: Prints a pyramid for mario {20,}\*")
                .stdout("[\*#]{50,}/?"))


@check50.check()
def weekrooster():
    """weekrooster werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("weekrooster") as run_check:
        (run_check()
            .stdin("maandag")
            .stdin("3")
            .stdin("di")
            .stdin("4")
            .stdin("vr")
            .stdin("5")
            .stdin("x")
            .stdout("3 uren op maandag")
            .stdout("4 uren op dinsdag")
            .stdout("0 uren op woensdag")
            .stdout("0 uren op donderdag")
            .stdout("5 uren op vrijdag"))
        
        (run_check()
            .stdin("ma")
            .stdin("2")
            .stdin("ma")
            .stdin("4")
            .stdin("ma")
            .stdin("3")
            .stdout("kan niet")
            .stdin("x")
            .stdout("6 uren op maandag")
            .stdout("0 uren op dinsdag")
            .stdout("0 uren op woensdag")
            .stdout("0 uren op donderdag")
            .stdout("0 uren op vrijdag"))

@check50.check()
def snake():
    """snake werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("snake") as run_check:        
        run_check("0", "2").stdout("12")
        run_check("5", "4").stdout("1")
        run_check("0", "5").stdout("0")

@check50.check()
def isbn():
    """isbn werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("isbn") as run_check:

        run_check("9780606323451").stdout("correct")
        run_check("9780007203582").stdout("incorrect")
        run_check("9780141032009").stdout("correct")


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
