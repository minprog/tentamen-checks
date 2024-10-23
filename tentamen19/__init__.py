import check50
import check50.c
import check50.internal

helpers = check50.internal.import_file(
    "helpers",
    check50.internal.check_dir / "../helpers/helpers.py"
)

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
def bevat_tenminste():
    """bevat_tenminste werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    printf("De tekst \"een twee drie\" bevat tenminste 6 klinkers:\n");
    printf("%d\n", bevat_tenminste("een twee drie", "aeoiu", 6));
    
    printf("De tekst \"hello, world!\" bevat tenminste 4 tekens van \",!\":\n");
    printf("%d\n", bevat_tenminste("hello, world!", ",!", 4));

    printf("De tekst \"Deze Tekst Bevat Vijf Hoofdletters\" bevat tenminste 5 van \"ABCDEFGHIJKLMNOPQRSTUVWXYZ\":\n");
    printf("%d\n", bevat_tenminste("Deze Tekst Bevat Vijf Hoofdletters", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5));
    
    printf("De tekst \"\" bevat tenminste 1 teken van \"abcdefghijklmnopqrstuvwxyz\":\n");
    printf("%d\n", bevat_tenminste("", "abcdefghijklmnopqrstuvwxyz", 1));
}
"""
    with helpers.replace_main("bevat_tenminste.c", main):
        with helpers.logged_check_factory("bevat_tenminste") as run_check:
            (run_check()
                .stdout('De tekst "een twee drie" bevat tenminste 6 klinkers:', regex=False)
                .stdout('1', regex=False)
                .stdout('De tekst "hello, world!" bevat tenminste 4 tekens van ",!":', regex=False)
                .stdout('0', regex=False)
                .stdout('De tekst "Deze Tekst Bevat Vijf Hoofdletters" bevat tenminste 5 van "ABCDEFGHIJKLMNOPQRSTUVWXYZ":', regex=False)
                .stdout('1', regex=False)
                .stdout('De tekst "" bevat tenminste 1 teken van "abcdefghijklmnopqrstuvwxyz":', regex=False)
                .stdout('0', regex=False))


@check50.check()
def uithangbord():
    """uithangbord werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    print_uithangbord("foo", "bar");
    print_uithangbord("langer", "kort");
    print_uithangbord("fee", "elders");
    print_uithangbord("", "");
}
"""
    with helpers.replace_main("uithangbord.c", main):
        with helpers.logged_check_factory("uithangbord") as run_check:
            (run_check()
                .stdout('#######', regex=False)
                .stdout('#     #', regex=False)
                .stdout('# f b #', regex=False)
                .stdout('# o a #', regex=False)
                .stdout('# o r #', regex=False)
                .stdout('#     #', regex=False)
                .stdout('#######', regex=False)
                .stdout('#######', regex=False)
                .stdout('#     #', regex=False)
                .stdout('# l k #', regex=False)
                .stdout('# a o #', regex=False)
                .stdout('# n r #', regex=False)
                .stdout('# g t #', regex=False)
                .stdout('# e   #', regex=False)
                .stdout('# r   #', regex=False)
                .stdout('#     #', regex=False)
                .stdout('#######', regex=False)
                .stdout('#######', regex=False)
                .stdout('#     #', regex=False)
                .stdout('# e f #', regex=False)
                .stdout('# l e #', regex=False)
                .stdout('# d e #', regex=False)
                .stdout('# e   #', regex=False)
                .stdout('# r   #', regex=False)
                .stdout('# s   #', regex=False)
                .stdout('#     #', regex=False)
                .stdout('#######', regex=False)
                .stdout('#######', regex=False)
                .stdout('#     #', regex=False)
                .stdout('#     #', regex=False)
                .stdout('#######', regex=False))


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
