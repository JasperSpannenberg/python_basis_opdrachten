# Opdracht 1 functies
# Naam student:Jasper Spannenberg
# Groep:IT2B

def volledige_naam(lijst_met_namen):
    for persoon in lijst_met_namen:
        # Maak een lijst van de naamdelen
        delen = [persoon['voornaam'], persoon['tussenvoegsel'], persoon['achternaam']]
        # Verwijder lege stukken (zoals een leeg tussenvoegsel)
        volledige_naam = " ".join(deel for deel in delen if deel.strip())
        print(volledige_naam)

namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)