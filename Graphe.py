from os import remove
import bisect
import primoColorations

# nom_fic : string
# mat_adj : list<list<bool>> matrice d'adjacence du graphe
# couleurs: list<int>, meilleure coloration jusqu'à maintenant
# set_couleurs: list<list<int>> matrice indiquant pour chaque sommet les couleurs qu'il peut prendre
# nb_couleurs: int
class Graphe:
    def __init__(self,fic,primo_colo):
        self.nom_fic=fic

        #génération de la matrice d'adjacence
        g=open('D_graphes/'+fic,'r')
        for li in g:
            elems=li.split()
            if(elems[0]=='p'): #création d'une matrice de 0
                self.mat_adj=[]
                for li in range(int(elems[2])+1):
                    ligne=[]
                    for col in range(int(elems[2])+1):
                        ligne.append(0)
                    self.mat_adj.append(ligne)
            elif(elems[0]=='e'):  #remplissage de 1 pour les sommets adjacents
                self.mat_adj[int(elems[2])][int(elems[1])]=1
                self.mat_adj[int(elems[1])][int(elems[2])]=1

        #première coloration
        if(primo_colo=="rand"):primoColorations.aleatoire(self)
        elif(primo_colo=="max"):primoColorations.gloutonMax(self)
        elif(primo_colo=="min"):primoColorations.gloutonMin(self)
        else:  print("WRONG PRIMO COLORATION")

    def __str__(self):
        return "\n graphe du fichier "+self.nom_fic+"\n coloré tel que suit :"+str(self.couleurs)

    def aUneCouleurValide(self,position):
        for sommet in range(len(self.mat_adj)-1):
            if self.mat_adj[position][sommet]==1 and self.couleurs[position]==self.couleurs[sommet] : 
                print("les sommets "+str(position)+"("+str(self.couleurs[position])+") et "+str(sommet)+"("+str(self.couleurs[sommet])+") ont la même couleur")
                return False
        return True

    def estValide(self):
        for elem in range(len(self.mat_adj)-1):
            if self.aUneCouleurValide(elem)!=True : return False
        return True

    def changeCouleur(self,position,couleur):
        bisect.insort(self.set_couleurs[position],self.couleurs[position]) # réinsertion de la couleur actuelle dans celles possibles
        self.set_couleurs[position].remove(couleur) # retrait de la nouvelle couleur de celles possibles

        #maj des possibilités de couleur des voisins

        #ajout de la possibilité de l'ancienne couleur
        for pos in range(len(self.mat_adj)-1): # pour chaque voisin
            if self.mat_adj[position][pos]==1 and (not self.couleurs[position] in self.set_couleurs[pos] ):
                peut_avoir_couleur=True # il peut maintenant avoir l'ancienne couleur
                for voisin in range (len(self.mat_adj)-1): # sauf si un autre de ses voisins l'a
                    if ((voisin!=position) and self.mat_adj[pos][voisin]==1 and self.couleurs[voisin]==self.couleurs[position]) : peut_avoir_couleur=False

                if(peut_avoir_couleur) : bisect.insort(self.set_couleurs[pos],self.couleurs[position])

        #retrait de la possibilité de la nouvelle couleur aux voisins
        for pos in range(len(self.mat_adj)-1): # pour chaque voisin
            if self.mat_adj[position][pos]==1 and couleur in self.set_couleurs[pos] :
                self.set_couleurs[pos].remove(couleur)

        #changement de la couleur        
        self.couleurs[position]=couleur

def evalueColoration(coloration):
    comptage=[0]*(max(coloration)+1)
    resultat=0

    for elem in coloration:
        comptage[elem]+=1

    for couleur in range(len(comptage)):
        resultat+=couleur*comptage[couleur]
        
    return resultat