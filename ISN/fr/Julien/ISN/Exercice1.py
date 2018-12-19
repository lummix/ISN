#Exercice 1
# Ecrire un programme qui demande à l'utilisateurde saisir 5 entiers. Le programme compte le nombre d'élements
#Supérieur à 10 qui ont été entrés.


#declaration de ma liste
liste = []

#creation d'une boucle pour tester si l'entier tapé est plus grand que 10

for i in range(5):
    while True:
        try:
            n = int(input("Veuillez entrez un entier:"))
            break
            if n > 10:
             liste.append(n)
        except:
            print("Ca doit être un entier")

#on range notre liste pas ordre croissant
liste.sort()

#affiche le résultat.
print("Il y a " + str(liste.__len__()) +" nombres plus grand que 10")