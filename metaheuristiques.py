import random
import Graphe

def recuitSimule(graphe):
    pass

#garde une structure de la forme [[indice,ancienne_val]]
def tabou(graphe,taille_liste):
    #initialisation
    parcours=[]
    for iter in range(0,300):
        min_val=9999999
        suivante=[]
        #on itère une fois pour chaque élément de la liste
        for pos in range(len(graphe.mat_adj)):
            #changement de couleur
            anc_couleur=graphe.couleurs[pos]
            if graphe.set_couleurs[pos]==[] : continue
            nouv_couleur=graphe.set_couleurs[pos][0]
            graphe.changeCouleur(pos,nouv_couleur)
            

            if len(parcours)>=taille_liste:
                #si la couleur n'est pas valide
                while ((not graphe.estValide()) or [pos,nouv_couleur] in parcours[-taille_liste:]):
                    #annule la modification
                    graphe.changeCouleur(pos,anc_couleur)

                    #en effectue une nouvelle
                    nouv_couleur=random.sample(graphe.set_couleurs[pos],1)[0]
                    #print(graphe.set_couleurs[pos])
                    #print(nouv_couleur)
                    graphe.changeCouleur(pos,nouv_couleur)

            #calcul de la valeure finale
            #print("position "+str(pos)+" : "+str(anc_couleur)+"-->"+str(nouv_couleur))
            val=Graphe.evalueColoration(graphe.couleurs)
            if val<min_val : # si elle est meilleure que la solution actuelle, on la remplace
                #print(str(val)+" remplace l'ancienne value "+str(min_val))
                min_val=val
                suivante=[[pos,nouv_couleur]]
            elif val<=min_val : # si elle est identique, on la sauvegarde pour une sélection aléatoire
                suivante.append([pos,nouv_couleur])
                #print(str(val)+" ajouté aux suivants possibles "+str(suivante))
            else :
                pass
            #annulation de la modification
            graphe.changeCouleur(pos,anc_couleur)
        
        #application de la modification du meilleur voisin
        if(len(suivante)>1): select=random.randrange(0,len(suivante)-1)
        else : select=0
        graphe.changeCouleur(suivante[select][0],suivante[select][1])
        print("suivante : "+str(suivante[select]))
        parcours.append(suivante[select])
        suivante=[]
        print(" iteration "+str(iter)+": "+str(Graphe.evalueColoration(graphe.couleurs)))

    graphe.nb_couleurs=max(graphe.couleurs)
    pass