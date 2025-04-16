# Opdracht 1 input function
# Naam student: Jasper Spannenberg
# Groep: IT2B

import math

# Vraag de gebruiker om de lengtes van twee zijden in te voeren
zijde1 = float(input("Geef de lengte van de eerste zijde (of de schuine zijde als je die weet): "))
zijde2 = float(input("Geef de lengte van de tweede zijde (of de schuine zijde als je die weet): "))

# Vraag welke van de zijden de schuine zijde is, en voer de berekening uit
is_schuine_zijde = input("Is de eerste zijde de schuine zijde? (ja/nee): ").strip().lower()

if is_schuine_zijde == "ja":
    # Bereken de lengte van de ontbrekende rechthoekige zijde
    rechthoekige_zijde = math.sqrt(zijde1**2 - zijde2**2)
    print(f"De lengte van de ontbrekende rechthoekige zijde is: {rechthoekige_zijde}")
else:
    # Bereken de schuine zijde
    schuine_zijde = math.sqrt(zijde1**2 + zijde2**2)
    print(f"De lengte van de schuine zijde is: {schuine_zijde}")