import check50
import check50.c
import check50.internal
import contextlib
import os
import sys
import re

@check50.check()
def reistijd():
    """reistijd is correct"""
    with get_check_factory("reistijd") as create_check:

        # check example 1
        with create_check() as check:
            (check
                .stdin("2.6")
                .stdin("200")
                .stdin("B")
                .stdin("4.2")
                .stdout("reis kost je ongeveer 205 minuten"))

        # check example 2
        with create_check() as check:
            (check
                .stdin("5.5")
                .stdin("50.5")
                .stdin("F")
                .stdin("3")
                .stdout("reis kost je ongeveer 73 minuten"))


@check50.check()
def elektrisch_rijden():
    """elektrisch rijden is correct"""
    def to_regex(answer):
        # escape all |
        answer_regex = [re.sub("\|", "\|", l) for l in answer]

        # escape all .
        answer_regex = [re.sub("\.", "\.", l) for l in answer_regex]

        # replace all spaces with "[ ]*"
        return [re.sub("[ ]+", "[ ]*", l) for l in answer_regex]

    with get_check_factory("elektrisch") as create_check:

        # check example 1
        with create_check() as check:
            check.stdin("1.95").stdin("0.3")
            answer = [
                "| KM    | Elektrisch | Benzine  |\n",
                "| 100   |  6.00      |  7.80    |\n",
                "| 200   | 12.00      | 15.60    |\n",
                "| 300   | 18.00      | 23.40    |\n",
                "| 400   | 24.00      | 31.20    |\n",
                "| 500   | 30.00      | 39.00    |\n",
                "| 600   | 36.00      | 46.80    |\n",
                "| 700   | 42.00      | 54.60    |\n",
                "| 800   | 48.00      | 62.40    |\n",
                "| 900   | 54.00      | 70.20    |"
            ]
            for line, line_regex in zip(answer, to_regex(answer)):
                check.stdout(line_regex, str_output=line)

        # # check example 2
        with create_check() as check:
            check.stdin("2.1").stdin("0.33")
            answer = [
                "| KM    | Elektrisch | Benzine  |\n",
                "| 100   |  6.60      |  8.40    |\n",
                "| 200   | 13.20      | 16.80    |\n",
                "| 300   | 19.80      | 25.20    |\n",
                "| 400   | 26.40      | 33.60    |\n",
                "| 500   | 33.00      | 42.00    |\n",
                "| 600   | 39.60      | 50.40    |\n",
                "| 700   | 46.20      | 58.80    |\n",
                "| 800   | 52.80      | 67.20    |\n",
                "| 900   | 59.40      | 75.60    |"
            ]
            for line, line_regex in zip(answer, to_regex(answer)):
                check.stdout(line_regex, str_output=line)


@check50.check()
def huis():
    """huis is correct"""
    with get_check_factory("huis") as create_check:

        # check example 1
        with create_check() as check:
            check.stdin("4")
            answer = (
                "   x(\s)*\n"
                "  x x(\s)*\n"
                " x   x(\s)*\n"
                "x     x(\s)*\n"
                "x     x(\s)*\n"
                "x     x(\s)*\n"
                "x     x(\s)*\n"
                "xxxxxxx(\s)*\n"
            )
            check.stdout(answer)

        # check example 2
        with create_check() as check:
            check.stdin("2")
            answer = (
                " x(\s)*\n"
                "x x(\s)*\n"
                "x x(\s)*\n"
                "xxx(\s)*\n"
            )
            check.stdout(answer)

        # check example 3
        with create_check() as check:
            check.stdin("5")
            answer = (
                "    x(\s)*\n"
                "   x x(\s)*\n"
                "  x   x(\s)*\n"
                " x     x(\s)*\n"
                "x       x(\s)*\n"
                "x       x(\s)*\n"
                "x       x(\s)*\n"
                "x       x(\s)*\n"
                "x       x(\s)*\n"
                "xxxxxxxxx(\s)*\n"
            )
            check.stdout(answer)


@check50.check()
def alfabet():
    """alfabet is correct"""
    with get_check_factory("alfabet") as create_check:

        # check example 1
        with create_check() as check:
            check.stdin("Taylor").stdin("Lana")
            check.stdout("Lana first")

        # check example 2
        with create_check() as check:
            check.stdin("shark").stdin("sWoRd")
            check.stdout("shark first")

        # check example 3
        with create_check() as check:
            check.stdin("Daantje").stdin("Daan")
            check.stdout("Daan first")

        # check example 4
        with create_check() as check:
            check.stdin("amanda").stdin("Amanda")
            check.stdout("No need to decide")


# All outputs from every run in a check
OUTPUTS = []

# OUTPUTS gets cleared before every check
check50.internal.register.before_every(OUTPUTS.clear)

# dump the contents of OUTPUTS in the data.output key of the json output
check50.internal.register.after_every(lambda: check50.data(output="\n".join(OUTPUTS)))


class StdoutStream:
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
def get_check_factory(*names):
    command = make_runnable(*names)
    outputs = []

    @contextlib.contextmanager
    def create_check():
        """
        Yields a check with a stream attached to stdout and stdin.
        Once the check completes (finally) append all text in stream to OUTPUTS.
        """
        try:
            check = check50.run(command)

            stream = StdoutStream()
            check.process.logfile = stream

            yield check
        finally:
            outputs.append(stream.text)
    try:
        yield create_check
    finally:
        check50.data(output="\n".join(outputs))


def make_runnable(*names):
    for name in names:
        if os.path.exists(f"{name}.c"):
            check50.c.compile(f"{name}.c", "-lcs50")
            return f"./{name}"

        if os.path.exists(f"{name}.py"):
            return f"{sys.executable} {name}.py"

    raise check50.Failure(f"{' en/of '.join(names)} {'is' if len(names) == 1 else 'zijn'} niet aanwezig")