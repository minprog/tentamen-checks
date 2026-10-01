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
def trap():
    """trap.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    string woorden1[] = {"een", "twee", "drie"};
    print_trap(woorden1, 3);
    printf("\n");

    string woorden2[] = {"a", "bb", "ccc", "dddd"};
    print_trap(woorden2, 4);
    printf("\n");

    string woorden3[] = {"minor", "programmeren"};
    print_trap(woorden3, 2);
    printf("\n");

    print_trap(woorden1, 0);
}
"""
    with helpers.replace_main("trap.c", main):
        with helpers.logged_check_factory("trap") as run_check:
            (run_check()
                .stdout(regel('[een]'), str_output='[een]')
                .stdout(regel('     [twee]'), str_output='     [twee]')
                .stdout(regel('           [drie]'), str_output='           [drie]')
                .stdout(regel('[a]'), str_output='[a]')
                .stdout(regel('   [bb]'), str_output='   [bb]')
                .stdout(regel('       [ccc]'), str_output='       [ccc]')
                .stdout(regel('            [dddd]'), str_output='            [dddd]')
                .stdout(regel('[minor]'), str_output='[minor]')
                .stdout(regel('       [programmeren]'), str_output='       [programmeren]')
                .stdout(regel('Lege trap'), str_output='Lege trap')
            )


@check50.check()
def lift():
    """lift.c werkt zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    int etages1[] = {0, 3, 1, 5};
    print_lift(etages1, 4);

    int etages2[] = {0, 1, 2, 3};
    print_lift(etages2, 4);

    int etages3[] = {5, 5, 5};
    print_lift(etages3, 3);

    int etages4[] = {2, 0, 2, 0, 2, 0};
    print_lift(etages4, 6);

    int etages5[] = {0, 4, 4, 2, 2, 7};
    print_lift(etages5, 6);

    int etages6[] = {3};
    print_lift(etages6, 1);

    // stilstand tussen twee ritten omlaag is geen richtingswisseling
    int etages7[] = {5, 3, 3, 1};
    print_lift(etages7, 4);
}
"""
    with helpers.replace_main("lift.c", main):
        with helpers.logged_check_factory("lift") as run_check:
            (run_check()
                .stdout(regel('Afgelegd: 9 etages'), str_output='Afgelegd: 9 etages')
                .stdout(regel('Wisselingen: 2'), str_output='Wisselingen: 2')
                .stdout(regel('Afgelegd: 3 etages'), str_output='Afgelegd: 3 etages')
                .stdout(regel('Wisselingen: 0'), str_output='Wisselingen: 0')
                .stdout(regel('Afgelegd: 0 etages'), str_output='Afgelegd: 0 etages')
                .stdout(regel('Wisselingen: 0'), str_output='Wisselingen: 0')
                .stdout(regel('Afgelegd: 10 etages'), str_output='Afgelegd: 10 etages')
                .stdout(regel('Wisselingen: 4'), str_output='Wisselingen: 4')
                .stdout(regel('Afgelegd: 11 etages'), str_output='Afgelegd: 11 etages')
                .stdout(regel('Wisselingen: 2'), str_output='Wisselingen: 2')
                .stdout(regel('Afgelegd: 0 etages'), str_output='Afgelegd: 0 etages')
                .stdout(regel('Wisselingen: 0'), str_output='Wisselingen: 0')
                .stdout(regel('Afgelegd: 4 etages'), str_output='Afgelegd: 4 etages')
                .stdout(regel('Wisselingen: 0'), str_output='Wisselingen: 0')
            )


@check50.check()
def jaartal():
    """jaartal.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    print_jaartal("In 1969 landde de eerste mens op de maan");
    print_jaartal("De brug opende in 1932, en werd verbreed in 1968");
    print_jaartal("2026");
    print_jaartal("1e keer in 1985!");
    print_jaartal("Het jaar 12345 bestaat niet");
    print_jaartal("Bel 0612345678 voor meer informatie");
    print_jaartal("Kamer 123 op verdieping 4");
}
"""
    with helpers.replace_main("jaartal.c", main):
        with helpers.logged_check_factory("jaartal") as run_check:
            (run_check()
                .stdout(regel('1969'), str_output='1969')
                .stdout(regel('1932'), str_output='1932')
                .stdout(regel('2026'), str_output='2026')
                .stdout(regel('1985'), str_output='1985')
                .stdout(regel('Geen jaartal gevonden'), str_output='Geen jaartal gevonden')
                .stdout(regel('Geen jaartal gevonden'), str_output='Geen jaartal gevonden')
                .stdout(regel('Geen jaartal gevonden'), str_output='Geen jaartal gevonden')
            )


