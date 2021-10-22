import check50
import check50.c

@check50.check()
def rechthoeken():
    """rechthoeken.c is correct"""
    check50.exists("rechthoeken.c")
    check50.c.compile("rechthoeken.c", "-lcs50")

    # check example 1
    (check50.run("./rechthoeken")
        .stdin("45")
        .stdin("33")
        .stdin("22")
        .stdin("12")
        .stdin("V")
        .stdout("1221(?!\d)", str_output="12.21"))

    # check example 2
    (check50.run("./rechthoeken")
        .stdin("1")
        .stdin("43")
        .stdin("39")
        .stdin("31")
        .stdin("S")
        .stdout("1252(?!\d)", str_output="12.52"))

    # check example 3
    (check50.run("./rechthoeken")
        .stdin("1")
        .stdin("43")
        .stdin("39")
        .stdin("31")
        .stdin("1")
        .stdout("43(?!\d)", str_output="0.43"))

    # check example 4
    (check50.run("./rechthoeken")
        .stdin("1")
        .stdin("43")
        .stdin("39")
        .stdin("31")
        .stdin("X")
        .stdout("is geen geldige keuze"))

    # check example 5
    (check50.run("./rechthoeken")
        .stdin("1")
        .stdin("43")
        .stdin("39")
        .stdin("31")
        .stdin("0")
        .stdout("is geen geldige keuze"))