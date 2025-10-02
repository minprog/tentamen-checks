import check50
import check50.internal

helpers = check50.internal.import_file(
    "helpers",
    check50.internal.check_dir / "../helpers/helpers.py"
)
helpers.set_stdout_limit(10000)
    

@check50.check()
def readability():
    """readability.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    printf("%.2f\n", readability_score("rubber duck"));
    printf("%.2f\n", readability_score("One rubber duck"));
    printf("%.2f\n", readability_score("Fee fi fo fum"));
    printf("%.2f\n", readability_score("This is cs50"));
    printf("%.2f\n", readability_score("THIS, IS, CS50!"));
    printf("%.2f\n", readability_score("And now for something Completely Different..."));
}
"""
    with helpers.replace_main("readability.c", main):
        with helpers.logged_check_factory("readability") as run_check:
            (run_check()
                .stdout('20.00\n', regex=False)
                .stdout('13.00\n', regex=False)
                .stdout('0.00\n', regex=False)
                .stdout('10.67\n', regex=False)
                .stdout('10.67\n', regex=False)
                .stdout('67.83\n', regex=False)
            )

@check50.check()
def uithangbord():
    """uithangbord.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    print_board("Margherita\nTutta\nla\nVita\n");
    print_board("mini\nklein\ngroter\n");
    print_board("Faculteit\nder\nNatuurwetenschappen\nWiskunde\nen\nInformatica\n");
}
"""
    with helpers.replace_main("uithangbord.c", main):
        with helpers.logged_check_factory("uithangbord") as run_check:
            (run_check()
                .stdout(r'^##########\n', str_output='##########\n')
                .stdout('Margherita\n', regex=False)
                .stdout('Tutta\n', regex=False)
                .stdout('la\n', regex=False)
                .stdout('Vita\n', regex=False)
                .stdout(r'^##########\n', str_output='##########\n')
                .stdout(r'^######\n', str_output='######\n')
                .stdout('mini\n', regex=False)
                .stdout('klein\n', regex=False)
                .stdout('groter\n', regex=False)
                .stdout(r'^######\n', str_output='######\n')
                .stdout(r'^###################\n', str_output='###################\n')
                .stdout('Faculteit\n', regex=False)
                .stdout('der\n', regex=False)
                .stdout('Natuurwetenschappen\n', regex=False)
                .stdout('Wiskunde\n', regex=False)
                .stdout('en\n', regex=False)
                .stdout('Informatica\n', regex=False)
                .stdout(r'^###################\n', str_output='###################\n')
            )

@check50.check()
def hoofdletterzoeker():
    """hoofdletterzoeker.c werkt zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    string tekst = "Hello World";
    printf("\"%s\" print:\n", tekst);
    print_woorden_met_hoofdletters(tekst);
    printf("\n");

    tekst = "Deze zin begint en eindigt met een Hoofdletter";
    printf("\"%s\" print:\n", tekst);
    print_woorden_met_hoofdletters(tekst);
    printf("\n");

    tekst = "geen hoofdletters in deze tekst";
    printf("\"%s\" print:\n", tekst);
    print_woorden_met_hoofdletters(tekst);
    printf("\n");

    tekst = "ieder Ander woord Begint met Een hoofdletter";
    printf("\"%s\" print:\n", tekst);
    print_woorden_met_hoofdletters(tekst);
    printf("\n");
}
"""
    with helpers.replace_main("hoofdletterzoeker.c", main):
        with helpers.logged_check_factory("hoofdletterzoeker") as run_check:
            (run_check()
                .stdout('"Hello World" print:\n', regex=False)
                .stdout('Hello World', regex=False)
                .stdout('Deze zin begint en eindigt met een Hoofdletter" print:\n', regex=False)
                .stdout('Deze Hoofdletter', regex=False)
                .stdout('geen hoofdletters in deze tekst" print:\n', regex=False)
                .stdout('\n', regex=False)
                .stdout('ieder Ander woord Begint met Een hoofdletter" print:\n', regex=False)
                .stdout('Ander Begint Een', regex=False)
            )

@check50.check()
def mirror():
    """mirror.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    print_mirror("lepel");
    print_mirror("Abba");
    print_mirror("nepper");
    print_mirror("paard");
    print_mirror("AbracadabrA");
    print_mirror("Programmeren");
}
"""
    with helpers.replace_main("mirror.c", main):
        with helpers.logged_check_factory("mirror") as run_check:
            (run_check()
                .stdout('-----', regex=False)
                .stdout('----', regex=False)
                .stdout('#----#', regex=False)
                .stdout('##-##', regex=False)
                .stdout('-##-#-#-##-', regex=False)
                .stdout('############', regex=False)
            )

@check50.check()
def recheck():
    """recheck.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    string submissions0[] = {"orakel.c", "rechthoeken.c", "coupons.c"};
    string timestamps0[] = {"10:13", "11:20", "12:05"};
    int n0 = 3;
    print_unchecked(submissions0, timestamps0, n0, 11);

    printf("------------------------\n");
    
    string submissions1[] = {"mario.c", "hello.c", "functions.c", "tideman.c", "tideman (1).c", "tideman (2).c"};
    string timestamps1[] = {"12:51", "13:47", "14:15", "15:01", "15:06", "15:11"};
    int n1 = 6;
    print_unchecked(submissions1, timestamps1, n1, 15);
    
    printf("------------------------\n");
    
    string submissions2[] = {"scrabble.c", "wachtwoord.c", "alfabet.c", "render.c", "rna.c"};
    string timestamps2[] = {"10:12", "10:16", "10:23", "10:43", "11:01"};
    int n2 = 5;
    print_unchecked(submissions2, timestamps2, n2, 10);
    
    printf("------------------------\n");
    
    string submissions3[] = {"tideman (27).c", "tideman (28).c", "calendar.c", "morse.c"};
    string timestamps3[] = {"03:43", "04:12", "09:27", "09:59"};
    int n3 = 4;
    print_unchecked(submissions3, timestamps3, n3, 9);
}
"""
    with helpers.replace_main("recheck.c", main):
        with helpers.logged_check_factory("recheck") as run_check:
            (run_check()
                .stdout('rechthoeken.c\n', regex=False)
                .stdout('------------------------\n', regex=False)
                .stdout('tideman.c\n', regex=False)
                .stdout('tideman (1).c\n', regex=False)
                .stdout('tideman (2).c\n', regex=False)
                .stdout('------------------------\n', regex=False)
                .stdout('scrabble.c\n', regex=False)
                .stdout('wachtwoord.c\n', regex=False)
                .stdout('alfabet.c\n', regex=False)
                .stdout('render.c\n', regex=False)
                .stdout('------------------------\n', regex=False)
                .stdout('calendar.c\n', regex=False)
                .stdout('morse.c\n', regex=False)   
            )
