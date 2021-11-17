import random
import Graphe

def recuitSimule(graphe):
    pass

#garde une structure de la forme [[indice,ancienne_val]]
def tabou(graphe):
    #initialisation
    parcours=[]
    for iter in range(0,300):
        print(" iteration "+str(iter)+": "+str(Graphe.evalueColoration(graphe.couleurs)))
        min_val=9999999
        suivante=[]
        #on itère une fois pour chaque élément de la liste
        for pos in range (len(graphe.mat_adj)):

            #changement de couleur
            anc_couleur=graphe.couleurs[pos]
            if graphe.set_couleurs[pos]==[] : break
            nouv_couleur=graphe.set_couleurs[pos][0]
            graphe.changeCouleur(pos,nouv_couleur)
            

            if len(parcours)>=2:
                #si la couleur n'est pas valide
                while ((not graphe.estValide()) or [pos,nouv_couleur] in parcours[-2:]):
                    #annule la modification
                    graphe.changeCouleur(pos,anc_couleur)

                    #en effectue une nouvelle
                    nouv_couleur=random.sample(graphe.set_couleurs[pos],1)[0]
                    #print(graphe.set_couleurs[pos])
                    #print(nouv_couleur)
                    graphe.changeCouleur(pos,nouv_couleur)

            #calcul de la valeure finale
            val=Graphe.evalueColoration(graphe.couleurs)
            if val<min_val :
                min_val=val
                suivante=[pos,nouv_couleur]
        
            #annulation de la modification
            graphe.changeCouleur(pos,anc_couleur)

        #application de la modification du meilleur voisin
        print("suivante : "+str(suivante))
        graphe.changeCouleur(suivante[0],suivante[1])
        parcours.append(suivante)
        suivante=[]
    graphe.nb_couleurs=max(graphe.couleurs)
    pass