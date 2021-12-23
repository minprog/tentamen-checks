import check50
import check50.c
import check50.internal
import contextlib
import os
import sys
import re
import glob

@check50.check()
def leestijd():
    """leestijd werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("leestijd") as run_check:

        # check example 1
        (run_check()
            .stdin("35")
            .stdin("50")
            .stdin("10")
            .stdin("15")
            .stdin("-1")
            .stdout("[Jj]e hebt ongeveer 9[12] pagina", "Je hebt ongeveer 91/92 pagina's gelezen."))

        # check example 2
        (run_check()
            .stdin("-1")
            .stdout("[Jj]e hebt niet gelezen\.?"))


@check50.check()
def leetspeak():
    """leetspeak werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("leetspeak", "1337") as run_check:

        (run_check("Waterlelie")
            .stdout("W473r131i3"))

        (run_check("Anders")
            .stdout("4nd3rs"))

        (run_check("tentamen baas!!")
            .stdout("73n74m3n"))


@check50.check()
def leetspeak2():
    """leetspeak werkt met input"""
    with logged_check_factory("leetspeak", "1337") as run_check:

        (run_check()
            .stdin("Waterlelie")
            .stdout("W473r131i3"))

        (run_check()
            .stdin("Anders")
            .stdout("4nd3rs"))

        (run_check()
            .stdin("tentamen baas!!")
            .stdout("73n74m3n b44s!!"))


@check50.check()
def carometer():
    """carometer werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("carometer", "rent") as run_check:

        (run_check()
            .stdin("5")
            .stdin("500")
            .stdin("j")
            .stdout("600", "De kosten zijn EUR 600"))

        (run_check()
            .stdin("5")
            .stdin("500")
            .stdin("j")
            .stdout("600", "De kosten zijn EUR 600"))

        (run_check()
            .stdin("2")
            .stdin("100")
            .stdin("n")
            .stdout("180", "De kosten zijn EUR 180"))

        (run_check()
            .stdin("2")
            .stdin("100")
            .stdin("n")
            .stdout("180", "De kosten zijn EUR 180"))

        (run_check()
            .stdin("0")
            .stdin("400")
            .stdin("n")
            .stdout("invoer!")
            .stdin("2")
            .stdin("100")
            .stdin("n")
            .stdout("180", "De kosten zijn EUR 180"))

        (run_check()
            .stdin("5")
            .stdin("19")
            .stdin("n")
            .stdout("invoer!")
            .stdin("2")
            .stdin("100")
            .stdin("n")
            .stdout("180", "De kosten zijn EUR 180"))

        (run_check()
            .stdin("5")
            .stdin("20")
            .stdin("z")
            .stdout("invoer!")
            .stdin("2")
            .stdin("100")
            .stdin("n")
            .stdout("180", "De kosten zijn EUR 180"))


@check50.check()
def afgebroken():
    """afgebroken werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("afgebroken") as run_check:

        (run_check()
            .stdin("Nederlanders worden steeds ouder, vooral door- dat ze na hun 65ste langer in leven blijven.")
            .stdout("Nederlanders worden steeds ouder, vooral doordat ze na hun 65ste langer in leven blijven."))

        (run_check()
            .stdin("Over de identiteit van de schutter zegt de po- litie: 'Als het de man is die we denken dat het is, dan is het een bekende van de politie.'")
            .stdout("Over de identiteit van de schutter zegt de politie: 'Als het de man is die we denken dat het is, dan is het een bekende van de politie.'"))

        (run_check()
            .stdin("Een 36-jarige Geldropse heeft deze week een in- breker in haar schuurtje net zo lang achtervolgd tot de politie arriveerde.")
            .stdout("Een 36-jarige Geldropse heeft deze week een inbreker in haar schuurtje net zo lang achtervolgd tot de politie arriveerde."))


@check50.check()
def validate():
    """validate werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("validate", "lisp", "validatie") as run_check:

        (run_check()
            .stdin("(defun factorial (())(] (loop))))")
            .stdout("[Ii]nvalid"))

        (run_check()
            .stdin("(write (factorial 3))")
            .stdout("[Vv]alid"))

        (run_check()
            .stdin("(defun gretting ((write-line \"let it snow\"))")
            .stdout("[Ii]nvalid"))


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

        files = glob.glob(f"{name}*.c")
        if len(files) >= 1:
            os.rename(files[0], real_name)
            check50.c.compile(real_name, "-lcs50")
            return f"./{name}"

    raise check50.Failure(f"{' en/of '.join(names)} {'is' if len(names) == 1 else 'zijn'} niet aanwezig")
