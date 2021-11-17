# nom_fic : string
# mat_adj : list<list<bool>> matrice d'adjacence du graphe
# couleurs: list<int>, meilleure coloration jusqu'à maintenant
# nb_couleurs: int
from os import remove


class Graphe:
    def __init__(self,fic):
        self.nom_fic=fic

        #génération de la matrice d'adjacence
        g=open('D_graphes/'+fic,'r')
        for li in g:
            elems=li.split()
            if(elems[0]=='p'): 
                self.mat_adj=[]
                for li in range(int(elems[2])+1):
                    ligne=[]
                    for col in range(int(elems[2])+1):
                        ligne.append(0)
                    self.mat_adj.append(ligne)

                #self.mat_adj=[([0]*(int(elems[2])+1))]*(int(elems[2])+1) # création d'une matrice de 0
            elif(elems[0]=='e'): 
                self.mat_adj[int(elems[2])][int(elems[1])]=1 # place un 1 dans la case correspondante


        #print(self.mat_adj)
        #première coloration par algo glouton
        self.set_couleurs=[[1]]
        for i in range (len(self.mat_adj)):
            self.set_couleurs.append([1])
        self.nb_couleurs=1
        self.couleurs=[]
        for sommet in range(len(self.mat_adj)):

            #print(self.set_couleurs)

            #print("set couleurs["+str(sommet)+"]:"+str(self.set_couleurs[sommet]))
            if(self.set_couleurs[sommet]==[]):
            #    print("IS IN")
                self.nb_couleurs+=1
                for suivant in range(sommet,(len(self.mat_adj)-1)):
                    self.set_couleurs[suivant].append(self.nb_couleurs)
            #print(self.set_couleurs[sommet])
            self.couleurs.append(self.set_couleurs[sommet][0])
            #print("mat adj :"+str(self.mat_adj[sommet]))

            print(self.couleurs)

            for suivant in range(sommet+1,(len(self.mat_adj)-1)):
                #print(str(suivant) +" a une adj de "+ str(self.mat_adj[sommet][suivant]))
                if self.mat_adj[sommet][suivant]==1:
                    #print("OK2")
                    #print("set_couleurs["+str(suivant)+"] :"+str(self.set_couleurs[suivant]))
                    #print("couleurs["+str(sommet)+"] :"+str(self.couleurs[sommet]))
                    #print(self.set_couleurs)
                    if self.couleurs[sommet] in self.set_couleurs[suivant]: self.set_couleurs[suivant].remove(self.couleurs[sommet])

  
    
    def __str__(self):
        return "\n graphe du fichier "+self.nom_fic+"\n coloré tel que suit :"+str(self.couleurs)

    def aUneCouleurValide(self,position):
        for sommet in range(len(self.mat_adj)-1):
            if self.mat_adj[position][sommet]==1 and self.couleurs[position]==self.couleurs[sommet] : return False
        return True

    def changeCouleur(self,position):
        pass


def evalueColoration(coloration):
    comptage=[0]*(max(coloration)+1)
    resultat=0

    for elem in coloration:
        comptage[elem]+=1

    print(" compatage elems : "+str(comptage))

    for couleur in range(len(comptage)):
        print(couleur)
        resultat+=couleur*comptage[couleur]
        
    return resultat