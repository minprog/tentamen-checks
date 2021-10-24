import check50
import check50.c
import os
import sys


@check50.check()
def elektrisch_rijden():
    """elektrisch rijden is correct"""
    command = make_runnable("elektrisch")

    # check example 1
    (check50.run(command)
        .stdin("200")
        .stdout("rijden bespaart je 3.6 euro", regex=False))

    # check example 2
    (check50.run(command)
        .stdin("-2")
        .stdin("0")
        .stdin("500")
        .stdout("rijden bespaart je 9.0 euro", regex=False))


def make_runnable(name):
    if os.path.exists(f"{name}.c"):
        check50.c.compile(f"{name}.c", "-lcs50")
        return f"./{name}"

    if os.path.exists(f"{name}.py"):
        return f"{sys.executable} {name}.py"

    raise check50.Failure(f"{name} is niet aanwezig")