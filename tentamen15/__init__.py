import check50
import check50.c
import check50.internal
import contextlib
import os
import sys
import glob


@check50.check()
def startswith():
    """startswith werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("startswith") as run_check:
        run_check("abd").stdin("alfa").stdin("bravo").stdin("charlie").stdin("delta").stdin("echo").stdout("alfa\nbravo\ndelta\n")
        
        run_check("aeiouy").stdin("alleen").stdin("woorden").stdin("die").stdin("beginnen").stdin("met").stdin("een").stdin("klinker").stdout("alleen\neen\n")
        
        out = run_check("efg").stdout()
        if out != "":
            raise check50.Failure(f"expected ./startswith efg to produce no output, but got: {out}")

        run_check().stdout("gebruik")


@check50.check()
def dagplanner():
    """dagplanner werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("dagplanner") as run_check:
        (run_check()
            .stdin("algoritmen & heuristieken")
            .stdin("11")
            .stdin("programmeerproject")
            .stdin("15")
            .stdin("stop")
            .stdout("9 uur:", regex=False)
            .stdout("11 uur: algoritmen & heuristieken", regex=False)
            .stdout("13 uur:", regex=False)
            .stdout("15 uur: programmeerproject", regex=False))

        (run_check()
            .stdin("scientific programming 1")
            .stdin("8")
            .stdin("16")
            .stdin("15")
            .stdin("kunstgeschiedenis")
            .stdin("10")
            .stdin("9")
            .stdin("inleiding logica")
            .stdin("9")
            .stdin("stop")
            .stdout("9 uur: inleiding logica", regex=False)
            .stdout("11 uur:", regex=False)
            .stdout("13 uur:", regex=False)
            .stdout("15 uur: scientific programming 1", regex=False))


@check50.check()
def tetris():
    """tetris werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("tetris") as run_check:
        (run_check(".......... .......... ........XX XXXXXXXXXX .XXXXXXXXX XXXXXXXXXX")
            .stdout("gevulde rijen: 2", regex=False))
        
        (run_check("X.. XXX .X.")
            .stdout("gevulde rijen: 1", regex=False))
        
        (run_check("XXXX XXXX XXXX")
            .stdout("gevulde rijen: 3", regex=False))
        
        (run_check("... ... ... ...")
            .stdout("gevulde rijen: 0", regex=False))
        
        (run_check()
            .stdout("gevulde rijen: 0", regex=False))


@check50.check()
def bsn():
    """bsn werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("bsn") as run_check:        
        run_check("111222333").stdout("ja")
        run_check("987654321").stdout("nee")
        run_check("111222332").stdout("nee")
        run_check("123456782").stdout("ja")
        run_check("12345").stdout("bsn moet precies 9 cijfers lang zijn", regex=False)
        run_check().stdout("Gebruik: ./bsn <nummer>", regex=False)


@check50.check()
def calculator():
    """calculator werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("calculator") as run_check:
        (run_check()
            .stdin("1000")
            .stdin("/")
            .stdin("100")
            .stdout("= 10", regex=False)
            .stdin("+")
            .stdin("9")
            .stdout("= 19", regex=False)
            .stdin("-")
            .stdin("17")
            .stdout("= 2", regex=False)
            .stdin("+")
            .stdin("30")
            .stdout("= 32", regex=False)
            .stdin("*")
            .stdin("-3")
            .stdout("= -96", regex=False)
            .stdin("S"))
        
        (run_check()
            .stdin("4")
            .stdin("*")
            .stdin("4")
            .stdout("= 16", regex=False)
            .stdin("/")
            .stdin("3")
            .stdout("= 5", regex=False)
            .stdin("H")
            .stdin("(")
            .stdin("+")
            .stdin("2")
            .stdout("= 7", regex=False)
            .stdin("S"))
        
        (run_check()
            .stdin("-4")
            .stdin("+")
            .stdin("0")
            .stdout("= -4", regex=False)
            .stdin("^")
            .stdin("3")
            .stdout("= -64", regex=False)
            .stdin("+")
            .stdin("62")
            .stdout("= -2", regex=False)
            .stdin("*")
            .stdin("-2")
            .stdout("= 4", regex=False)
            .stdin("S"))


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
