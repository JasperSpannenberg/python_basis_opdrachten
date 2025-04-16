# Opdracht 3 Tekst opslaan
# Naam student:Jasper Spannenberg
# Groep:IT2B

def encrypt(tekst):
    encrypted_tekst = ""

    for char in tekst:
        # Controleer of het karakter een kleine letter is
        if 'a' <= char <= 'z':
            encrypted_tekst += chr((ord(char) - ord('a') + 5) % 26 + ord('a'))
        # Controleer of het karakter een hoofdletter is
        elif 'A' <= char <= 'Z':
            encrypted_tekst += chr((ord(char) - ord('A') + 5) % 26 + ord('A'))
        # Als het geen letter is, voeg het ongewijzigd toe
        else:
            encrypted_tekst += char

    return encrypted_tekst


# Vraag om invoer
tekst = input("Geef de tekst die wilt encrypten..\n")

# Encrypt de tekst
gecodeerde_tekst = encrypt(tekst)

# Print de geëncryptede tekst
print("Geëncryptede tekst:")
print(gecodeerde_tekst)



