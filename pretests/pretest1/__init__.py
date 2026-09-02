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


def main_voor(functie):
    """
    Een main die de functie aanroept met de hoeveelheid die als argument
    meegegeven wordt, en enkel het resultaat print. Zo gaat er per aanroep
    precies een run overheen, en blijft de foutmelding kort.
    """
    return r"""
int main(int argc, char *argv[])
{
    int hoeveelheid = 0;
    sscanf(argv[1], "%d", &hoeveelheid);
    printf("%.2f\n", """ + functie + r"""(hoeveelheid));
}
"""


def check_functie(functie, verwachtingen):
    """Roep functie aan voor elke hoeveelheid en vergelijk met de verwachte prijs"""
    with helpers.replace_main("tapas.c", main_voor(functie)):
        with helpers.logged_check_factory("tapas") as run_check:
            for hoeveelheid, prijs in verwachtingen:
                run_check(str(hoeveelheid)).stdout(
                    regel(prijs),
                    str_output=f"{functie}({hoeveelheid}) geeft {prijs}"
                )


@check50.check()
def vegetarisch():
    """bereken_kosten_vegetarisch berekent de juiste prijs"""
    check_functie("bereken_kosten_vegetarisch", [
        (1, "5.00"),
        (2, "10.00"),
        (3, "14.25"),
        (4, "19.00"),
        (5, "22.50"),
        (10, "45.00"),
    ])


@check50.check()
def vis():
    """bereken_kosten_vis berekent de juiste prijs"""
    check_functie("bereken_kosten_vis", [
        (1, "6.75"),
        (2, "13.50"),
        (3, "20.25"),
        (4, "27.00"),
        (6, "36.45"),
        (10, "60.75"),
    ])


@check50.check()
def vlees():
    """bereken_kosten_vlees berekent de juiste prijs"""
    check_functie("bereken_kosten_vlees", [
        (1, "8.00"),
        (2, "14.00"),
        (3, "18.00"),
        (4, "24.00"),
        (5, "30.00"),
        (10, "60.00"),
    ])


@check50.check()
def tapas():
    """tapas.c werkt precies zoals de voorbeelden in de opdracht"""
    gerechten = {1: "vegetarisch", 2: "vis", 3: "vlees"}

    with helpers.logged_check_factory("tapas") as run_check:
        for type_gerecht, hoeveelheid, prijs in [
            (2, 3, "20.25"),
            (3, 2, "14.00"),
            (1, 4, "19.00"),
            (1, 5, "22.50"),
            (2, 6, "36.45"),
            (3, 1, "8.00"),
        ]:
            (run_check()
                .stdin(str(type_gerecht), prompt=False)
                .stdin(str(hoeveelheid), prompt=False)
                .stdout(
                    prijs.replace(".", r"\."),
                    str_output=f"de totale kosten van {hoeveelheid} porties "
                               f"{gerechten[type_gerecht]} zijn {prijs}"
                ))
