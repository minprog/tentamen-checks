import check50
import check50.internal

helpers = check50.internal.import_file(
    "helpers",
    check50.internal.check_dir / "../helpers/helpers.py"
)
helpers.set_stdout_limit(10000)


@check50.check()
def middelste_woord():
    """middelste_woord werkt zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    printf("Het middelste woord van \"hello world hoe gaat het\" is:\n");
    print_middelste_woord("hello world hoe gaat het");
    printf("Het middelste woord van \"dit is een even aantal woorden\" is:\n");
    print_middelste_woord("dit is een even aantal woorden");
    printf("Het middelste woord van \"\" is:\n");
    print_middelste_woord("");
    printf("Het middelste woord van \"foo\" is:\n");
    print_middelste_woord("foo");
}
"""
    with helpers.replace_main("middelste_woord.c", main):
        with helpers.logged_check_factory("middelste_woord") as run_check:
            (run_check()
                .stdout('Het middelste woord van "hello world hoe gaat het" is:', regex=False)
                .stdout('hoe', regex=False)
                .stdout('Het middelste woord van "dit is een even aantal woorden" is:', regex=False)
                .stdout('een', regex=False)
                .stdout('Het middelste woord van "" is:\n', regex=False)
                .stdout('\n', regex=False)
                .stdout('Het middelste woord van "foo" is:', regex=False)
                .stdout('foo', regex=False))


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
    with helpers.replace_main("filter.c", main):
        with helpers.logged_check_factory("filter") as run_check:
            (run_check()
                .stdout('filter op "hello world" met de karakters "eo" geeft:', regex=False)
                .stdout('h ll  w rld', regex=False)
                .stdout('filter op "haal even, alle lees-tekens weg!" met de karakters ",.-!" geeft:', regex=False)
                .stdout('haal even  alle lees tekens weg', regex=False)
                .stdout('filter op "of,alle,letters,dit,keer!" met de karakters "abcdefghijklmnopqrstuvwxyz" geeft:', regex=False)
                .stdout('  ,    ,       ,   ,    !', regex=False))


@check50.check()
def hittegolf():
    """hittegolf werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    int temperaturen1[] = {25, 30, 30, 30, 25};
    printf("De langste hittegolf was %d dagen\n", vind_langste_hittegolf(temperaturen1, 5));

    int temperaturen2[] = {33, 35, 30, 25, 26, 20, 21, 30, 31, 30, 29, 28, 26, 23, 27, 31, 30, 27, 27, 28, 26};
    printf("De langste hittegolf was %d dagen\n", vind_langste_hittegolf(temperaturen2, 21));

    int temperaturen3[] = {19, 25, 26, 24, 17, 23, 20};
    printf("De langste hittegolf was %d dagen\n", vind_langste_hittegolf(temperaturen3, 7));

    int temperaturen4[] = {20, 26, 31, 29, 30, 25, 23, 31, 28, 26, 32, 31, 29, 32, 30, 28, 24};
    printf("De langste hittegolf was %d dagen\n", vind_langste_hittegolf(temperaturen4, 17));

    int temperaturen5[] = {30, 33, 32, 30, 20, 19, 25};
    printf("De langste hittegolf was %d dagen\n", vind_langste_hittegolf(temperaturen5, 7));
}
"""
    with helpers.replace_main("hittegolf.c", main):
        with helpers.logged_check_factory("hittegolf") as run_check:
            (run_check()
                .stdout('De langste hittegolf was 5 dagen', regex=False)
                .stdout('De langste hittegolf was 6 dagen', regex=False)
                .stdout('De langste hittegolf was 0 dagen', regex=False)
                .stdout('De langste hittegolf was 9 dagen', regex=False)
                .stdout('De langste hittegolf was 0 dagen', regex=False))


@check50.check()
def kano():
    """kano werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    printf("Eerste snelheidsmetingen: {3, 4, 5, 0, 2, 2, 2, 2, 2, 2}\n");
    float snelheden1[] = {3, 4, 5, 0, 2, 2, 2, 2, 2, 2};
    print_gemiddeldes(snelheden1, 10);

    printf("Tweede snelheidsmetingen: {2, 2, 3, 3, 0, 4, 5, 0, 3}\n");
    float snelheden2[] = {2, 2, 3, 3, 0, 4, 5, 0, 3};
    print_gemiddeldes(snelheden2, 9);

    printf("Derde snelheidsmetingen: {5.25}\n");
    float snelheden3[] = {5.25};
    print_gemiddeldes(snelheden3, 1);
}
"""
    with helpers.replace_main("kano.c", main):
        with helpers.logged_check_factory("kano") as run_check:
            (run_check()
                .stdout('Eerste snelheidsmetingen: {3, 4, 5, 0, 2, 2, 2, 2, 2, 2}', regex=False)
                .stdout('anotrip 1: 4.00 km/u', regex=False)
                .stdout('anotrip 2: 2.00 km/u', regex=False)
                .stdout('Tweede snelheidsmetingen: {2, 2, 3, 3, 0, 4, 5, 0, 3}', regex=False)
                .stdout('anotrip 1: 2.50 km/u', regex=False)
                .stdout('anotrip 2: 4.50 km/u', regex=False)
                .stdout('anotrip 3: 3.00 km/u', regex=False)
                .stdout('Derde snelheidsmetingen: {5.25}', regex=False)
                .stdout('anotrip 1: 5.25 km/u', regex=False))
