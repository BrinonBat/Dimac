# nom_fic : string
# mat_adj : list<list<bool>> matrice d'adjacence du graphe
# couleurs: list<int>, meilleure coloration jusqu'à maintenant
# nb_couleurs: int
class Graphe:
    def __init__(self,fic):
        self.nom_fic=fic

        #génération de la matrice d'adjacence
        g=open('D_graphes/'+fic,'r')
        for li in g:
            elems=li.split()
            if(elems[0]=='p'): self.mat_ajd=[([0]*(int(elems[2])+1))]*(int(elems[2])+1) # création d'une matrice de 0
            elif(elems[0]=='e'): self.mat_adj[int(elems[1])][int(elems[2])]=1 # place un 1 dans la case correspondante

        #TODO premiere coloration
        self.couleurs=[]
        self.nb_couleurs=0


    
    def __str__(self):
        return "\n graphe du fichier "+self.nom_fic+"\n coloré tel que suit :"+str(self.couleurs)

def evalueColoration(coloration):
    comptage=[0]*max(coloration)
    resultat=0

    for elem in coloration:
        comptage[elem]+=1

    for couleur in comptage:
        resultat+=couleur*comptage[couleur]

    return resultat