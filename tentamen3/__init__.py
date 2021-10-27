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


@check50.check()
def postzegels():
    """postzegels is correct"""
    command = make_runnable("postzegels")

    # check example 1
    (check50.run(command)
        .stdin("130")
        .stdin("2")
        .stdin("N")
        .stdout("Plak 2 postzegel(s)", regex=False))

    # check example 2
    (check50.run(command)
        .stdin("300")
        .stdin("2")
        .stdin("S")
        .stdout("Plak 6 postzegel(s)", regex=False))

    # check example 3
    (check50.run(command)
        .stdin("120")
        .stdin("2")
        .stdin("N")
        .stdout("Plak 1 postzegel(s)", regex=False))

    # check example 4
    (check50.run(command)
        .stdin("120")
        .stdin("5")
        .stdin("N")
        .stdout("Dit kan niet met de post"))

    # check example 5
    (check50.run(command)
        .stdin("120")
        .stdin("3")
        .stdin("A")
        .stdin("B")
        .stdin("D")
        .stdout("Plak 2 postzegel(s)", regex=False))


@check50.check()
def trapezium():
    """trapezium is correct"""
    command = make_runnable("trapezium")

    # check example 1
    check = check50.run(command).stdin("5")
    answer = (
        "    ##########(\s)*\n"
        "   #        #(\s)*\n"
        "  #        #(\s)*\n"
        " #        #(\s)*\n"
        "##########(\s)*"
    )
    check.stdout(answer)

    # check example 2
    check = check50.run(command).stdin("15")
    answer = (
        "              ##############################(\s)*\n"
        "             #                            #(\s)*\n"
        "            #                            #(\s)*\n"
        "           #                            #(\s)*\n"
        "          #                            #(\s)*\n"
        "         #                            #(\s)*\n"
        "        #                            #(\s)*\n"
        "       #                            #(\s)*\n"
        "      #                            #(\s)*\n"
        "     #                            #(\s)*\n"
        "    #                            #(\s)*\n"
        "   #                            #(\s)*\n"
        "  #                            #(\s)*\n"
        " #                            #(\s)*\n"
        "##############################(\s)*"
    )
    check.stdout(answer)

    # check example 3
    check = (check50.run(command)
        .stdin("-3")
        .stdin("40")
        .stdin("3")
        .stdin("5"))
    answer = (
        "    ##########(\s)*\n"
        "   #        #(\s)*\n"
        "  #        #(\s)*\n"
        " #        #(\s)*\n"
        "##########(\s)*"
    )
    check.stdout(answer)


@check50.check()
def spraaksynthese():
    """spraaksynthese is correct"""
    command = make_runnable("spraaksynthese", "synthese")

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

    # check example 3
    (check50.run(command)
        .stdin("12o4")
        .stdout("Dat is geen getal"))


@check50.check()
def wachtwoorden():
    """wachtwoorden is correct"""
    command = make_runnable("wachtwoord")

    # check example 1
    (check50.run(command)
        .stdin("aaa")
        .stdout("Niet sterk genoeg")
        .stdin("AAA")
        .stdout("Niet sterk genoeg")
        .stdin("aaaaAAAA")
        .stdout("Niet sterk genoeg")
        .stdin("aaaaaaaaa")
        .stdout("Niet sterk genoeg")
        .stdin("AAAAAAAAA")
        .stdout("Niet sterk genoeg")
        .stdin("000000000")
        .stdout("Niet sterk genoeg")
        .stdin("aaaaAAAAA0000")
        .stdout("Sterk genoeg"))

    # check example 2
    (check50.run(command)
        .stdin("abc0D")
        .stdout("Niet sterk genoeg")
        .stdin("abc0Defg")
        .stdout("Sterk genoeg"))


def make_runnable(*names):
    for name in names:
        if os.path.exists(f"{name}.c"):
            check50.c.compile(f"{name}.c", "-lcs50")
            return f"./{name}"

        if os.path.exists(f"{name}.py"):
            return f"{sys.executable} {name}.py"

    raise check50.Failure(f"{' en/of '.join(names)} {'is' if len(names) == 1 else 'zijn'} niet aanwezig")