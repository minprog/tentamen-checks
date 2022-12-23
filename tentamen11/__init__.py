import check50
import check50.c
import check50.internal
import contextlib
import os
import sys
import glob

@check50.check()
def spam():
    """spam werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("spam") as run_check:

        test_string = "Ca$hh M0n3y"
        output = (run_check()
            .stdin(test_string)
            .stdout("30(?!\d)", str_output="30")
            .stdout())

        if "spam" not in output or "normaal" in output:
            raise check50.Failure(f"{test_string} should be spam")

        test_string = "Deze email is normaal."
        output = (run_check()
            .stdin(test_string)
            .stdout("5(?!\d)", str_output="5")
            .stdout())

        if "spam" in output or "normaal" not in output:
            raise check50.Failure(f"{test_string} should not be spam")

@check50.check()
def regen():
    """regen werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("regen") as run_regen:

        (run_regen()
            .stdin("12")
            .stdin("12")
            .stdin("999")
            .stdout("[Gg]emiddeld 12(?!\d)", str_output="Gemiddeld 12 millimeter"))

        (run_regen()
            .stdin("12")
            .stdin("6")
            .stdin("3")
            .stdin("999")
            .stdout("[gG]emiddeld 7(?!\d)", str_output="Gemiddeld 7 millimeter"))

        (run_regen()
            .stdin("999")
            .stdout("[Dd][ai]t kan niet", str_output="Dat kan niet"))

        (run_regen()
            .stdin("12")
            .stdin("11")
            .stdin("999")
            .stdout("[Gg]emiddeld 11(?!\d)", str_output="Gemiddeld 11 millimeter"))

@check50.check()
def gelijkbenig():
    """gelijkbenig werkt precies zoals de voorbeelden in de opdracht"""
    command = make_runnable("gelijkbenig")

    # check example 1
    check = check50.run(command).stdin("5")
    answer = (
        "    #(\s)*\n"
        "   # #(\s)*\n"
        "  #   #(\s)*\n"
        " #     #(\s)*\n"
        "#########(\s)*"
    )
    check.stdout(answer)

    # check example 2
    check = check50.run(command).stdin("15")
    answer = (
        "              #(\s)*\n"
        "             # #(\s)*\n"
        "            #   #(\s)*\n"
        "           #     #(\s)*\n"
        "          #       #(\s)*\n"
        "         #         #(\s)*\n"
        "        #           #(\s)*\n"
        "       #             #(\s)*\n"
        "      #               #(\s)*\n"
        "     #                 #(\s)*\n"
        "    #                   #(\s)*\n"
        "   #                     #(\s)*\n"
        "  #                       #(\s)*\n"
        " #                         #(\s)*\n"
        "#############################(\s)*"
    )
    check.stdout(answer)

    # check example 3
    check = (check50.run(command)
        .stdin("-3")
        .stdin("40")
        .stdin("3")
        .stdin("5"))
    answer = (
        "    #(\s)*\n"
        "   # #(\s)*\n"
        "  #   #(\s)*\n"
        " #     #(\s)*\n"
        "#########(\s)*"
    )
    check.stdout(answer)

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
        run.stdout("(Totalen:)?[\s\n]*" + "\n".join([f"\s*{k}\s*:\s*{output.get(k,0)}\s*" for k in [1,2,3,4,5,6]]), "Totalen:\n" + "\n".join([f"{k}: {output.get(k,0)}" for k in [1,2,3,4,5,6]]))

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
            .stdout("(Usage: )?./absoluut num..."))



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
