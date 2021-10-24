import check50
import check50.c
import os
import sys
import re


@check50.check()
def reistijd():
    """reistijd is correct"""
    command = make_runnable("reistijd")

    # check example 1
    (check50.run(command)
        .stdin("2.6")
        .stdin("200")
        .stdin("B")
        .stdin("4.2")
        .stdout("reis kost je ongeveer 205 minuten", regex=False))

    # check example 2
    (check50.run(command)
        .stdin("5.5")
        .stdin("50.5")
        .stdin("F")
        .stdin("3")
        .stdout("reis kost je ongeveer 73 minuten", regex=False))


@check50.check()
def elektrisch_rijden():
    """elektrisch rijden is correct"""
    command = make_runnable("elektrisch")

    def to_regex(answer):
        # escape all |
        answer_regex = [re.sub("\|", "\|", l) for l in answer]

        # escape all .
        answer_regex = [re.sub("\.", "\.", l) for l in answer_regex]

        # replace all spaces with "[ ]*"
        return [re.sub("[ ]+", "[ ]*", l) for l in answer_regex]

    # check example 1
    check = check50.run(command).stdin("1.95").stdin("0.3")
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

    # check example 2
    check = check50.run(command).stdin("2.1").stdin("0.33")
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
    command = make_runnable("huis")

    # check example 1
    check = check50.run(command).stdin("4")
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
    check = check50.run(command).stdin("2")
    answer = (
        " x(\s)*\n"
        "x x(\s)*\n"
        "x x(\s)*\n"
        "xxx(\s)*\n"
    )
    check.stdout(answer)

    # check example 3
    check = check50.run(command).stdin("5")
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
    command = make_runnable("alfabet")

    # check example 1
    (check50.run(command)
        .stdin("Taylor")
        .stdin("Lana")
        .stdout("Lana first"))

    # check example 2
    (check50.run(command)
        .stdin("shark")
        .stdin("sWoRd")
        .stdout("shark first"))

    # check example 3
    (check50.run(command)
        .stdin("Daantje")
        .stdin("Daan")
        .stdout("Daan first"))

    # check example 4
    (check50.run(command)
        .stdin("amanda")
        .stdin("Amanda")
        .stdout("No need to decide"))


def make_runnable(name):
    if os.path.exists(f"{name}.c"):
        check50.c.compile(f"{name}.c", "-lcs50")
        return f"./{name}"

    if os.path.exists(f"{name}.py"):
        return f"{sys.executable} {name}.py"

    raise check50.Failure(f"{name} is niet aanwezig")