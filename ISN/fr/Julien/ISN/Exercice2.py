#Exercice 2

#Ecrire un programme qui demande une valeur de n, puis qui demande n nombres à l'utilisateur.
#Le programme affiche ensuite la liste des nombres pairs qui ont été entrés.

#Demande à l'utilisateur de choisir une valeur de n

while True:
    try:
     n = int(input("Combien d'entrées voulez-vous ?"))
     break
     if n <0:
         print("Merci de saisir un nb positif")
    except:
        print("Merci d'entrer un entier!")


#création de la liste

liste = []

#création de la boucle

for i in range(n):
 while True:
   try:
    nombre = int(input("Veuillez saisir un nombre"))
    break
    if (nombre % 2) ==0:
        liste.append(nombre)
   except:
       print("Merci de saisir un entier")
#on range notre liste dans l'ordre croissant

liste.sort()

#On affiche la liste contenant tous les nombres pairs
print("Les nombres pairs sont" +str(liste))




