# Opdracht 2 tekstbestanden
# Naam student:Jasper Spannenberg
# Groep:IT2B

import random

# Kies een willekeurig getal tussen 1 en 100
geheim_getal = random.randint(1, 100)
aantal_raden = 0

# Welkom bij het spel
print("Raad mijn geheime getal!")

# Start de loop om te raden
while True:
    # Vraag de gebruiker om een getal in te voeren
    gebruiker_raad = int(input("Raad mijn geheime getal\n"))
    aantal_raden += 1  # Tel het aantal pogingen

    # Controleer of het geraden getal correct is
    if gebruiker_raad < geheim_getal:
        print("hoger")
    elif gebruiker_raad > geheim_getal:
        print("lager")
    else:
        print(f"Je hebt het getal geraden, het is {geheim_getal}!")
        print(f"Je hebt het in {aantal_raden} keer gedaan")
        break  # Stop de game als het juiste getal is geraden
