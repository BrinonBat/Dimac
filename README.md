# SumCOL
Résolution du problème sumCOL sur des graphes Dimacs. 
Le but est de trouver une coloration de graphe minimisant la somme du produit de chaque couleur avec le nombre de sommets qui lui sont attribués 

### Tests de la recherche tabou
Des tests automatiques sont en place. Par défaut, on effectuel es tests sur les deux fichiers DSCJ500.1 et DSCJ250.5.
La liste tabou a une taille allant de 0 à la moitié de la taille du graphe, avec un pas de 10.
le nombre d'itérations par défaut est de 2000
10 seeds sont fournies en dur au début du main.py. Il est possible d'en ajouter ou d'en retirer en dur sans casser l'algorithme.


### TODO list
 - [x] modélisation du problème 
 - [x] lecture de graphs à partir du fichier
 - [x] ajout d'une primo-coloration du graphe
 - [x] premier algo tabou
 - [x] ajout d'un fichier avec les primo-colorations
 - [x] optimiser l'algo et la modélisation à l'aide de quelques articles
 - [x] ajout d'une seed pour le random
 - [ ] sélection automatique de l'algo de primo-coloration
 - [x] sauvegarde des résultats dans des fichiers csv
 - [x] génération de graphiques pour visualiser
 - [ ] renseignement sur les méthodes mises en place pour la résolution du problème
 - [ ] ~~algo recuit simulé pour comparer les résultats~~
