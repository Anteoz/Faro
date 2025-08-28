import matplotlib.pyplot as plt
from math import gcd
import plotly.express as px


#Nombres premiers
def erat(n,p): #Liste les nombres premiers et les divise si besoin pour les remettre à l'échelle sur le graphique
    if n<2:
        return None
    V=[True for x in range(n+1)]
    L=[]
    for i in range(2,n+1):
        idx=0
        if V[i]:
            L.append(int(i/p))
            while (idx+i)<len(V):
                idx=idx+i
                V[idx]=False
    return (L)


#Déterminer mélanges
def ordre_multiplicatif(a, m): #Retourne l'ordre multiplicatif de a modulo m
    if gcd(a, m) != 1:
        return None
    k = 1
    var = a % m
    while var != 1:
        var = (var * a) % m
        k += 1
    return k


def nombre_in_shuffles(taille_paquet): #Retourne l'ordre d'un paquet d'une certaine taille
    if taille_paquet % 2 != 0 or taille_paquet < 2:
        raise ValueError("La taille du paquet doit être un nombre pair ≥ 2.")
    modulo = taille_paquet + 1
    return ordre_multiplicatif(2, modulo)


def in_graph(n): #Liste les ordres des tailles de paquet jusqu'à n
    return [nombre_in_shuffles(i) for i in [2 * i for i in range (1,int(n/2)+1)]]


#Indicatrice d'Euler
def euler(n):
    if n == 0:
        return 0
    count = 0
    for k in range(1, n+1):
        if gcd(k, n) == 1:
            count += 1
    return count

def euler_list(n):
    return [euler(i) for i in range(1, n+1)]

#Tracer


def tracer(Taille, p=0, n = False, e = False):
    if p != 0:
        for i in range(1, p + 1):
            plt.plot([0,Taille], [0,int(Taille/i)], linewidth=0.5, color='#a10ff1')
            for j in range(i, p + 1):
                plt.plot([0,Taille], [0,int(i*Taille/j)], linewidth=0.5, color='#0ff168')

    # Nombres premiers
    if n == True:
        plt.plot(erat(Taille,1), erat(Taille,1), color='#f1c40f', marker='.', markersize=1, linestyle='None')

    # Mélanges
    plt.plot([2 * i for i in range(1, int(Taille/2) + 1)], in_graph(Taille), label='In', color='#3498db', marker='.', markersize=1, linestyle='None')
    if e == True:
        # Indicatrice d'Euler
        plt.plot(range(0, Taille), euler_list(Taille), label='Euler φ(n)', color='#e74c3c', marker='none', linewidth = '0.1') #De 0 à Taille pour décaler le graphe vers la gauche puisque nous étudions les in shuffle

    plt.title('Nombre de mélanges en fonction du nombre de cartes')
    plt.xlabel('Nombre de cartes')
    plt.ylabel('Nombre de mélanges')
    plt.legend()
    plt.show()
