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
"    ##\n"
"   #  #\n"
"  #    #\n"
" #      #\n"
"##########\n")
    check.stdout(answer)

    # check example 2
    check = check50.run("./driehoek").stdin("20")
    answer = (
"                   ##\n"
"                  #  #\n"
"                 #    #\n"
"                #      #\n"
"               #        #\n"
"              #          #\n"
"             #            #\n"
"            #              #\n"
"           #                #\n"
"          #                  #\n"
"         #                    #\n"
"        #                      #\n"
"       #                        #\n"
"      #                          #\n"
"     #                            #\n"
"    #                              #\n"
"   #                                #\n"
"  #                                  #\n"
" #                                    #\n"
"########################################\n")
    check.stdout(answer)



@check50.check()
def temperaturen():
    """temperaturen.c is correct"""
    check50.exists("temperaturen.c")