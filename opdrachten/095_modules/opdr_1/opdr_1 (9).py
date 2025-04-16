# Opdracht 1 functies
# Naam student:Jasper Spannenberg
# Groep:IT2B

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

from my_modules import personen

personenlijst = [
    {"voornaam": "Jan", "tussenvoegsel": "van der", "achternaam": "Vliet", "plaats": "Amsterdam"},
    {"voornaam": "Jan Jaap", "tussenvoegsel": "", "achternaam": "Siewers", "plaats": "Delft"},
    {"voornaam": "Piet", "tussenvoegsel": "de", "achternaam": "Vries", "plaats": "Leiden"},
    {"voornaam": "Griet", "tussenvoegsel": "van der", "achternaam": "Pol", "plaats": "Drachten"}
]

# Test: filter op voornaam begint met 'ja'
print("Filter op voornaam 'ja':")
resultaten = personen.filter(personenlijst, "voornaam", "ja")
for naam in resultaten:
    print(naam)

# Test: filter op voornaam begint met 'pie'
print("\nFilter op voornaam 'pie':")
resultaten = personen.filter(personenlijst, "voornaam", "pie")
for naam in resultaten:
    print(naam)

# Test: filter op plaats begint met 'd'
print("\nFilter op plaats 'd':")
resultaten = personen.filter(personenlijst, "plaats", "d")
for naam in resultaten:
    print(naam)