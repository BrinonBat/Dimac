import Graphe

test=Graphe.Graphe("DSJC500.1")

for elem in range(len(test.mat_adj)):
    if test.aUneCouleurValide(elem)!=True : print("mal conçu !")

print(test)



print(test.nb_couleurs)
#coloration=[2,1,2]
print("coloration test "+str(Graphe.evalueColoration(test.couleurs)))