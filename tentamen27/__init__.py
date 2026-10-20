import re

import check50
import check50.internal

helpers = check50.internal.import_file(
    "helpers",
    check50.internal.check_dir / "../helpers/helpers.py"
)
helpers.set_stdout_limit(10000)


def regel(tekst):
    """
    Regex die precies deze regel matcht. Lege regels ertussen worden
    overgeslagen, zodat een printf("\\n") tussen twee aanroepen niet meetelt.
    Extra spaties of tekens op de regel zelf tellen wel mee.
    """
    return r"^[\r\n]*" + re.escape(tekst) + r"\r?\n"


@check50.check()
def achtbaan():
    """achtbaan.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    int hoogtes1[] = {1, 3, 2, 5, 4};
    print_achtbaan(hoogtes1, 5);

    int hoogtes2[] = {1, 2, 2, 1};
    print_achtbaan(hoogtes2, 4);

    int hoogtes3[] = {3, 1, 1, 4};
    print_achtbaan(hoogtes3, 4);

    int hoogtes4[] = {1, 2, 2, 3, 1};
    print_achtbaan(hoogtes4, 5);

    int hoogtes5[] = {3, 1, 4, 1, 5, 9, 2, 6};
    print_achtbaan(hoogtes5, 8);

    int hoogtes6[] = {2, 2, 1};
    print_achtbaan(hoogtes6, 3);

    int hoogtes7[] = {5, 5, 5};
    print_achtbaan(hoogtes7, 3);

    int hoogtes8[] = {7};
    print_achtbaan(hoogtes8, 1);
}
"""
    with helpers.replace_main("achtbaan.c", main):
        with helpers.logged_check_factory("achtbaan") as run_check:
            (run_check()
                .stdout(regel('Pieken: 2'), str_output='Pieken: 2')
                .stdout(regel('Dalen: 1'), str_output='Dalen: 1')
                .stdout(regel('Pieken: 1'), str_output='Pieken: 1')
                .stdout(regel('Dalen: 0'), str_output='Dalen: 0')
                .stdout(regel('Pieken: 0'), str_output='Pieken: 0')
                .stdout(regel('Dalen: 1'), str_output='Dalen: 1')
                .stdout(regel('Pieken: 1'), str_output='Pieken: 1')
                .stdout(regel('Dalen: 0'), str_output='Dalen: 0')
                .stdout(regel('Pieken: 2'), str_output='Pieken: 2')
                .stdout(regel('Dalen: 3'), str_output='Dalen: 3')
                .stdout(regel('Pieken: 0'), str_output='Pieken: 0')
                .stdout(regel('Dalen: 0'), str_output='Dalen: 0')
                .stdout(regel('Pieken: 0'), str_output='Pieken: 0')
                .stdout(regel('Dalen: 0'), str_output='Dalen: 0')
                .stdout(regel('Pieken: 0'), str_output='Pieken: 0')
                .stdout(regel('Dalen: 0'), str_output='Dalen: 0')
            )


@check50.check()
def letterteller():
    """lengtes.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    print_lengtes("programmeren,is,leuk");
    print_lengtes("Zomer,in,de,stad");
    print_lengtes("xyz");
    print_lengtes("a,,b");
    print_lengtes(",kaas,");
    print_lengtes("");
}
"""
    with helpers.replace_main("lengtes.c", main):
        with helpers.logged_check_factory("lengtes") as run_check:
            (run_check()
                .stdout(regel('programmeren: 12'), str_output='programmeren: 12')
                .stdout(regel('is: 2'), str_output='is: 2')
                .stdout(regel('leuk: 4'), str_output='leuk: 4')
                .stdout(regel('Zomer: 5'), str_output='Zomer: 5')
                .stdout(regel('in: 2'), str_output='in: 2')
                .stdout(regel('de: 2'), str_output='de: 2')
                .stdout(regel('stad: 4'), str_output='stad: 4')
                .stdout(regel('xyz: 3'), str_output='xyz: 3')
                .stdout(regel('a: 1'), str_output='a: 1')
                .stdout(regel('(leeg): 0'), str_output='(leeg): 0')
                .stdout(regel('b: 1'), str_output='b: 1')
                .stdout(regel('(leeg): 0'), str_output='(leeg): 0')
                .stdout(regel('kaas: 4'), str_output='kaas: 4')
                .stdout(regel('(leeg): 0'), str_output='(leeg): 0')
                .stdout(regel('Geen woorden'), str_output='Geen woorden')
            )


