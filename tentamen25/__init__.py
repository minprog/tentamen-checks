import check50
import check50.internal

helpers = check50.internal.import_file(
    "helpers",
    check50.internal.check_dir / "../helpers/helpers.py"
)
helpers.set_stdout_limit(10000)


@check50.check()
def postal():
    """postal.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    string address1 = "Dorpsstraat 34 1234AB";
    print_postal_code(address1);
    
    string address2 = "1337yo Hoofdstraat 1226a";
    print_postal_code(address2);
    
    string address3 = "Hugo de Vrieslaan 1506HF 37AB";
    print_postal_code(address3);
    
    string address4 = "1403Yz 319 Fooweg";
    print_postal_code(address4);
}
"""
    with helpers.replace_main("postal.c", main):
        with helpers.logged_check_factory("postal") as run_check:
            (run_check()
                .stdout(r'(Postal code: )?1234AB\s*'
                        r'(Postal code: )?1337yo\s*'
                        r'(Postal code: )?1506HF\s*'
                        r'(Postal code: )?1403Yz\s*')
            )


@check50.check()
def raster():
    """raster.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    print_raster("abc", "de", "fghi");
    print_raster("a", "b", "c");
    print_raster("minor", "programmeren", "tentamen");
}
"""
    with helpers.replace_main("raster.c", main):
        with helpers.logged_check_factory("raster") as run_check:
            (run_check()
                .stdout('---------', regex=False)
                .stdout('|a|b|c| |', regex=False)
                .stdout('|d|e| | |', regex=False)
                .stdout('|f|g|h|i|', regex=False)
                .stdout('---------', regex=False)
                .stdout('---', regex=False)
                .stdout('|a|', regex=False)
                .stdout('|b|', regex=False)
                .stdout('|c|', regex=False)
                .stdout('---', regex=False)
                .stdout('-------------------------', regex=False)
                .stdout('|m|i|n|o|r| | | | | | | |', regex=False)
                .stdout('|p|r|o|g|r|a|m|m|e|r|e|n|', regex=False)
                .stdout('|t|e|n|t|a|m|e|n| | | | |', regex=False)
                .stdout('-------------------------', regex=False)
            )


@check50.check()
def athletics():
    """athletics.c werkt zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    int distances1[] = {0, 90, 170, 250, 325, 400};
    print_stats(distances1, 6);
    
    int distances2[] = {0, 70, 140, 210, 270, 330, 390, 50, 100, 150, 200};
    print_stats(distances2, 11);
    
    int distances3[] = {
        0, 65, 125, 190, 250, 310, 370, 30, 90,
        150, 210, 270, 330, 380, 40, 100, 150, 200
    };
    print_stats(distances3, 18);
}
"""
    with helpers.replace_main("athletics.c", main):
        with helpers.logged_check_factory("athletics") as run_check:
            (run_check()
                .stdout(r'Top speed: 32\.40 km/h', str_output='Top speed: 32.40 km/h')
                .stdout(r'Total distance: 400\.0+ m', str_output='Total distance: 400.00 m')
                .stdout(r'Top speed: 25\.20 km/h', str_output='Top speed: 25.20 km/h')
                .stdout(r'Total distance: 600\.0+ m', str_output='Total distance: 600.00 m')
                .stdout(r'Top speed: 23\.40 km/h', str_output='Top speed: 23.40 km/h')
                .stdout(r'Total distance: 1000\.0+ m', str_output='Total distance: 1000.00 m')
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
