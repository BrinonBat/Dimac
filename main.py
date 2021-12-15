import Graphe,metaheuristiques,time,random,csv
import numpy as np

lancer_serie=True
nb_iter=1000

#lancement en série ou unitaire
if(lancer_serie):
    li_primo_colo=["min","max","rand"] # différents choix de coloration
    seeds=[10101860,8456974,478512365,452595,12541255878,4457963284,11458779653,1254,2688795413,22051998]
    liste_graphes=["DSJC250.5","DSJC500.1","DSJC500.5","DSJC1000.1"]
    #pour chaque fichier
    for nom_graphe in liste_graphes:

        #création de la matrice stockant les résultats
        size=int(nom_graphe[4:-2])
        indices=np.arange(0,int(size/2),10)
        results=np.zeros(shape=(len(indices),len(seeds)))
        for primo_colo in li_primo_colo:

            #récupération des seeds et lancement
            for seed_num in range(0,len(seeds)): #on procède ainsi car on stocke le seed_num dans la matrice de résultats
                random.seed(seeds[seed_num])
                for indice_num in range(0,len(indices)):
                    taille_liste=indices[indice_num] #de même que pour le seed_num
                    #premiere coloration
                    graphe=Graphe.Graphe(nom_graphe,primo_colo)

                    duree=time.time() #lancement du timer

                    #lancement de l'algo
                    metaheuristiques.tabu(graphe,taille_liste,nb_iter,False)
                    results[indice_num,seed_num]=Graphe.evalueColoration(graphe.couleurs)
                    end=time.time()
                    duree=(end-duree)
                    print("graphe "+nom_graphe+" pour la seed "+str(seeds[seed_num])+" avec une liste tabou de taille "+str(taille_liste)+" terminé en: "+str(duree)+" secondes")
            
            #enregistrement dans le fichier correspondant
            nom_fichier="resultats/"+nom_graphe[4:]+"_"+primo_colo+".csv"
            with open(nom_fichier,"w",newline='') as file:
                csv_writer = csv.writer(file, delimiter=' ',dialect='unix',quoting=csv.QUOTE_NONE)

                #ecriture de la première ligne
                first_line=["taille_tabou"]+seeds
                csv_writer.writerow(first_line)

                #écriture des résultats
                save=np.c_[indices,results]
                for i in range(0,len(results)):
                    print(save[i])
                    csv_writer.writerow(save[i])

else:
    #séléction manuelle des paramètres
    seed=10101860
    nom_graphe="DSJC1000.1"
    taille_liste=160
    nb_iter=15000
    verbose=True
    primo_colo="min"
    #seed le random
    random.seed(seed)

    #premiere coloration
    graphe=Graphe.Graphe(nom_graphe,primo_colo)
    print(graphe.nb_couleurs)
    print("coloration graphe "+str(Graphe.evalueColoration(graphe.couleurs)))

    #lancement de l'algo
    duree=time.time()
    metaheuristiques.tabu(graphe,taille_liste,nb_iter,verbose)
    end=time.time()
    duree=(end-duree)

    #affichage du résultat
    print(graphe)
    print("Le graphe contient "+str(graphe.nb_couleurs)+" couleurs")
    print("graphe est valide ? "+str(graphe.estValide()))
    print("son score est de "+str(Graphe.evalueColoration(graphe.couleurs)))
    print("durée totale d'exécution:"+str(duree))