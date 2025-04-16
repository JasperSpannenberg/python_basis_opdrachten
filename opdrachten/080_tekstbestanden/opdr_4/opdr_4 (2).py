# Opdracht 4 Tekst opslaan
# Naam student:Jasper Spannenberg
# Groep: IT2B


# Lijst van vragen
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

# Lijst om de antwoorden van de feestgangers op te slaan
feestganger = {}

# Stel de vragen en sla de antwoorden op
for index, vraag in enumerate(vragen):
    antwoord = input(f"{vraag}\n")
    if index == 0:
        feestganger['voornaam'] = antwoord
    elif index == 1:
        feestganger['achternaam'] = antwoord
    elif index == 2:
        feestganger['drank'] = antwoord
    elif index == 3:
        feestganger['eten'] = antwoord

# Print een bedankje
print("Bedankt voor het invullen!")
print("See you at the party.")

# Schrijf de gegevens naar een tekstbestand
with open("feestgangers.txt", "a") as file:
    file.write(f"voornaam: {feestganger['voornaam']}\n")
    file.write(f"achternaam: {feestganger['achternaam']}\n")
    file.write(f"drank: {feestganger['drank']}\n")
    file.write(f"eten: {feestganger['eten']}\n")
    file.write("\n")

# Indien gewenst, kun je de inhoud van het bestand printen
print("\nInhoud van tekstbestand:")
with open("feestgangers.txt", "r") as file:
    print(file.read())