@check50.check()
def koploper():
    """koploper.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    int getallen1[] = {5, 2, 5, 3, 5, 2};
    print_koploper(getallen1, 6);

    int getallen2[] = {5, 2, 5, 3, 2, 2};
    print_koploper(getallen2, 6);

    int getallen3[] = {7, 3, 9, 3};
    print_koploper(getallen3, 4);

    int getallen4[] = {4, 4, 4, 4};
    print_koploper(getallen4, 4);

    int getallen5[] = {0, 1, 0, 1, 0, 1};
    print_koploper(getallen5, 6);

    int getallen6[] = {1, 2, 3};
    print_koploper(getallen6, 3);

    print_koploper(getallen6, 0);
}
"""
    with helpers.replace_main("koploper.c", main):
        with helpers.logged_check_factory("koploper") as run_check:
            (run_check()
                .stdout(regel('5 komt 3 keer voor'), str_output='5 komt 3 keer voor')
                .stdout(regel('2 komt 3 keer voor'), str_output='2 komt 3 keer voor')
                .stdout(regel('3 komt 2 keer voor'), str_output='3 komt 2 keer voor')
                .stdout(regel('4 komt 4 keer voor'), str_output='4 komt 4 keer voor')
                .stdout(regel('0 komt 3 keer voor'), str_output='0 komt 3 keer voor')
                .stdout(regel('Geen herhalingen'), str_output='Geen herhalingen')
                .stdout(regel('Geen herhalingen'), str_output='Geen herhalingen')
            )

@check50.check()
def kenteken_geldig():
    """is_geldig_kenteken geeft true of false terug zoals in de opdracht"""
    main = r"""
int main(void)
{
    printf("%i\n", is_geldig_kenteken("GX-01-BC"));
    printf("%i\n", is_geldig_kenteken("12-AB-34"));
    printf("%i\n", is_geldig_kenteken("RT-VD-88"));
    printf("%i\n", is_geldig_kenteken("40-72-KP"));
    printf("%i\n", is_geldig_kenteken("AB-CD-EF"));
    printf("%i\n", is_geldig_kenteken("12-34-56"));
    printf("%i\n", is_geldig_kenteken("gx-01-bc"));
    printf("%i\n", is_geldig_kenteken("GX-0B-CD"));
    printf("%i\n", is_geldig_kenteken("GX-01-B"));
    printf("%i\n", is_geldig_kenteken("GX0-1-BC"));
}
"""
    with helpers.replace_main("kenteken.c", main):
        with helpers.logged_check_factory("kenteken") as run_check:
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
def kenteken():
    """kenteken.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    print_kenteken("GX-01-BC");
    print_kenteken("12-AB-34");
    print_kenteken("RT-VD-88");
    print_kenteken("40-72-KP");
    print_kenteken("AB-CD-EF");
    print_kenteken("12-34-56");
    print_kenteken("gx-01-bc");
    print_kenteken("GX-0B-CD");
    print_kenteken("GX-01-B");
    print_kenteken("GX0-1-BC");
}
"""
    with helpers.replace_main("kenteken.c", main):
        with helpers.logged_check_factory("kenteken") as run_check:
            (run_check()
                .stdout(regel('XX-99-XX'), str_output='XX-99-XX')
                .stdout(regel('99-XX-99'), str_output='99-XX-99')
                .stdout(regel('XX-XX-99'), str_output='XX-XX-99')
                .stdout(regel('99-99-XX'), str_output='99-99-XX')
                .stdout(regel('Ongeldig kenteken'), str_output='Ongeldig kenteken')
                .stdout(regel('Ongeldig kenteken'), str_output='Ongeldig kenteken')
                .stdout(regel('Ongeldig kenteken'), str_output='Ongeldig kenteken')
                .stdout(regel('Ongeldig kenteken'), str_output='Ongeldig kenteken')
                .stdout(regel('Ongeldig kenteken'), str_output='Ongeldig kenteken')
                .stdout(regel('Ongeldig kenteken'), str_output='Ongeldig kenteken')
            )

