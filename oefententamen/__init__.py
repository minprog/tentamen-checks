import check50
import check50.c

@check50.check()
def trein():
    """trein.c is correct"""
    check50.exists("trein.c")
    check50.c.compile("trein.c")

    # check example 1
    check50.run("./trein").stdin("100").stdin("50").stdout("11,75").stdout("59")

    # check example 2
    check50.run("./trein").stdin("20").stdin("75").stdout("5.63").stdout("141")

@check50.check()
def babysitten():
    """babysitten.c is correct"""
    check50.exists("babysitten.c")

@check50.check()
def tram():
    """tram.c is correct"""
    check50.exists("tram.c")

@check50.check()
def driehoek():
    """driehoek.c is correct"""
    check50.exists("driehoek.c")

@check50.check()
def temperaturen():
    """temperaturen.c is correct"""
    check50.exists("temperaturen.c")