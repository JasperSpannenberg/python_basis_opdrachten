# Opdracht 4 condities
# Naam student:Jasper Spannenberg
# Groep:IT2B

# Beschikbare toppings en prijzen
toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]

# Maak een lijst van alleen de toppingsnamen
beschikbare_toppings = [topping[0] for topping in toppings]

# Vraag de gebruiker om een keuze
keuze = input(f"Kies je topping uit deze lijst: {beschikbare_toppings}\n")

# Controleer of de keuze geldig is
geselecteerde_topping = next((topping for topping in toppings if topping[0] == keuze), None)

if geselecteerde_topping:
    # Als de topping gevonden is, toon de naam en prijs
    print(f"U heeft {geselecteerde_topping[0]} besteld. Dat kost {geselecteerde_topping[1]}")
else:
    # Als de topping niet gevonden is
    print("Uw keuze zit niet in ons assortiment")