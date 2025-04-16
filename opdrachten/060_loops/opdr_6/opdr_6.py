# Opdracht 3 input functie
# Naam student: Jasper Spannenberg
# Groep: IT2B

# Originele lijst
pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer de lijst op alfabet
pizzas.sort()

# Voeg een pizza toe (bijvoorbeeld 'yo-favorito')
pizzas.append('yo-favorito')

# Verwijder de minst lekkere pizza (bijvoorbeeld 'olivio')
pizzas.remove('olivio')

# Print de eerste 3 pizza's
print(pizzas[:3])

# Print alleen de middelste pizza (lijst heeft nu 5 items, dus index 2 is midden)
print([pizzas[len(pizzas)//2]])

# Print de laatste 3 pizza's
print(pizzas[-3:])
# Hier start de for-loop

my_list = []