import Graphe
import metaheuristiques
import time



#récupération des seeds et lancement
s=open('randomSeeds.csv','r')
for li in s:
    seeds=li.split()
    seed=int(seeds[0])

#premiere coloration
test=Graphe.Graphe("DSJC500.1",seed)

est_valide=True
for elem in range(len(test.mat_adj)):
    if test.aUneCouleurValide(elem)!=True : est_valide=False

print(test)



print(test.nb_couleurs)
print("coloration test "+str(Graphe.evalueColoration(test.couleurs)))

duree=time.time()
#lancement de l'algo
taille_liste=2
metaheuristiques.tabu_nouv(test,taille_liste)
end=time.time()
duree=(end-duree)

print(test)
print(test.nb_couleurs)
print(" est valide ? "+str(test.estValide()))
print('durée totale :'+str(duree))