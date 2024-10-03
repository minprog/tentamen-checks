import check50
import check50.c
import check50.internal

helpers = check50.internal.import_file(
    "helpers",
    check50.internal.check_dir / "../helpers/helpers.py"
)

@check50.check()
def woordlengte():
    """woordlengte werkt zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    string tekst = "hello world";
    int gemiddelde = bereken_gemiddelde_woordlengte(tekst);
    printf("gemiddelde woordlengte van \"%s\" is %d\n", tekst, gemiddelde);

    tekst = "nul een twee";
    gemiddelde = bereken_gemiddelde_woordlengte(tekst);
    printf("gemiddelde woordlengte van \"%s\" is %d\n", tekst, gemiddelde);
    
    tekst = "vier vijf zes";
    gemiddelde = bereken_gemiddelde_woordlengte(tekst);
    printf("gemiddelde woordlengte van \"%s\" is %d\n", tekst, gemiddelde);

    tekst = "the quick brown fox jumps over the lazy dog";
    gemiddelde = bereken_gemiddelde_woordlengte(tekst);
    printf("gemiddelde woordlengte van \"%s\" is %d\n", tekst, gemiddelde);

    tekst = "";
    gemiddelde = bereken_gemiddelde_woordlengte(tekst);
    printf("gemiddelde woordlengte van \"%s\" is %d\n", tekst, gemiddelde);
}
"""
    with helpers.replace_main("woordlengte.c", main):
        with helpers.logged_check_factory("woordlengte") as run_check:
            (run_check()
                .stdout('gemiddelde woordlengte van "hello world" is 5\n', regex=False)
                .stdout('gemiddelde woordlengte van "nul een twee" is 3\n', regex=False)
                .stdout('gemiddelde woordlengte van "vier vijf zes" is 4\n', regex=False)
                .stdout('gemiddelde woordlengte van "the quick brown fox jumps over the lazy dog" is 4\n', regex=False)
                .stdout('gemiddelde woordlengte van "" is 0\n', regex=False))


@check50.check()
def print_hoofdletters():
    """print_hoofdletters werkt precies zoals de voorbeelden in de opdracht"""
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

    tekst = "ieder Ander woord Begint met Een hoofdletter";
    printf("\"%s\" print:\n", tekst);
    print_woorden_met_hoofdletters(tekst);
    printf("\n");

    tekst = "geen hoofdletters in deze tekst";
    printf("\"%s\" print:\n", tekst);
    print_woorden_met_hoofdletters(tekst);
    printf("\n");
}
"""
    with helpers.replace_main("print_hoofdletters.c", main):
        with helpers.logged_check_factory("print_hoofdletters") as run_check:
            (run_check()
                .stdout('"Hello World" print:', regex=False)
                .stdout('Hello World', regex=False)
                .stdout('"Deze zin begint en eindigt met een Hoofdletter" print:', regex=False)
                .stdout('Deze Hoofdletter', regex=False)
                .stdout('"ieder Ander woord Begint met Een hoofdletter" print:', regex=False)
                .stdout('Ander Begint Een', regex=False)
                .stdout('"geen hoofdletters in deze tekst" print:', regex=False))


@check50.check()
def filter_tekens():
    """filter_tekens werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    char tekst1[] = "hello world";
    printf("filter op \"%s\" met de karakters \"eo\" geeft:\n", tekst1);
    filter_tekens(tekst1, "eo");
    printf("%s\n", tekst1);

    char tekst2[] = "haal even, alle lees-tekens weg!";
    printf("filter op \"%s\" met de karakters \",.-!\" geeft:\n", tekst2);
    filter_tekens(tekst2, ",.-!");
    printf("%s\n", tekst2);

    char tekst3[] = "of,alle,letters,dit,keer!";
    printf("filter op \"%s\" met de karakters \"abcdefghijklmnopqrstuvwxyz\" geeft:\n", tekst3);
    filter_tekens(tekst3, "abcdefghijklmnopqrstuvwxyz");
    printf("%s\n", tekst3);
}
"""
    with helpers.replace_main("filter_tekens.c", main):
        with helpers.logged_check_factory("filter_tekens") as run_check:
            (run_check()
                .stdout('filter op "hello world" met de karakters "eo" geeft:', regex=False)
                .stdout('h ll  w rld', regex=False)
                .stdout('filter op "haal even, alle lees-tekens weg!" met de karakters ",.-!" geeft:', regex=False)
                .stdout('haal even  alle lees tekens weg', regex=False)
                .stdout('filter op "of,alle,letters,dit,keer!" met de karakters "abcdefghijklmnopqrstuvwxyz" geeft:', regex=False)
                .stdout('  ,    ,       ,   ,    !', regex=False))


@check50.check()
def visite():
    """visite werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    print_visitekaart("Martijn", "docent", "555-555-800");
    print_visitekaart("Nina", "studentassistent", "333-555-977");
    print_visitekaart("Jan-Peter de derde", "jurist", "555-100-200");
}
"""
    with helpers.replace_main("visite.c", main):
        with helpers.logged_check_factory("visite") as run_check:
            (run_check()
                .stdout('-----------', regex=False)
                .stdout('  Martijn', regex=False)
                .stdout('  docent', regex=False)
                .stdout('555-555-800', regex=False)
                .stdout('-----------', regex=False)
                .stdout('----------------', regex=False)
                .stdout('      Nina', regex=False)
                .stdout('studentassistent', regex=False)
                .stdout('  333-555-977', regex=False)
                .stdout('----------------', regex=False)
                .stdout('------------------', regex=False)
                .stdout('Jan-Peter de derde', regex=False)
                .stdout('      jurist', regex=False)
                .stdout('   555-100-200', regex=False)
                .stdout('------------------', regex=False))


@check50.check()
def fitness():
    """fitness werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    float afstanden1[] = {1.5, 2, 3};
    float tijden1[] = {8, 12, 20};
    print_fitness_rapport(afstanden1, tijden1, 3);

    float afstanden2[] = {14, 12, 18, 19, 20};
    float tijden2[] = {112, 90, 144, 160, 200};
    print_fitness_rapport(afstanden2, tijden2, 5);

    float afstanden3[] = {6.5, 10, 15, 17.5};
    float tijden3[] = {60, 100, 150, 180};
    print_fitness_rapport(afstanden3, tijden3, 4);
}
"""
    with helpers.replace_main("fitness.c", main):
        with helpers.logged_check_factory("fitness") as run_check:
            (run_check()
                .stdout('De langste afstand is 3.00 kilometer', regex=False)
                .stdout('De langste tijd is 20.00 minuten', regex=False)
                .stdout('De hoogste snelheid is 11.25 km/u door 1.50 kilometer in 8.00 minuten te lopen', regex=False)
                .stdout('De langste afstand is 20.00 kilometer', regex=False)
                .stdout('De langste tijd is 200.00 minuten', regex=False)
                .stdout('De hoogste snelheid is 8.00 km/u door 12.00 kilometer in 90.00 minuten te lopen', regex=False)
                .stdout('De langste afstand is 17.50 kilometer', regex=False)
                .stdout('De langste tijd is 180.00 minuten', regex=False)
                .stdout('De hoogste snelheid is 6.50 km/u door 6.50 kilometer in 60.00 minuten te lopen', regex=False))