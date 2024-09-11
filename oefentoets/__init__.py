import check50
import check50.c

helpers = check50.internal.import_file(
    "helpers",
    check50.internal.check_dir / "../helpers/helpers.py"
)

@check50.check()
def makelaar():
    """makelaar werkt precies zoals de voorbeelden in de opdracht"""
    check50.exists("makelaar.c")

    main = r"""
int main(void)
{
    printf("55 m2, 1 sk, 1 bk, wijk 1\n");
    printf("De waarde van het huis is EUR %d,-\n\n", verkoopprijs(55, 1, 1, 1));

    printf("\n150 m2, 3 sk, 3 bk, wijk 1\n");
    printf("De waarde van het huis is EUR %d,-\n\n", verkoopprijs(150, 3, 3, 1));

    printf("\n150 m2, 3 sk, 3 bk, wijk 2\n");
    printf("De waarde van het huis is EUR %d,-\n", verkoopprijs(150, 3, 3, 2));
}
"""
    with helpers.replace_main("makelaar.c", main):
        with helpers.logged_check_factory("makelaar") as run_check:
            (run_check()
                .stdout("EUR 295000")
                .stdout("EUR 826200")
                .stdout("EUR 930000"))

@check50.check()
def header():
    """header werkt precies zoals de voorbeelden in de opdracht"""
    check50.exists("header.c")

    main = r"""
int main(void)
{
    header("Doug Lloyd", "02/10/2023", "Prints hello world");
    header("Martijn Stegeman", "01/05/2021", "Print Mario's piramide");
}
"""
    helpers.set_stdout_limit(80)

    with helpers.replace_main("header.c", main):
        with helpers.logged_check_factory("header") as run_check:

                (run_check()
                    .stdout("/*******************************************************************************", regex=False)
                    .stdout("* Author: Doug Lloyd                                                           *", regex=False)
                    .stdout("* Date: 02/10/2023                                                             *", regex=False)
                    .stdout("* Description: Prints hello world                                              *", regex=False)
                    .stdout("*******************************************************************************/", regex=False)
                    .stdout("/*******************************************************************************", regex=False)
                    .stdout("* Author: Martijn Stegeman                                                     *", regex=False)
                    .stdout("* Date: 01/05/2021                                                             *", regex=False)
                    .stdout("* Description: Print Mario's piramide                                          *", regex=False)
                    .stdout("*******************************************************************************/", regex=False))


@check50.check()
def collatz():
    """collatz werkt precies zoals de voorbeelden in de opdracht"""
    check50.exists("collatz.c")

    main = r"""
int main(void)
{
    printf("Collatz beginnend bij 8\n");
    collatz(8);
    printf("Collatz beginnend bij 10\n");
    collatz(10);
}
"""
    with helpers.replace_main("collatz.c", main):
        with helpers.logged_check_factory("collatz") as run_check:

            (run_check()
                .stdout("[S|s]tap 1: 8",  str_output="Stap 1: 8")
                .stdout("[S|s]tap 2: 4",  str_output="Stap 2: 4")
                .stdout("[S|s]tap 3: 2",  str_output="Stap 3: 2")
                .stdout("[S|s]tap 4: 1",  str_output="Stap 4: 1")
                .stdout("[S|s]tap 1: 10", str_output="Stap 1: 10")
                .stdout("[S|s]tap 2: 5",  str_output="Stap 2: 5")
                .stdout("[S|s]tap 3: 16", str_output="Stap 3: 16")
                .stdout("[S|s]tap 4: 8",  str_output="Stap 4: 8")
                .stdout("[S|s]tap 5: 4",  str_output="Stap 5: 4")
                .stdout("[S|s]tap 6: 2",  str_output="Stap 6: 2")
                .stdout("[S|s]tap 7: 1",  str_output="Stap 7: 1"))


@check50.check()
def spam():
    """spam werkt precies zoals de voorbeelden in de opdracht"""
    check50.exists("spam.c")

    main = r"""
int main(void)
{
    string subject1 = "CaZhh M0n3y";
    printf("-> \"%s\"\n", subject1);
    spam_check(subject1);

    string subject2 = "Dit was zeker geen spam!";
    printf("\n-> \"%s\"\n", subject2);
    spam_check(subject2);

    string subject3 = "";
    printf("\n-> \"%s\"\n", subject3);
    spam_check(subject3);
}
"""
    with helpers.replace_main("spam.c", main):
        with helpers.logged_check_factory("spam") as run_check:

            (run_check()
                .stdout('-> "CaZhh M0n3y"', regex=False)
                .stdout("Er zijn 20 procent niet-alfabetische karakters.", regex=False)
                .stdout("Deze mail is spam.", regex=False)
                .stdout('-> "Dit was zeker geen spam!"', regex=False)
                .stdout("Er zijn 5 procent niet-alfabetische karakters.", regex=False)
                .stdout("Deze mail is normaal.", regex=False)
                .stdout('-> ""', regex=False)
                .stdout("Deze mail heeft geen subject.", regex=False))


@check50.check()
def afgebroken():
    """afgebroken werkt precies zoals de voorbeelden in de opdracht"""
    check50.exists("afgebroken.c")

    main = r"""
int main(void)
{
    string tekst = "Nederlanders worden steeds ouder, vooral door- dat ze na hun 65ste ...";
    printf("Origineel: %s\n", tekst);
    afgebroken(tekst);

    tekst = "Over de identiteit van de schutter zegt de po- litie: 'Als het de ...";
    printf("Origineel: %s\n", tekst);
    afgebroken(tekst);

    tekst = "Een 36-jarige Geldropse heeft deze week een in- breker in haar ...";
    printf("Origineel: %s\n", tekst);
    afgebroken(tekst);
}
"""
    with helpers.replace_main("afgebroken.c", main):
        with helpers.logged_check_factory("afgebroken") as run_check:
            (run_check()
                .stdout("Origineel: Nederlanders worden steeds ouder, vooral door- dat ze na hun 65ste ...", regex=False)
                .stdout("Nederlanders worden steeds ouder, vooral doordat ze na hun 65ste langer in ...", regex=False)
                .stdout("Origineel: Over de identiteit van de schutter zegt de po- litie: 'Als het de ...", regex=False)
                .stdout("Over de identiteit van de schutter zegt de politie: 'Als het de man is die ...", regex=False)
                .stdout("Origineel: Een 36-jarige Geldropse heeft deze week een in- breker in haar ...", regex=False)
                .stdout("Een 36-jarige Geldropse heeft deze week een inbreker in haar schuurtje net ...", regex=False))
                        

@check50.check()
def leestijd():
    """leestijd werkt precies zoals de voorbeelden in de opdracht"""
    check50.exists("leestijd.c")

    main = r"""
int main(void)
{
    // zet de leestijden klaar in een array
    int tijden1[] = { 35, 50, 10, 15 };
    // roep de functie aan, met de array en ook de lengte van de array
    printf("{ 35, 50, 10, 15 }\n");
    leestijd(tijden1, 4);

    // zet de leestijden klaar in een array
    int tijden2[] = { };
    // roep de functie aan, met de array en ook de lengte van de array
    printf("{ }\n");
    leestijd(tijden2, 0);
}
"""
    with helpers.replace_main("leestijd.c", main):
        with helpers.logged_check_factory("leestijd") as run_check:
            (run_check()
                .stdout("{ 35, 50, 10, 15 }", regex=False)
                .stdout("Je hebt ongeveer 92 pagina's gelezen.", regex=False)
                .stdout("{ }", regex=False)
                .stdout("Je hebt niet gelezen.", regex=False))
