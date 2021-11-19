import Graphe
import metaheuristiques




#récupération des seeds et lancement
s=open('randomSeeds.csv','r')
for li in s:
    seeds=li.split()
    seed=int(seeds[0])

test=Graphe.Graphe("DSJC500.1",seed)
est_valide=True
for elem in range(len(test.mat_adj)):
    if test.aUneCouleurValide(elem)!=True : est_valide=False

print(test)



print(test.nb_couleurs)
#coloration=[2,1,2]
print("coloration test "+str(Graphe.evalueColoration(test.couleurs)))

#test.changeCouleur(0,test.set_couleurs[0][0])
#print(test)
#print("modification test "+str(Graphe.evalueColoration(test.couleurs)))

taille_liste=2
metaheuristiques.tabou(test,taille_liste)

print(test)
print(test.nb_couleurs)
print(" est valide ? "+str(test.estValide()))