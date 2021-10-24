import check50
import check50.c

@check50.check()
def vakantie():
    """vakantie.c is correct"""
    check50.exists("vakantie.c")
    check50.c.compile("vakantie.c", "-lcs50")

    # check example 1
    (check50.run("./vakantie")
        .stdin("v")
        .stdin("1")
        .stdout("319(?!\d)", str_output="319"))

    # check example 2
    (check50.run("./vakantie")
        .stdin("t")
        .stdin("10")
        .stdout("721(?!\d)", str_output="721"))

    # check example 3
    (check50.run("./vakantie")
        .stdin("a")
        .stdin("7")
        .stdout("587(?!\d)", str_output="587"))


@check50.check()
def caffeine():
    """caffeine.c is correct"""
    check50.exists("caffeine.c")
    check50.c.compile("caffeine.c", "-lcs50")

    # check example 1
    output = (check50.run("./caffeine")
        .stdin("2")
        .stdin("1")
        .stdin("0")
        .stdin("0")
        .stdin("22")
        .stdout("225(?!\d)", str_output="225")
        .stdout())

    if "veilige" not in output or "te veel" in output:
        raise check50.Failure()

    # check example 2
    output = (check50.run("./caffeine")
        .stdin("2")
        .stdin("0")
        .stdin("2")
        .stdin("0")
        .stdin("17")
        .stdout("340(?!\d)", str_output="340")
        .stdout())

    if "veilige" in output or "te veel" not in output:
        raise check50.Failure()

    # check example 3
    output = (check50.run("./caffeine")
        .stdin("0")
        .stdin("0")
        .stdin("0")
        .stdin("1")
        .stdin("10")
        .stdout("40(?!\d)", str_output="40")
        .stdout())

    if "veilige" in output or "te veel" not in output:
        raise check50.Failure()

    # check example 4
    output = (check50.run("./caffeine")
        .stdin("5")
        .stdin("0")
        .stdin("0")
        .stdin("0")
        .stdin("38")
        .stdout("450(?!\d)", str_output="450")
        .stdout())

    if "veilige" in output or "te veel" not in output:
        raise check50.Failure()


@check50.check()
def rna():
    """rna.c is correct"""
    check50.exists("rna.c")
    check50.c.compile("rna.c", "-lcs50")

    # check example 1
    (check50.run("./rna")
        .stdin("ATGC")
        .stdout("UACG(?!\w)", str_output="UACG"))

    # check example 2
    (check50.run("./rna")
        .stdin("AAF")
        .stdout("[O|o]ngeldige", str_output="Ongeldige"))

    # check example 3
    (check50.run("./rna")
        .stdin("AAGGTTCCAA")
        .stdout("UUCCAAGGUU(?!\w)", str_output="UUCCAAGGUU"))


@check50.check()
def driehoek():
    """driehoek.c is correct"""
    check50.exists("driehoek.c")
    check50.c.compile("driehoek.c", "-lcs50")

    # check example 1
    check = check50.run("./driehoek").stdin("5")
    answer = (
"    ##(\s)*\n"
"   #  #(\s)*\n"
"  #    #(\s)*\n"
" #      #(\s)*\n"
"##########(\s)*\n")
    check.stdout(answer)

    # check example 2
    check = check50.run("./driehoek").stdin("20")
    answer = (
"                   ##(\s)*\n"
"                  #  #(\s)*\n"
"                 #    #(\s)*\n"
"                #      #(\s)*\n"
"               #        #(\s)*\n"
"              #          #(\s)*\n"
"             #            #(\s)*\n"
"            #              #(\s)*\n"
"           #                #(\s)*\n"
"          #                  #(\s)*\n"
"         #                    #(\s)*\n"
"        #                      #(\s)*\n"
"       #                        #(\s)*\n"
"      #                          #(\s)*\n"
"     #                            #(\s)*\n"
"    #                              #(\s)*\n"
"   #                                #(\s)*\n"
"  #                                  #(\s)*\n"
" #                                    #(\s)*\n"
"########################################(\s)*\n")
    check.stdout(answer)


@check50.check()
def temperaturen():
    """temperaturen.c is correct"""
    check50.exists("temperaturen.c")
    check50.c.compile("temperaturen.c", "-lcs50")

    # check example 1
    check = check50.run("./temperaturen").stdin("C").stdin("0").stdin("20").stdin("5")
    answer = (
        "(\s)*C(\s)*\|(\s)*F(\s)*\n"
        "(\s)*0(\s)*\|(\s)*32(\s)*\n"
        "(\s)*5(\s)*\|(\s)*41(\s)*\n"
        "(\s)*10(\s)*\|(\s)*50(\s)*\n"
        "(\s)*15(\s)*\|(\s)*59(\s)*\n"
        "(\s)*20(\s)*\|(\s)*68(\s)*\n"
    )
    check.stdout(answer)

    # check example 2
    check = check50.run("./temperaturen").stdin("F").stdin("0").stdin("10").stdin("2")
    answer = (
        "(\s)*F(\s)*\|(\s)*C(\s)*\n"
        "(\s)*0(\s)*\|(\s)*-17(\s)*\n"
        "(\s)*2(\s)*\|(\s)*-16(\s)*\n"
        "(\s)*4(\s)*\|(\s)*-15(\s)*\n"
        "(\s)*6(\s)*\|(\s)*-14(\s)*\n"
        "(\s)*8(\s)*\|(\s)*-13(\s)*\n"
        "(\s)*10(\s)*\|(\s)*-12(\s)*\n"
    )
    check.stdout(answer)

    # check example 3
    check = check50.run("./temperaturen").stdin("F").stdin("100").stdin("0").stdin("3")
    answer = (
        "(\s)*F(\s)*\|(\s)*C(\s)*\n"
    )
    check.stdout(answer)

    # check example 4
    check = check50.run("./temperaturen").stdin("c").stdin("v").stdin("F").stdin("0").stdin("9").stdin("-3").stdin("0").stdin("3")
    answer = (
        "(\s)*F(\s)*\|(\s)*C(\s)*\n"
        "(\s)*0(\s)*\|(\s)*-17(\s)*\n"
        "(\s)*3(\s)*\|(\s)*-16(\s)*\n"
        "(\s)*6(\s)*\|(\s)*-14(\s)*\n"
        "(\s)*9(\s)*\|(\s)*-12(\s)*\n"
    )
    check.stdout(answer)
