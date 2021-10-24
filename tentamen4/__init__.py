import check50
import check50.c
import os
import sys


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


def make_runnable(name):
    if os.path.exists(f"{name}.c"):
        check50.c.compile(f"{name}.c", "-lcs50")
        return f"./{name}"

    if os.path.exists(f"{name}.py"):
        return f"{sys.executable} {name}.py"

    raise check50.Failure(f"{name} is niet aanwezig")