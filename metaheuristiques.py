import random
import Graphe
import numpy as np
def recuitSimule(graphe):
    pass

#garde une structure de la forme [[indice,ancienne_val]]
def tabu(graphe,duree_tabou,nb_iter):
    parcours=[]
    liste_tabou=np.zeros(shape=(len(graphe.mat_adj),graphe.nb_couleurs+1))
    #initialisation
    for iter in range(0,nb_iter):
        print("deb")
        min_val=9999999
        #on itère une fois pour chaque élément de la liste
        for pos in range(len(graphe.mat_adj)):
            #changement de couleur
            if graphe.set_couleurs[pos]==[] : continue

            #récupération des différentes couleurs pouvant être appliquées
            couleurs=[]
            for coul in graphe.set_couleurs[pos]:
                if(iter>=liste_tabou[pos,coul]):
                    couleurs.append(coul)
            if(len(couleurs)>=1): nouv_couleur=couleurs[0]
            else:continue

            #calcul de la valeure finale
            val=nouv_couleur-graphe.couleurs[pos]
            if val<min_val : # si elle est meilleure que la solution actuelle, on la remplace
                min_val=val
                suivante=[[pos,nouv_couleur]]
            elif val==min_val : # si elle est identique, on la sauvegarde pour une sélection aléatoire
                suivante.append([pos,nouv_couleur])
            else :
                pass
            #annulation de la modification
        
        #application de la modification du meilleur voisin
        if(len(suivante)>1): select=random.randrange(0,len(suivante)-1)
        else : select=0
        ancienne_couleur=graphe.couleurs[suivante[select][0]]
        ancien_score=Graphe.evalueColoration(graphe.couleurs)
        graphe.changeCouleur(suivante[select][0],suivante[select][1]) #[position,couleur]
        liste_tabou[suivante[select][0],suivante[select][1]]=iter+duree_tabou
        value=Graphe.evalueColoration(graphe.couleurs)
        parcours.append([suivante[select][0],ancienne_couleur,ancien_score])
        print("suivante : "+str(suivante[select]))
        print(" iteration "+str(iter)+": "+str(value))
        suivante=[]


    #récupération du meilleur graphe trouvé
    #trouve le meilleur graphe
    position=0
    print(parcours)
    for i in range(1,nb_iter):
        coup=parcours[-i]  #[position,ancienne_couleur,ancien_score]
        if(coup[2]<value):
            print(" actual value is "+str(value)+" tested value is "+str(coup[2]))
            value=coup[2]
            position=i
    #le regénére si besoin
    if(position>0):
        print("entered")
        for i in range(1,position+1):
            coup=parcours[-i]
            graphe.changeCouleur(coup[0],coup[1])
    graphe.nb_couleurs=max(graphe.couleurs)
    pass


#garde une structure de la forme [[indice,ancienne_val]]
def tabu_propa(graphe,duree_tabou):
    #initialisation
    parcours=[]
    for iter in range(0,100):
        min_val=9999999
        #on itère une fois pour chaque élément de la liste
        for pos in range(len(graphe.mat_adj)):
            #changement de couleur
            anc_couleur=graphe.couleurs[pos]
            if graphe.set_couleurs[pos]==[] : continue
            nouv_couleur=graphe.set_couleurs[pos][0]
            graphe.changeCouleur(pos,nouv_couleur)
            

            if len(parcours)>=duree_tabou:
                #si la couleur n'est pas valide
                while ((not graphe.estValide()) or [pos,nouv_couleur] in parcours[-duree_tabou:]):
                    #annule la modification
                    graphe.changeCouleur(pos,anc_couleur)

                    #en effectue une nouvelle
                    nouv_couleur=random.sample(graphe.set_couleurs[pos],1)[0]
                    #print(graphe.set_couleurs[pos])
                    #print(nouv_couleur)
                    graphe.changeCouleur(pos,nouv_couleur)
            else:
                #si la couleur n'est pas valide
                while ((not graphe.estValide()) or [pos,nouv_couleur] in parcours):
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