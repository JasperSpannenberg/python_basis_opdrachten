# Opdracht 3 condities
# Naam student:Jasper Spannenberg
# Groep: IT2B


# Gegeven variabelen
normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Vraag de leeftijd van de bezoeker
age = int(input("Geef uw leeftijd in aantal jaar\n"))

# Bepaal in welke groep de bezoeker valt en bereken de korting
for groep, (min_age, max_age) in leeftijd.items():
    if min_age <= age <= max_age:
        korting = kortings_percentages[groep]
        prijs = normale_toegangsprijs * (1 - korting / 100)

        # Print de informatie
        print(f"U behoort tot de groep {groep}")
        print(f"U krijgt {korting}% korting")
        print(f"U betaalt daarom {prijs:.2f}")
        break
