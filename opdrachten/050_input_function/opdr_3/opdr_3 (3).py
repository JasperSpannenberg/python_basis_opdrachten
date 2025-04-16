# Opdracht 3 input functie
# Naam student:Jasper Spannenberg
# Groep:IT2B

# Vraag om input van de gebruiker
invoer = input("Amsterdam,Zwolle,Dronten,Haarlem,Zaanstad")

# Zet de invoer om in een lijst (strip haalt eventuele spaties weg)
lijst = [item.strip() for item in invoer.split(",")]

# Sorteer de lijst in omgekeerde alfabetische volgorde
lijst.sort(reverse=True)

# Print de gesorteerde lijst
print("Gesorteerde lijst (omgekeerd alfabetisch):")
print(lijst)

