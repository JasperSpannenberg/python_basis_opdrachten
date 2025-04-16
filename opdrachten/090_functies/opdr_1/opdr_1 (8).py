# Opdracht 1 functies
# Naam student:Jasper Spannenberg
# Groep:IT2B


def write_to_file(bestandsnaam, tekst):
    with open(bestandsnaam, "a") as file:
        file.write(tekst + "\n")

# Voorbeeld van gebruik
my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)
