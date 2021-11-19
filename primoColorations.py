import random

def gloutonMin(graphe):
    #donne 1 comme couleur possible à tous
    graphe.set_couleurs=[[1]]
    for i in range (len(graphe.mat_adj)):
        graphe.set_couleurs.append([1])
    graphe.nb_couleurs=1
    graphe.couleurs=[]
    for sommet in range(len(graphe.mat_adj)):
        #cas de sommet sans couleur disponible
        if(graphe.set_couleurs[sommet]==[]):
            #on créée une couleur supplémentaire, que l'on ajoute aux possibilités des autres sommets
            graphe.nb_couleurs+=1
            for suivant in range(len(graphe.mat_adj)-1):
                graphe.set_couleurs[suivant].append(graphe.nb_couleurs)
        #attribution de la couleur
        graphe.couleurs.append(graphe.set_couleurs[sommet][0])
        graphe.set_couleurs[sommet].remove(graphe.set_couleurs[sommet][0])

        for suivant in range((len(graphe.mat_adj)-1)):
            if graphe.mat_adj[sommet][suivant]==1:
                if graphe.couleurs[sommet] in graphe.set_couleurs[suivant]: graphe.set_couleurs[suivant].remove(graphe.couleurs[sommet])

def gloutonMax(graphe):
    #donne 1 comme couleur possible à tous
    graphe.set_couleurs=[[1]]
    for i in range (len(graphe.mat_adj)):
        graphe.set_couleurs.append([1])
    graphe.nb_couleurs=1
    graphe.couleurs=[]
    for sommet in range(len(graphe.mat_adj)):
        #cas de sommet sans couleur disponible
        if(graphe.set_couleurs[sommet]==[]):
            #on créée une couleur supplémentaire, que l'on ajoute aux possibilités des autres sommets
            graphe.nb_couleurs+=1
            for suivant in range(len(graphe.mat_adj)-1):
                graphe.set_couleurs[suivant].append(graphe.nb_couleurs)
        #attribution de la couleur
        taille=len(graphe.set_couleurs[sommet])-1
        graphe.couleurs.append(graphe.set_couleurs[sommet][taille])
        graphe.set_couleurs[sommet].remove(graphe.set_couleurs[sommet][taille])

        for suivant in range((len(graphe.mat_adj)-1)):
            if graphe.mat_adj[sommet][suivant]==1:
             if graphe.couleurs[sommet] in graphe.set_couleurs[suivant]: graphe.set_couleurs[suivant].remove(graphe.couleurs[sommet])

def numSommet(graphe):
    #première coloration par une couleur par sommet
    graphe.set_couleurs=[]
    for i in range (len(graphe.mat_adj)):
        graphe.set_couleurs.append([])
    graphe.couleurs=[]
    for sommet in range(len(graphe.mat_adj)):
        graphe.couleurs.append(sommet)
        for suivant in range((len(graphe.mat_adj)-1)):
            if graphe.mat_adj[sommet][suivant]!=1:
                graphe.set_couleurs[suivant].append(sommet)
        graphe.nb_couleurs=max(graphe.couleurs)

        for suivant in range((len(graphe.mat_adj)-1)):
                if graphe.mat_adj[sommet][suivant]==1:
                    if graphe.couleurs[sommet] in graphe.set_couleurs[suivant]: graphe.set_couleurs[suivant].remove(graphe.couleurs[sommet])

def aleatoire(graphe,seed): 
    random.seed(seed)
    graphe.set_couleurs=[[1]]
    for i in range (len(graphe.mat_adj)):
        graphe.set_couleurs.append([1])
    graphe.nb_couleurs=1
    graphe.couleurs=[]
    for sommet in range(len(graphe.mat_adj)):
        #cas de sommet sans couleur disponible
        if(graphe.set_couleurs[sommet]==[]):
            #on créée une couleur supplémentaire, que l'on ajoute aux possibilités des autres sommets
            graphe.nb_couleurs+=1
            for suivant in range(len(graphe.mat_adj)-1):
                graphe.set_couleurs[suivant].append(graphe.nb_couleurs)
        #attribution de la couleur
        if len(graphe.set_couleurs[sommet])>1 : indice=random.randrange(0,len(graphe.set_couleurs[sommet])-1)
        else : indice=0
        graphe.couleurs.append(graphe.set_couleurs[sommet][indice])
        graphe.set_couleurs[sommet].remove(graphe.set_couleurs[sommet][indice])

        for suivant in range((len(graphe.mat_adj)-1)):
            if graphe.mat_adj[sommet][suivant]==1:
             if graphe.couleurs[sommet] in graphe.set_couleurs[suivant]: graphe.set_couleurs[suivant].remove(graphe.couleurs[sommet])


    pass