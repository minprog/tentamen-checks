import check50
import check50.c
import check50.internal

helpers = check50.internal.import_file(
    "helpers",
    check50.internal.check_dir / "../helpers/helpers.py"
)
helpers.set_stdout_limit(10000)


@check50.check()
def difference():
    """difference.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    string a0 = "abc";
    string b0 = "ad";
    print_difference(a0, b0);
    
    string a1 = "abcdefghij";
    string b1 = "abxdefyhij";
    print_difference(a1, b1);
    
    string a2 = "abc";
    string b2 = "abcdef";
    print_difference(a2, b2);
    
    print_difference(b2, a2);
    
    string a3 = "FoobaR";
    string b3 = "foobar!";
    print_difference(b3, a3);
}
"""
    with helpers.replace_main("difference.c", main):
        with helpers.logged_check_factory("difference") as run_check:
            (run_check()
                .stdout('-#+', regex=False)
                .stdout('--#---#---', regex=False)
                .stdout('---+++', regex=False)
                .stdout('---+++', regex=False)
                .stdout('#----#+', regex=False)
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
                .stdout('Postal code: 1234AB', regex=False)
                .stdout('Postal code: 1337yo', regex=False)
                .stdout('Postal code: 1506HF', regex=False)
                .stdout('Postal code: 1403Yz', regex=False)
            )


@check50.check()
def bundled():
    """bundled.c werkt precies zoals de voorbeelden in de opdracht"""
    main = r"""
int main(void)
{
    int n1 = 7;
    int numbers1[] = {3, 4, 5, 6, 7, 8, 9};
    print_bundles(numbers1, n1, 3);
    printf("\n");
    
    int n2 = 11;
    int numbers2[] = {20, 15, 14, 16, 37, 45, 5, 18, 4, 3, 2};
    print_bundles(numbers2, n2, 4);
    printf("\n");
    
    int n3 = 4;
    int numbers3[] = {1, 2, 3, 4};
    print_bundles(numbers3, n3, 10);
    printf("\n");
    
    print_bundles(numbers3, n3, 1);
    printf("\n");
}
"""
    with helpers.replace_main("bundled.c", main):
        with helpers.logged_check_factory("bundled") as run_check:
            (run_check()
                .stdout('[3, 4, 5]', regex=False)
                .stdout('[6, 7, 8]', regex=False)
                .stdout('[9]', regex=False)
                .stdout('[20, 15, 14, 16]', regex=False)
                .stdout('[37, 45, 5, 18]', regex=False)
                .stdout('[4, 3, 2]', regex=False)
                .stdout('[1, 2, 3, 4]', regex=False)
                .stdout('[1]', regex=False)
                .stdout('[2]', regex=False)
                .stdout('[3]', regex=False)
                .stdout('[4]', regex=False)
            )
