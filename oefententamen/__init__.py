import check50
import check50.c

@check50.check()
def trein():
    """trein.c is correct"""
    check50.exists("trein.c")
    check50.c.compile("trein.c", "-lcs50")

    # check example 1
    (check50.run("./trein")
        .stdin("100")
        .stdin("50")
        .stdout("11\.75(?!\d)", str_output="11.75")
        .stdout("59(?!\d)", str_output="59"))

    # check example 2
    (check50.run("./trein")
        .stdin("20")
        .stdin("75")
        .stdout("5\.63(?!\d)", str_output="5.63")
        .stdout("141(?!\d)", str_output="141"))


@check50.check()
def babysitten():
    """babysitten.c is correct"""
    check50.exists("babysitten.c")
    check50.c.compile("babysitten.c", "-lcs50")

    # check example 1
    (check50.run("./babysitten")
        .stdin("1930")
        .stdin("0047")
        .stdout("40(?!\d)", str_output="40"))

    # check example 2
    (check50.run("./babysitten")
        .stdin("2045")
        .stdin("0200")
        .stdout("44(?!\d)", str_output="44"))

    # check example 3
    (check50.run("./babysitten")
        .stdin("2040")
        .stdin("2320")
        .stdout("24(?!\d)", str_output="24"))

    # check example 4
    (check50.run("./babysitten")
        .stdin("0033")
        .stdin("0133")
        .stdout("20(?!\d)", str_output="20"))

@check50.check()
def tram():
    """tram.c is correct"""
    check50.exists("tram.c")
    check50.c.compile("tram.c", "-lcs50")

    # check example 1
    check = check50.run("./tram").stdin("25").stdout("10")
    try:
        check.stdout("\d")
    except check50.Failure:
        pass
    else:
        raise check50.Failure("It looks like you are printing more than one number, please print just the percentage")

    # check example 2
    check = check50.run("./tram").stdin("60").stdout("4")
    try:
        check.stdout("\d")
    except check50.Failure:
        pass
    else:
        raise check50.Failure("It looks like you are printing more than one number, please print just the percentage")


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

