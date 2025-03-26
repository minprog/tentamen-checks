import check50
import check50.c
import check50.internal

helpers = check50.internal.import_file(
    "helpers",
    check50.internal.check_dir / "../helpers/helpers.py"
)
helpers.set_stdout_limit(10000)
    

@check50.check()
def woord_piramide():
    """woord_piramide.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    print_piramide("a", "abc", "abcde");
    print_piramide("ev", "oneve", "!even!");
    print_piramide("min", "prog", "tentamen");
}
"""
    with helpers.replace_main("woord_piramide.c", main):
        with helpers.logged_check_factory("woord_piramide") as run_check:
            (run_check()
                .stdout('#########', regex=False)
                .stdout('#   a   #', regex=False)
                .stdout('#  abc  #', regex=False)
                .stdout('# abcde #', regex=False)
                .stdout('#########', regex=False)
                .stdout('##########', regex=False)
                .stdout('#   ev   #', regex=False)
                .stdout('# oneve  #', regex=False)
                .stdout('# !even! #', regex=False)
                .stdout('##########', regex=False)
                .stdout('############', regex=False)
                .stdout('#   min    #', regex=False)
                .stdout('#   prog   #', regex=False)
                .stdout('# tentamen #', regex=False)
                .stdout('############', regex=False)
            )

@check50.check()
def grouped():
    """grouped.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    int numbers1[] = {5, 5, 5, 7, 7, 8};
    print_groups(numbers1, 6);
    printf("\n");
    
    int numbers2[] = {1, 2, 3, 4, 5};
    print_groups(numbers2, 5);
    printf("\n");
    
    int numbers3[] = {2, 2, 0, 0, 3, 3, 3, 3, 0};
    print_groups(numbers3, 9);
    printf("\n");
}
"""
    with helpers.replace_main("grouped.c", main):
        with helpers.logged_check_factory("grouped") as run_check:
            (run_check()
                .stdout('3 times 5', regex=False)
                .stdout('2 times 7', regex=False)
                .stdout('1 times 8', regex=False)
                .stdout('1 times 1', regex=False)
                .stdout('1 times 2', regex=False)
                .stdout('1 times 3', regex=False)
                .stdout('1 times 4', regex=False)
                .stdout('1 times 5', regex=False)
                .stdout('2 times 2', regex=False)
                .stdout('2 times 0', regex=False)
                .stdout('4 times 3', regex=False)
                .stdout('1 times 0', regex=False)
            )

@check50.check()
def hordes():
    """hordes.c werkt zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    int afstanden1[] = {0, 30, 60, 90, 120, 150};
    int n1 = 6;
    int baanlengte1 = 400;
    printf("%i\n", tel_hordes(afstanden1, n1, baanlengte1));
    
    int afstanden2[] = {0, 40, 75, 5, 35, 70, 100};
    int n2 = 7;
    int baanlengte2 = 100;
    printf("%i\n", tel_hordes(afstanden2, n2, baanlengte2));
    
    int afstanden3[] = {0, 25, 50, 75, 25, 50, 75, 25, 50};
    int n3 = 9;
    int baanlengte3 = 75;
    printf("%i\n", tel_hordes(afstanden3, n3, baanlengte3));
    
    int afstanden4[] = {0, 20, 50, 80, 100, 20, 40, 60};
    int n4 = 8;
    int baanlengte4 = 100;
    printf("%i\n", tel_hordes(afstanden4, n4, baanlengte4));
}
"""
    with helpers.replace_main("hordes.c", main):
        with helpers.logged_check_factory("hordes") as run_check:
            (run_check()
                .stdout('5', regex=False)
                .stdout('6', regex=False)
                .stdout('5', regex=False)
                .stdout('5', regex=False)
            )

@check50.check()
def telefoon():
    """telefoon.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    print_nummer("0645612456");
    print_nummer("+31612312334");
    print_nummer("+31202223331");
    print_nummer("0201234567");
    print_nummer("020123456");
    print_nummer("+312012345678");
    print_nummer("+120123456789");
    print_nummer("1201234567");
    print_nummer("+2201234567");
}
"""
    with helpers.replace_main("telefoon.c", main):
        with helpers.logged_check_factory("telefoon") as run_check:
            (run_check()
                .stdout('0645612456', regex=False)
                .stdout('0612312334', regex=False)
                .stdout('0202223331', regex=False)
                .stdout('0201234567', regex=False)
                .stdout('Verkeerde lengte', regex=False)
                .stdout('Verkeerde lengte', regex=False)
                .stdout('Verkeerd begin', regex=False)
                .stdout('Verkeerd begin', regex=False)
                .stdout('Verkeerd begin', regex=False)
            )

@check50.check()
def contains():
    """contains.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    printf("%i\n", contains("hello", "el"));
    printf("%i\n", contains("foo", "bar"));
    printf("%i\n", contains("hello, world", ","));
    printf("%i\n", contains("minor programmeren tentamen", "programmeren"));
    printf("%i\n", contains("minor programmeren tentamen", "programeren"));
}
"""
    with helpers.replace_main("contains.c", main):
        with helpers.logged_check_factory("contains") as run_check:
            (run_check()
                .stdout('1', regex=False)
                .stdout('0', regex=False)
                .stdout('1', regex=False)
                .stdout('1', regex=False)
                .stdout('0', regex=False)
            )
