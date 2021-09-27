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
        .stdout("311(?!\d)", str_output="311"))

    # check example 2
    (check50.run("./vakantie")
        .stdin("t")
        .stdin("10")
        .stdout("718(?!\d)", str_output="718"))

    # check example 3
    (check50.run("./vakantie")
        .stdin("a")
        .stdin("7")
        .stdout("582(?!\d)", str_output="582"))


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

