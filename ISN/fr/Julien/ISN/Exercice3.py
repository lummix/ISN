#Exercice 3

# Ecrire un programme qui demande à l'utilisateur de saisir les notes sur 20 des élèves d'une classe.
#Le nombre d'élèves est choisi au début du programme puis le programme affiche la somme, la plus grand valeur, la plus petite et la moyenne


import numpy

#On demande le nombre d'élèves et on check que le nombre est bien un entier positif
while True:
    try:
       n = int(input("Veuillez saisir le nombre d'élèves"))
       if(n > 0):
           break
       else:
           print("Merci d'entrer un nombre positif")
    except:
        print("Merci de saisir un entier")


#Creation de la liste
notes = []

#Boucle


for i in range(n):
    while True: # La double boucle n'est pas très belle mais elle fait le taff pour cet exo
        try:
            note = float(input("Veuillez entrer la note de l'élève: "))
            if note >0 and note <= 20:
                notes.append(note)
                break
            else:
             print("La note doit etre comprise entre 0 et 20")
        except:
            print("La note ne peut pas être un caractère, attention")



#On range la liste
notes.sort()

#La plus petite valeur aura comme index 0
min = notes[0]

#La plus grand valeur aura comme index la longueur de la liste
max = notes.__len__() -1
maxi = notes[max]

#Somme de la liste
somme = sum(notes)

#Moyenne de la liste
moyenne = numpy.mean(notes)


print("La somme de la liste est :" + str(somme))
print("Le min de la liste est :" + str(min))
print("La moyenne de la liste est :" + str(moyenne))
print("Le max de la liste est :" + str(maxi))
