# nom_fic : string
# graphe : list<list<bool>>
# couleurs: list<int>
# nb_couleurs: int
class Graphe:
    def __init__(self,fic):
        nom_fic=fic
        #génération du graphe
        g=open('D_graphes/'+fic,'r')
        for li in g:
            elems=li.split()
            if(elems[0]=='p'): graphe=[[0]*elems[2]]*elems[2]
            elif(elems[0]=='e'):graphe[elems[1]][elems[2]]=1

        self.couleurs=[]
        self.nb_couleurs=0
    
    def __str__(self):
        return "\n graphe du fichier "+self.nom_fic+"\n "+str(self.graphe)+"\n coloré tel que suit :"+str(self.couleurs)

    