@check50.check()
def comprimeren():
    """comprimeren.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    print_gecomprimeerd("aaabbc");
    print_gecomprimeerd("abc");
    print_gecomprimeerd("aaaaaaaaaaaa");
    print_gecomprimeerd("Aa");
    print_gecomprimeerd("mississippi");
    print_gecomprimeerd("");
}
"""
    with helpers.replace_main("comprimeren.c", main):
        with helpers.logged_check_factory("comprimeren") as run_check:
            (run_check()
                .stdout(regel('3a2bc'), str_output='3a2bc')
                .stdout(regel('abc'), str_output='abc')
                .stdout(regel('12a'), str_output='12a')
                .stdout(regel('Aa'), str_output='Aa')
                .stdout(regel('mi2si2si2pi'), str_output='mi2si2si2pi')
                .stdout(regel('Lege tekst'), str_output='Lege tekst')
            )

@check50.check()
def hashtag():
    """hashtag.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    print_hashtag("#tentamen");
    print_hashtag("#Prog1");
    print_hashtag("#CS50");
    print_hashtag("#MinorProgrammeren2026");
    print_hashtag("#");
    print_hashtag("tentamen");
    print_hashtag("#1337");
    print_hashtag("#twee woorden");
    print_hashtag("#te-veel-streepjes");
    print_hashtag("#dubbel#op");
}
"""
    with helpers.replace_main("hashtag.c", main):
        with helpers.logged_check_factory("hashtag") as run_check:
            (run_check()
                .stdout(regel('#tentamen'), str_output='#tentamen')
                .stdout(regel('#prog1'), str_output='#prog1')
                .stdout(regel('#cs50'), str_output='#cs50')
                .stdout(regel('#minorprogrammeren2026'), str_output='#minorprogrammeren2026')
                .stdout(regel('Geen hashtag'), str_output='Geen hashtag')
                .stdout(regel('Geen hashtag'), str_output='Geen hashtag')
                .stdout(regel('Geen hashtag'), str_output='Geen hashtag')
                .stdout(regel('Geen hashtag'), str_output='Geen hashtag')
                .stdout(regel('Geen hashtag'), str_output='Geen hashtag')
                .stdout(regel('Geen hashtag'), str_output='Geen hashtag')
            )


@check50.check()
def hashtag_geldig():
    """is_geldige_hashtag geeft true of false terug zoals in de opdracht"""
    main = r"""
int main(void)
{
    printf("%i\n", is_geldige_hashtag("#tentamen"));
    printf("%i\n", is_geldige_hashtag("#Prog1"));
    printf("%i\n", is_geldige_hashtag("#CS50"));
    printf("%i\n", is_geldige_hashtag("#MinorProgrammeren2026"));
    printf("%i\n", is_geldige_hashtag("#"));
    printf("%i\n", is_geldige_hashtag("tentamen"));
    printf("%i\n", is_geldige_hashtag("#1337"));
    printf("%i\n", is_geldige_hashtag("#twee woorden"));
    printf("%i\n", is_geldige_hashtag("#te-veel-streepjes"));
    printf("%i\n", is_geldige_hashtag("#dubbel#op"));
}
"""
    with helpers.replace_main("hashtag.c", main):
        with helpers.logged_check_factory("hashtag") as run_check:
            (run_check()
                .stdout(regel('1'), str_output='1')
                .stdout(regel('1'), str_output='1')
                .stdout(regel('1'), str_output='1')
                .stdout(regel('1'), str_output='1')
                .stdout(regel('0'), str_output='0')
                .stdout(regel('0'), str_output='0')
                .stdout(regel('0'), str_output='0')
                .stdout(regel('0'), str_output='0')
                .stdout(regel('0'), str_output='0')
                .stdout(regel('0'), str_output='0')
            )


@check50.check()
def inpakken():
    """inpakken.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    string woorden1[] = {"de", "kat", "krabt", "de", "krullen", "van", "de", "trap"};
    print_regels(woorden1, 8, 10);
    printf("\n");

    print_regels(woorden1, 8, 20);
    printf("\n");

    string woorden2[] = {"onvoorstelbaar", "kort"};
    print_regels(woorden2, 2, 5);
    printf("\n");

    print_regels(woorden2, 0, 10);
}
"""
    with helpers.replace_main("inpakken.c", main):
        with helpers.logged_check_factory("inpakken") as run_check:
            (run_check()
                .stdout(regel('de kat'), str_output='de kat')
                .stdout(regel('krabt de'), str_output='krabt de')
                .stdout(regel('krullen'), str_output='krullen')
                .stdout(regel('van de'), str_output='van de')
                .stdout(regel('trap'), str_output='trap')
                .stdout(regel('de kat krabt de'), str_output='de kat krabt de')
                .stdout(regel('krullen van de trap'), str_output='krullen van de trap')
                .stdout(regel('onvoorstelbaar'), str_output='onvoorstelbaar')
                .stdout(regel('kort'), str_output='kort')
                .stdout(regel('Niets te printen'), str_output='Niets te printen')
            )


