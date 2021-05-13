from random import randint
def comparaison():
    de=randint(1,6)
    if de==5:
        res="Egal"
    elif de<5:
        res="Inférieur"
    else:
        res="Supérieur"
    return res



def produit(n):
    """Cette fonction calcule le produit 1*2*...*n
    n : entier
    p : entier
    """
    p=1
    for facteur in range(2,n+1):
        p=p*facteur
    return p

def montant(n):
    """Calcul le montant du compte au bout de n années.
    n : entier (int)
    m : flottant (float)
    """
    m=5000
    for annee in range(1,n+1):
        m=1.03*m+300
    return m


