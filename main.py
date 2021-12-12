import Graphe
import metaheuristiques
import time
import random


#récupération des seeds et lancement
s=open('randomSeeds.csv','r')
for li in s:
    seeds=li.split()
    seed=int(seeds[0])
random.seed(seed)
#premiere coloration
graphe=Graphe.Graphe("DSJC500.1")
print(graphe.nb_couleurs)
print("coloration graphe "+str(Graphe.evalueColoration(graphe.couleurs)))

duree=time.time()
#lancement de l'algo
taille_liste=200
metaheuristiques.tabu(graphe,taille_liste,1000)
end=time.time()
duree=(end-duree)

print(graphe)
print(graphe.nb_couleurs)
print(" est valide ? "+str(graphe.estValide()))
print("son score est de "+str(Graphe.evalueColoration(graphe.couleurs)))
print('durée totale :'+str(duree))