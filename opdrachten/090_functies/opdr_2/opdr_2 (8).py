# Opdracht 1 functies
# Naam student:Jasper Spannenberg
# Groep:IT2B

# Functie om kilometers naar miles om te rekenen
def kilometers_naar_miles(km):
    return km / 1.609344

# Functie om miles naar kilometers om te rekenen
def miles_naar_kilometers(miles):
    return miles * 1.609344

# Voorbeeldwaarden
kilometers = 1223
miles = 867

# Berekeningen
miles_result = kilometers_naar_miles(kilometers)
km_result = miles_naar_kilometers(miles)

# Output
print(f"{kilometers} kilometers = {miles_result} miles")
print(f"{miles} miles = {km_result} kilometers")