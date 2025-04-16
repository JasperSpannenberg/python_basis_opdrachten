# my_modules/csv.py

def schrijf_naar_csv(bestandsnaam, data):
    """
    Schrijft een lijst van lijsten naar een CSV-bestand.

    :param bestandsnaam: Naam van het bestand (bijv. 'output.csv')
    :param data: Een lijst van lijsten, bijv: [["voornaam", "achternaam"], ["Willem", "Dijk"]]
    """
    with open(bestandsnaam, "w", encoding="utf-8") as file:
        for regel in data:
            file.write(",".join(regel) + "\n")