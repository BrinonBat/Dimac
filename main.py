import Graphe
import metaheuristiques
test=Graphe.Graphe("DSJC500.1")
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

metaheuristiques.tabou(test)

print(test)
print(test.nb_couleurs)
print(" est valide ? "+str(test.estValide()))