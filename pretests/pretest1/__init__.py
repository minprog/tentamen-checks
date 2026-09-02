import re

import check50
import check50.internal

helpers = check50.internal.import_file(
    "helpers",
    check50.internal.check_dir / "../../helpers/helpers.py"
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
def vegetarisch():
    """bereken_kosten_vegetarisch berekent de juiste prijs"""
    main = r"""
int main(void)
{
    printf("%.2f\n", bereken_kosten_vegetarisch(1));
    printf("%.2f\n", bereken_kosten_vegetarisch(2));
    printf("%.2f\n", bereken_kosten_vegetarisch(3));
    printf("%.2f\n", bereken_kosten_vegetarisch(4));
    printf("%.2f\n", bereken_kosten_vegetarisch(5));
    printf("%.2f\n", bereken_kosten_vegetarisch(10));
}
"""
    with helpers.replace_main("tapas.c", main):
        with helpers.logged_check_factory("tapas") as run_check:
            (run_check()
                .stdout(regel("5.00"), str_output="5.00")
                .stdout(regel("10.00"), str_output="10.00")
                .stdout(regel("14.25"), str_output="14.25")
                .stdout(regel("19.00"), str_output="19.00")
                .stdout(regel("22.50"), str_output="22.50")
                .stdout(regel("45.00"), str_output="45.00")
            )


@check50.check()
def vis():
    """bereken_kosten_vis berekent de juiste prijs"""
    main = r"""
int main(void)
{
    printf("%.2f\n", bereken_kosten_vis(1));
    printf("%.2f\n", bereken_kosten_vis(2));
    printf("%.2f\n", bereken_kosten_vis(3));
    printf("%.2f\n", bereken_kosten_vis(4));
    printf("%.2f\n", bereken_kosten_vis(6));
    printf("%.2f\n", bereken_kosten_vis(10));
}
"""
    with helpers.replace_main("tapas.c", main):
        with helpers.logged_check_factory("tapas") as run_check:
            (run_check()
                .stdout(regel("6.75"), str_output="6.75")
                .stdout(regel("13.50"), str_output="13.50")
                .stdout(regel("20.25"), str_output="20.25")
                .stdout(regel("27.00"), str_output="27.00")
                .stdout(regel("36.45"), str_output="36.45")
                .stdout(regel("60.75"), str_output="60.75")
            )


@check50.check()
def vlees():
    """bereken_kosten_vlees berekent de juiste prijs"""
    main = r"""
int main(void)
{
    printf("%.2f\n", bereken_kosten_vlees(1));
    printf("%.2f\n", bereken_kosten_vlees(2));
    printf("%.2f\n", bereken_kosten_vlees(3));
    printf("%.2f\n", bereken_kosten_vlees(4));
    printf("%.2f\n", bereken_kosten_vlees(5));
    printf("%.2f\n", bereken_kosten_vlees(10));
}
"""
    with helpers.replace_main("tapas.c", main):
        with helpers.logged_check_factory("tapas") as run_check:
            (run_check()
                .stdout(regel("8.00"), str_output="8.00")
                .stdout(regel("14.00"), str_output="14.00")
                .stdout(regel("18.00"), str_output="18.00")
                .stdout(regel("24.00"), str_output="24.00")
                .stdout(regel("30.00"), str_output="30.00")
                .stdout(regel("60.00"), str_output="60.00")
            )


@check50.check()
def tapas():
    """tapas.c werkt precies zoals de voorbeelden in de opdracht"""
    with helpers.logged_check_factory("tapas") as run_check:
        run_check().stdin("2").stdin("3").stdout(r"20\.25", str_output="20.25")
        run_check().stdin("3").stdin("2").stdout(r"14\.00", str_output="14.00")
        run_check().stdin("1").stdin("4").stdout(r"19\.00", str_output="19.00")
        run_check().stdin("1").stdin("5").stdout(r"22\.50", str_output="22.50")
        run_check().stdin("2").stdin("6").stdout(r"36\.45", str_output="36.45")
        run_check().stdin("3").stdin("1").stdout(r"8\.00", str_output="8.00")
