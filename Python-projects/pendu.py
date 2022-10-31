
import random
file = open ("/home/vitaly/Projet python/Python-projects/dico_france.txt", "r", encoding = "ISO-8859-15")
dico=file.read().split()
#print(dico)
mot = random.choice(dico)

#print (mot)
lvl = (input("Choisir lvl facile intermediaire expert: "))
hp = 0

if lvl == "facile":
    hp = 10
elif lvl == "intermediaire":
    hp = 7
elif lvl == "expert":
    hp = 4
else:
    print("erreur warrning warning BOUUUUM")

historique = []
lettres = []
trouve = False
print ("nombre de lettre :", len(mot))
while not trouve:
    trouve = True
    for i in mot :
        if i in lettres:
            print (i,end = "")
        else: 
            trouve = False
            print (" _ ", end ="")
    if hp == 0: 
        print (" t'es un looser! Il fallait trouver ")
        break
    if trouve:
        print(" PABABABABABA T'es un bogosss suuuuuu suuuuuuu")
        break

    lettre = input("  :Choisi une lettre :")
    lettres.append(lettre)
    
    if lettre not in mot:
        hp = hp -1
        print ("Il te reste maintenant", hp)
    
    if lvl != "expert" :
        historique.append(lettre)
        print ("Tu as deja tape: ", historique)