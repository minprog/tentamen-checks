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


@check50.check()
def hoofdletters():
    """hoofdletters is correct"""
    command = make_runnable("hoofdletters")

    # check example 1
    (check50.run(command)
        .stdin("Er zijn geen goede schrijvers.")
        .stdout("1 woord met een hoofdletter"))

    # check example 2
    (check50.run(command)
        .stdin("Obi-Wan Kenobi nam zijn taak vrij serieus")
        .stdout("2 woorden met een hoofdletter"))

    # check example 3
    (check50.run(command)
        .stdin("Het leven op zondag begon zonder Onrust.")
        .stdout("2 woorden met een hoofdletter"))

    # check example 4
    (check50.run(command)
        .stdin("ergens heeft het ook wel wat")
        .stdout("0 woorden met een hoofdletter"))


@check50.check()
def regen():
    """regen is correct"""
    command = make_runnable("regen")

    # check example 1
    (check50.run(command)
        .stdin("12")
        .stdin("12")
        .stdin("999")
        .stdout("Gemiddeld 12 millimeter"))

    # check example 2
    (check50.run(command)
        .stdin("12")
        .stdin("6")
        .stdin("3")
        .stdin("999")
        .stdout("Gemiddeld 7 millimeter"))

    # check example 3
    (check50.run(command)
        .stdin("999")
        .stdout("Dat kan niet"))

    # check example 4
    (check50.run(command)
        .stdin("12")
        .stdin("11")
        .stdin("999")
        .stdout("Gemiddeld 11 millimeter"))


@check50.check()
def spraaksynthese():
    """spraaksynthese is correct"""
    command = make_runnable("spraaksynthese")

    # check example 1
    (check50.run(command)
        .stdin("123")
        .stdout("een\n")
        .stdout("twee\n")
        .stdout("drie"))

    # check example 2
    (check50.run(command)
        .stdin("4210")
        .stdout("vier\n")
        .stdout("twee\n")
        .stdout("een\n")
        .stdout("nul"))


@check50.check()
def email_validator():
    """email-validator is correct"""
    command = make_runnable("mail")

    # check example 1
    (check50.run(command)
        .stdin("mdaks@gmail.com")
        .stdout("Geldig"))

    # check example 2
    (check50.run(command)
        .stdin("a@gmail.nl")
        .stdout("Geldig"))

    # check example 3
    (check50.run(command)
        .stdin("@")
        .stdout("Ongeldig"))

    # check example 4
    (check50.run(command)
        .stdin("me.@com")
        .stdout("Ongeldig"))

    # check example 5
    (check50.run(command)
        .stdin("m.raak@student.uva.nl")
        .stdout("Geldig"))


def make_runnable(name):
    if os.path.exists(f"{name}.c"):
        check50.c.compile(f"{name}.c", "-lcs50")
        return f"./{name}"

    if os.path.exists(f"{name}.py"):
        return f"{sys.executable} {name}.py"

    raise check50.Failure(f"{name} is niet aanwezig")