# Opdracht 1 while-loops
# Naam student:Jasper Spannenberg
# Groep:IT2B

# Vraag 1: Wat vind je van de huidige regering?
regering_antwoord = input("Wat vind je van de huidige regering?\n")

# Vraag 2: Wat vind je van de Python-lessen tot nu toe?
python_antwoord = input("Wat vind je van de Python-lessen tot nu toe?\n")

# Vraag 3: Wat vind jij de mooiste stad van Nederland?
stad_antwoord = input("Wat vind jij de mooiste stad van Nederland?\n")

# Open het bestand in 'append' mode om de gegevens toe te voegen
with open("enquete_resultaten.txt", "a") as bestand:
    # Sla de antwoorden op in het bestand
    bestand.write(f"Wat vind je van de huidige regering?: {regering_antwoord}\n")
    bestand.write(f"Wat vind je van de Python-lessen tot nu toe?: {python_antwoord}\n")
    bestand.write(f"Wat vind jij de mooiste stad van Nederland?: {stad_antwoord}\n")
    bestand.write("\n")  # Voeg een lege regel toe tussen enquêtes voor leesbaarheid

# Bevestiging dat de resultaten zijn opgeslagen
print("\nBedankt voor het invullen! Je antwoorden zijn opgeslagen.")