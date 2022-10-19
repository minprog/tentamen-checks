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
def spam():
    """spam.c is correct"""
    check50.exists("spam.c")
    check50.c.compile("spam.c", "-lcs50")

    # check example 1
    output = (check50.run("./spam")
        .stdin("Ca$hh M0n3y")
        .stdout("30(?!\d)", str_output="30")
        .stdout())

    if "spam" not in output or "normaal" in output:
        raise check50.Failure()

    # check example 2
    output = (check50.run("./spam")
        .stdin("Dit was zeker geen spam!")
        .stdout("5(?!\d)", str_output="5")
        .stdout())

    if "spam" in output or "normaal" not in output:
        raise check50.Failure()


@check50.check()
def afgebroken():
    """afgebroken werkt precies zoals de voorbeelden in de opdracht"""
    with logged_check_factory("afgebroken") as run_check:

        (run_check()
            .stdin("Nederlanders worden steeds ouder, vooral door- dat ze na hun 65ste langer in leven blijven.")
            .stdout("Nederlanders worden steeds ouder, vooral doordat ze na hun 65ste langer in leven blijven."))

        (run_check()
            .stdin("Over de identiteit van de schutter zegt de po- litie: 'Als het de man is die we denken dat het is, dan is het een bekende van de politie.'")
            .stdout("Over de identiteit van de schutter zegt de politie: 'Als het de man is die we denken dat het is, dan is het een bekende van de politie.'"))

        (run_check()
            .stdin("Een 36-jarige Geldropse heeft deze week een in- breker in haar schuurtje net zo lang achtervolgd tot de politie arriveerde.")
            .stdout("Een 36-jarige Geldropse heeft deze week een inbreker in haar schuurtje net zo lang achtervolgd tot de politie arriveerde."))
