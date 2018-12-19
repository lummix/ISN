#Exerice 5
#Mini Projet

#Développer un programme reprennant le principe du chiffrement de César. ( Chiffre de César)

#Définition des caractères utilsés
minuscules = 'abcdefghijklmnopqrstuvwxyz'
majuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Fonctions
def rotation(chaine, x):

    return chaine[x:] + chaine[:x]

def index(c, chaine):
    for i in range(len(chaine)):
        if (c == chaine[i]):
            return i
    return -1

def chiffre_minuscules(chaine, x):

    r = rotation(minuscules, x)
    resultat = ''
    for lettre in chaine:
        resultat = resultat + r[index(lettre, minuscules)]
    return resultat

def chiffre(chaine, x):

    r_min = rotation(minuscules, x)
    r_maj = rotation(majuscules, x)
    resultat = ''
    for lettre in chaine:
        if lettre in minuscules:
            resultat = resultat + r_min[index(lettre, minuscules)]
        elif lettre in majuscules:
            resultat = resultat + r_maj[index(lettre, majuscules)]
        else:
            resultat = resultat + lettre
    return resultat

# Utilisation :
#print(chiffre(" la phase / mot", x (nb de décalage)))

#Exemple:
#print(chiffre_minuscules('bonjour', 3))
print(chiffre('Test AHAH', 3))
