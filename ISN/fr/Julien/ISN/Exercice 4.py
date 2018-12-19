# Exercice 4

#On se donne un liste d'entier. Ecrire un programme qui range les élements de cette liste dans une autre liste en mettant les
#élements pairs à gauche et les éléments impairs à droite.


# On demande le nombre d'élements
n = int(input("Veuillez saisir le nombre d'élèves"))

# Creation de liste
pair = []
impair = []

# Boucle

for i in range(n):
    note = int(input("Veuillez entrer les notes des élèves: "))
    if note % 2 ==0:
        pair.append(note)
    else:
        impair.append(note)

#On combine le tout dans une liste
print(pair + impair)


