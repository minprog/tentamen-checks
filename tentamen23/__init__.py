import check50
import check50.internal

helpers = check50.internal.import_file(
    "helpers",
    check50.internal.check_dir / "../helpers/helpers.py"
)
helpers.set_stdout_limit(10000)


@check50.check()
def toegestane_lengte():
    """toegestane_lengte.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    print_toegestane_lengte("Hello bye", 5);
    printf("\n");
    print_toegestane_lengte("Fee fi fo fum", 2);
    printf("\n");
    print_toegestane_lengte("nog een keer dan", 3);
    printf("\n");
}
"""
    with helpers.replace_main("toegestane_lengte.c", main):
        with helpers.logged_check_factory("toegestane_lengte") as run_check:
            (run_check()
                .stdout(r'^Hello\s*\n', str_output='Hello\n')
                .stdout(r'^fi fo\s*\n', str_output='fi fo\n')
                .stdout(r'^nog een dan\s*\n', str_output='nog een dan\n')
            )

@check50.check()
def rechthoek():
    """rechthoek.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    print_rechthoek("bye", "hello");
    print_rechthoek("minor", "programmeren");
    print_rechthoek("langste", "kort");
}
"""
    with helpers.replace_main("rechthoek.c", main):
        with helpers.logged_check_factory("rechthoek") as run_check:
            (run_check()
                .stdout('^#hello#\n', str_output='#hello#\n')
                .stdout('^b     b\n', str_output='b     b\n')
                .stdout('^y     y\n', str_output='y     y\n')
                .stdout('^e     e\n', str_output='e     e\n')
                .stdout('^#hello#\n', str_output='#hello#\n')
                .stdout('^#programmeren#\n', str_output='#programmeren#\n')
                .stdout('^m            m\n', str_output='m            m\n')
                .stdout('^i            i\n', str_output='i            i\n')
                .stdout('^n            n\n', str_output='n            n\n')
                .stdout('^o            o\n', str_output='o            o\n')
                .stdout('^r            r\n', str_output='r            r\n')
                .stdout('^#programmeren#\n', str_output='#programmeren#\n')
                .stdout('^#langste#\n', str_output='#langste#\n')
                .stdout('^k       k\n', str_output='k       k\n')
                .stdout('^o       o\n', str_output='o       o\n')
                .stdout('^r       r\n', str_output='r       r\n')
                .stdout('^t       t\n', str_output='t       t\n')
                .stdout('^#langste#\n', str_output='#langste#\n')
            )

@check50.check()
def woordlengte():
    """woordlengte.c werkt zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    int lengtes1[] = {5, 7};
    string tekst1 = "hello goodbye";
    bool b1 = check_lengtes(tekst1, lengtes1);
    printf("%i\n", b1);
    
    int lengtes2[] = {3, 2, 2, 4};
    string tekst2 = "fee fi fo fum";
    bool b2 = check_lengtes(tekst2, lengtes2);
    printf("%i\n", b2);
    
    int lengtes3[] = {4, 2, 4};
    string tekst3 = "this is cs50";
    bool b3 = check_lengtes(tekst3, lengtes3);
    printf("%i\n", b3);
    
    int lengtes4[] = {8, 3};
    string tekst4 = "terra ide";
    bool b4 = check_lengtes(tekst4, lengtes4);
    printf("%i\n", b4);
    
    int lengtes5[] = {2, 2, 6};
    string tekst5 = "in het midden";
    bool b5 = check_lengtes(tekst5, lengtes5);
    printf("%i\n", b5);
}
"""
    with helpers.replace_main("woordlengte.c", main):
        with helpers.logged_check_factory("woordlengte") as run_check:
            (run_check()
                .stdout('1\n', regex=False)
                .stdout('0\n', regex=False)
                .stdout('1\n', regex=False)
                .stdout('0\n', regex=False)
                .stdout('0\n', regex=False)
            )

@check50.check()
def gum():
    """gum.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    char tekst1[] = "gum gum dit allemaal en dat uit";
    gum(tekst1, "dit");
    printf("%s\n", tekst1);
    gum(tekst1, "uit");
    printf("%s\n", tekst1);
    gum(tekst1, "dat");
    printf("%s\n", tekst1);
    gum(tekst1, "en");
    printf("%s\n", tekst1);
    gum(tekst1, "allemaal");
    printf("%s\n", tekst1);
    gum(tekst1, "gum");
    printf("%s\n", tekst1);
    
    printf("\n");
    
    char tekst2[] = "fee fi fo fum";
    gum(tekst2, "f");
    printf("%s\n", tekst2);
    gum(tekst2, "ee");
    printf("%s\n", tekst2);
    gum(tekst2, "fo");
    printf("%s\n", tekst2);
    gum(tekst2, "dah");
    printf("%s\n", tekst2);
    gum(tekst2, "um");
    printf("%s\n", tekst2);
}
"""
    with helpers.replace_main("gum.c", main):
        with helpers.logged_check_factory("gum") as run_check:
            (run_check()
                .stdout("gum gum ___ allemaal en dat uit", regex=False)
                .stdout("gum gum ___ allemaal en dat ___", regex=False)
                .stdout("gum gum ___ allemaal en ___ ___", regex=False)
                .stdout("gum gum ___ allemaal __ ___ ___", regex=False)
                .stdout("gum gum ___ ________ __ ___ ___", regex=False)
                .stdout("___ ___ ___ ________ __ ___ ___", regex=False)
                .stdout("_ee _i _o _um\n", regex=False)
                .stdout("___ _i _o _um\n", regex=False)
                .stdout("___ _i _o _um\n", regex=False)
                .stdout("___ _i _o _um\n", regex=False)
                .stdout("___ _i _o ___\n", regex=False)
            )

@check50.check()
def code_som():
    """code_som.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    int getallen1[] = {10, 20, 30};
    int operaties1[] = {0, 2};
    reken_uit(getallen1, operaties1, 2);
    
    int getallen2[] = {80, 40, 50, 90, 100};
    int operaties2[] = {3, 1, 0, 2};
    reken_uit(getallen2, operaties2, 4);
    
    int getallen3[] = {25, 30, 4, 2, 1, 2};
    int operaties3[] = {0, 2, 3, 0, 1};
    reken_uit(getallen3, operaties3, 5);
}
"""
    with helpers.replace_main("code_som.c", main):
        with helpers.logged_check_factory("code_som") as run_check:
            (run_check()
                .stdout('10 + 20 * 30 = 900\n', regex=False)
                .stdout('80 / 40 - 50 + 90 * 100 = 4200\n', regex=False)
                .stdout('25 + 30 * 4 / 2 + 1 - 2 = 109\n', regex=False)
            )
