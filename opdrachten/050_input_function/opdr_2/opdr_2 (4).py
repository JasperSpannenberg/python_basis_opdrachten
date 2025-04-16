# Opdracht 2 berekeningen
# Naam student: Jasper Spannenberg
# Groep:IT2B

# Begin met de originele lijst van gasten
gastenlijst = ["Jasper", "Paul", "Kees", "Marie", "Hilda"]

# Print de oorspronkelijke gastenlijst
print("Oorspronkelijke lijst:", gastenlijst)

# Marie belt en wil niet meer meegaan, dus verwijderen we haar uit de lijst
gastenlijst.remove("Marie")

# Print de aangepaste lijst na het verwijderen van Marie
print("Na het verwijderen van Marie:", gastenlijst)

# George belt en wil naast Kees zitten, dus we voegen George toe na Kees
# Eerst vinden we de index van Kees en voegen we George na Kees toe
index_kees = gastenlijst.index("Kees")
gastenlijst.insert(index_kees + 1, "George")

# Print de uiteindelijke gastenlijst
print("Na het toevoegen van George:", gastenlijst)