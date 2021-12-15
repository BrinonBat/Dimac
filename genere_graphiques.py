import csv
import matplotlib.pyplot as plt
from statistics import mean

def show_mean(csv_name):
#gather the datas
    with open("resultats/"+csv_name+".csv", 'r+', newline='') as csv_file:
        reader = list(csv.reader(csv_file,delimiter=" "))

        taille_tabou=[]
        courbe=[]

        # ajout, à chaque ligne, de la valeur dans la courbe correspondante
        for row in reader[1:]:
            taille_tabou.append(row[0])
            courbe.append(mean([int(elem[:-2]) for elem in row[1:]]))
    
    #paramètrage du graphique
    plt.plot([int(float(elem)) for elem in taille_tabou],courbe,label="moyenne des valeurs obtenues")
    plt.xlabel("taille_tabou")
    plt.xticks([int(float(elem)) for elem in taille_tabou[::2]])
    plt.ylabel("value")
    plt.grid()
    plt.legend()
    plt.savefig("resultats/"+csv_name+"_mean.png")
    plt.close()

def show(csv_name):
    #gather the datas
    with open("resultats/"+csv_name+".csv", 'r+', newline='') as csv_file:
        reader = list(csv.reader(csv_file,delimiter=" "))

        #récupération des seeds et création d'une courbe par seed
        taille_tabou=[]
        first_line=reader[0]
        courbes=[]
        for seed in first_line[1:]:
            courbes.append([int(seed)])

        # ajout, à chaque ligne, de la valeur dans la courbe correspondante
        for row in reader[1:]:
            taille_tabou.append(row[0])
            for i in range(0,len(row[1:])):
                courbes[i].append(row[i+1])
    
    print(courbes)
    #ajout des courbes au graphique
    for courbe in courbes:
        plt.plot([int(float(elem)) for elem in taille_tabou],courbe[1:],label=str(courbe[0]))

    #paramètrage du graphique
    plt.xlabel("taille_tabou")
    plt.xticks([int(float(elem)) for elem in taille_tabou[::2]])
    plt.ylabel("value")
    plt.grid()
    plt.legend()
    plt.savefig("resultats/"+csv_name+".png")
    plt.close()

show("250.5_min")
show("500.5_min")
show_mean("250.5_min")
show_mean("250.5_max")
show_mean("250.5_rand")
show_mean("500.1_min")
show_mean("500.1_max")
show_mean("500.1_rand")
show_mean("500.5_min")
show_mean("500.5_max")
show_mean("500.5_rand")
show_mean("1000.1_min")
show_mean("1000.1_max")
show_mean("1000.1_rand")
