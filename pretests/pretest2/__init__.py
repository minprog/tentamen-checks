import re

import check50
import check50.internal

helpers = check50.internal.import_file(
    "helpers",
    check50.internal.check_dir / "../../helpers/helpers.py"
)
helpers.set_stdout_limit(10000)


def verdict(uitslag):
    """
    Regex die de uitslag koppelt aan de prompt van diezelfde sprong. Zo wijst
    een foutmelding naar de sprong die misgaat, en niet naar een sprong verderop
    waar dezelfde tekst toevallig ook staat.
    """
    return rf"Hoogte:[^\n]*{re.escape(uitslag)}"


def hoogste(centimeters):
    """Regex voor de slotregel, met de tekst erbij zodat een ingetikte
    hoogte die toevallig hetzelfde getal is niet per ongeluk matcht"""
    return rf"[Hh]oogste sprong:\s*{centimeters}"


def run_sprongen(run_check, hoogtes):
    """Start het programma en voer het aantal sprongen en de hoogtes in"""
    check = run_check().stdin(str(len(hoogtes)), prompt=False)
    for hoogte in hoogtes:
        check = check.stdin(str(hoogte), prompt=False)
    return check


@check50.check()
def record():
    """record.c meldt een record bij iedere hogere sprong"""
    with helpers.logged_check_factory("record") as run_check:
        (run_sprongen(run_check, [120, 115, 140])
            .stdout(verdict("Record!"), str_output="Record! na 120")
            .stdout(verdict("Geen record"), str_output="Geen record na 115")
            .stdout(verdict("Record!"), str_output="Record! na 140")
            .stdout(hoogste(140), str_output="Hoogste sprong: 140"))

        (run_sprongen(run_check, [133])
            .stdout(verdict("Record!"), str_output="Record! na 133")
            .stdout(hoogste(133), str_output="Hoogste sprong: 133"))


@check50.check(record)
def gelijk():
    """een even hoge sprong is geen record"""
    with helpers.logged_check_factory("record") as run_check:
        (run_sprongen(run_check, [70, 70])
            .stdout(verdict("Record!"), str_output="Record! na 70")
            .stdout(verdict("Geen record"), str_output="Geen record na nog een 70")
            .stdout(hoogste(70), str_output="Hoogste sprong: 70"))

        (run_sprongen(run_check, [90, 105, 105, 100])
            .stdout(verdict("Record!"), str_output="Record! na 90")
            .stdout(verdict("Record!"), str_output="Record! na 105")
            .stdout(verdict("Geen record"), str_output="Geen record na nog een 105")
            .stdout(verdict("Geen record"), str_output="Geen record na 100")
            .stdout(hoogste(105), str_output="Hoogste sprong: 105"))


@check50.check(record)
def dalend():
    """de hoogste sprong blijft staan als de sprongen daarna lager zijn"""
    with helpers.logged_check_factory("record") as run_check:
        (run_sprongen(run_check, [150, 20, 30, 40])
            .stdout(verdict("Record!"), str_output="Record! na 150")
            .stdout(verdict("Geen record"), str_output="Geen record na 20")
            .stdout(verdict("Geen record"), str_output="Geen record na 30")
            .stdout(verdict("Geen record"), str_output="Geen record na 40")
            .stdout(hoogste(150), str_output="Hoogste sprong: 150"))


@check50.check(record)
def geen_sprongen():
    """bij 0 sprongen print record.c Geen sprongen"""
    with helpers.logged_check_factory("record") as run_check:
        (run_sprongen(run_check, [])
            .stdout("Geen sprongen", str_output="Geen sprongen", regex=False))
