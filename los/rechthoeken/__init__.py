import check50
import check50.c
import os
import sys


@check50.check()
def rechthoeken():
    """rechthoeken is correct"""
    command = make_runnable("rechthoeken")

    # check example 1
    (check50.run(command)
        .stdin("45")
        .stdin("33")
        .stdin("22")
        .stdin("12")
        .stdin("V")
        .stdout("1221(?!\d)", str_output="1221"))

    # check example 2
    (check50.run(command)
        .stdin("1")
        .stdin("43")
        .stdin("39")
        .stdin("31")
        .stdin("S")
        .stdout("1252(?!\d)", str_output="1252"))

    # check example 3
    (check50.run(command)
        .stdin("1")
        .stdin("43")
        .stdin("39")
        .stdin("31")
        .stdin("1")
        .stdout("43(?!\d)", str_output="43"))

    # check example 4
    (check50.run(command)
        .stdin("1")
        .stdin("43")
        .stdin("39")
        .stdin("31")
        .stdin("X")
        .stdout("is geen geldige keuze"))

    # check example 5
    (check50.run(command)
        .stdin("1")
        .stdin("43")
        .stdin("39")
        .stdin("31")
        .stdin("0")
        .stdout("is geen geldige keuze"))


def make_runnable(name):
    if os.path.exists(f"{name}.c"):
        check50.c.compile(f"{name}.c", "-lcs50")
        return f"./{name}"

    if os.path.exists(f"{name}.py"):
        return f"{sys.executable} {name}.py"

    raise check50.Failure(f"{name} is niet aanwezig")
