import check50
import check50.c
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
            .stdout("[Jj]e hebt ongeveer 9[12][\n]* pagina", "Je hebt ongeveer 91/92 pagina's gelezen."))

        # check example 2
        (run_check()
            .stdin("-1")
            .stdout("[Jj]e hebt niet gelezen\.?"))


@check50.check()
def spam():
    """spam werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("spam") as run_check:
        
        test_string = "Ca$hh M0n3y"
        output = (run_check(test_string)
            .stdout("30(?!\d)", str_output="30")
            .stdout())

        if "spam" not in output or "normaal" in output:
            raise check50.Failure(f"{test_string} should be spam")

        test_string = "Dit was zeker geen spam!"
        output = (run_check(test_string)
            .stdout("5(?!\d)", str_output="5")
            .stdout())

        if "spam" in output or "normaal" not in output:
            raise check50.Failure(f"{test_string} shoud not be spam")


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
