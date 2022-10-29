import check50
import check50.c
import check50.internal
import contextlib
import os
import sys
import glob

@check50.check()
def morse():
    """morse werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("morse") as run_check:

        run_check().stdout("[Uu]sage: ./morse[^\n]*", str_output="Usage: ./morse <code>")
        
        run_check("...---...").stdout("SOS")

        run_check("-..------.-.").stdout("DOOR")


@check50.check()
def formule():
    """formule werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("formule") as run_check:
        
        (run_check()
            .stdin("hello world!")
            .stdout("geen fouten", str_output="Er zijn geen fouten."))

        (run_check()
            .stdin("(a + b - (c * d))")
            .stdout("geen fouten", str_output="Er zijn geen fouten."))

        (run_check()
            .stdin(")a + b(")
            .stdout("te vroeg", str_output="Er wordt een haakje te vroeg gesloten."))

        (run_check()
            .stdin("a + (c * d")
            .stdout("te weinig", str_output="Er worden te weinig haakjes gesloten."))
        

@check50.check()
def tennis():
    """tennis werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("tennis") as run_check:
        (run_check("tennis")
            .stdin("hello")
            .stdin("world")
            .stdout("1 wint", str_output="Speler 1 wint!"))

        (run_check("tennis")
            .stdin("dat")
            .stdin("tentamen")
            .stdin("nooit")
            .stdin("top")
            .stdin("wijk")
            .stdout("2 wint", str_output="Speler 2 wint!"))


@check50.check()
def streep():
    """streep werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("streep") as run_check:

        run_check().stdout("([Uu]sage:?)? ./streep[^\n]*", str_output="Usage: ./streep <height> <width>")
        
        (run_check("15", "5")
            .stdout("#\s*\n", str_output="#\n")
            .stdout(" #\s*\n", str_output=" #\n")
            .stdout("  #\s*\n", str_output="  #\n")
            .stdout("   #\s*\n", str_output="   #\n")
            .stdout("    #\s*\n", str_output="    #\n")
            .stdout("#\s*\n", str_output="#\n")
            .stdout(" #\s*\n", str_output=" #\n")
            .stdout("  #\s*\n", str_output="  #\n")
            .stdout("   #\s*\n", str_output="   #\n")
            .stdout("    #\s*\n", str_output="    #\n")
            .stdout("#\s*\n", str_output="#\n")
            .stdout(" #\s*\n", str_output=" #\n")
            .stdout("  #\s*\n", str_output="  #\n")
            .stdout("   #\s*\n", str_output="   #\n")
            .stdout("    #\s*\n", str_output="    #\n"))

        (run_check("4", "3")
            .stdout("#\s*\n", str_output="#\n")
            .stdout(" #\s*\n", str_output=" #\n")
            .stdout("  #\s*\n", str_output="  #\n")
            .stdout("#\s*\n", str_output="#\n"))

        (run_check("7", "2")
            .stdout("#\s*\n", str_output="#\n")
            .stdout(" #\s*\n", str_output=" #\n")
            .stdout("#\s*\n", str_output="#\n")
            .stdout(" #\s*\n", str_output=" #\n")
            .stdout("#\s*\n", str_output="#\n")
            .stdout(" #\s*\n", str_output=" #\n")
            .stdout("#\s*\n", str_output="#\n"))


@check50.check()
def som():
    """som werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("som") as run_check:

        (run_check()
            .stdin("hello12world34")
            .stdout("46", str_output="De som[^\d]*46"))

        (run_check()
            .stdin("2 vliegen in 1 klap")
            .stdout("3", str_output="De som[^\d]*3"))
        
        (run_check()
            .stdin("nee")
            .stdout("0", str_output="De som[^\d]*0"))


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
