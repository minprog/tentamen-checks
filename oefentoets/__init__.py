import check50
import check50.c

helpers = check50.internal.import_file(
    "helpers",
    check50.internal.check_dir / "../helpers/helpers.py"
)

@check50.check()
def makelaar():
    """makelaar werkt precies zoals de voorbeelden in de opdracht"""
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


# @check50.check()
# def leestijd():
#     """leestijd werkt precies zoals de voorbeelden in de opdracht"""
#     with logged_check_factory("leestijd") as run_check:

#         # check example 1
#         (run_check()
#             .stdin("35")
#             .stdin("50")
#             .stdin("10")
#             .stdin("15")
#             .stdin("-1")
#             .stdout("[Jj]e hebt ongeveer 9[12][\n]* pagina", "Je hebt ongeveer 91/92 pagina's gelezen."))

#         # check example 2
#         (run_check()
#             .stdin("-1")
#             .stdout("[Jj]e hebt niet gelezen\.?"))


# @check50.check()
# def spam():
#     """spam werkt precies zoals de voorbeelden in de opdracht"""
#     with logged_check_factory("spam") as run_check:

#         test_string = "CaZhh M0n3y"
#         output = (run_check(test_string)
#             .stdout("20(?!\d)", str_output="20")
#             .stdout())

#         if "spam" not in output or "normaal" in output:
#             raise check50.Failure(f"{test_string} should be spam")

#         test_string = "Dit was zeker geen spam!"
#         output = (run_check(test_string)
#             .stdout("5(?!\d)", str_output="5")
#             .stdout())

#         if "spam" in output or "normaal" not in output:
#             raise check50.Failure(f"{test_string} should not be spam")

#         (run_check()
#             .stdout("(Usage: )?./spam text..."))


# @check50.check()
# def afgebroken():
#     """afgebroken werkt precies zoals de voorbeelden in de opdracht"""
#     with logged_check_factory("afgebroken") as run_check:

#         (run_check()
#             .stdin("Nederlanders worden steeds ouder, vooral door- dat ze na hun 65ste langer in leven blijven.")
#             .stdout("Nederlanders worden steeds ouder, vooral doordat ze na hun 65ste langer in leven blijven."))

#         (run_check()
#             .stdin("Over de identiteit van de schutter zegt de po- litie: 'Als het de man is die we denken dat het is, dan is het een bekende van de politie.'")
#             .stdout("Over de identiteit van de schutter zegt de politie: 'Als het de man is die we denken dat het is, dan is het een bekende van de politie.'"))

#         (run_check()
#             .stdin("")
#             .stdin("Een 36-jarige Geldropse heeft deze week een in- breker in haar schuurtje net zo lang achtervolgd tot de politie arriveerde.")
#             .stdout("Een 36-jarige Geldropse heeft deze week een inbreker in haar schuurtje net zo lang achtervolgd tot de politie arriveerde."))

