def maxi(a,b):
    """Renvoi le plus grand des deux nombres a,b -> flottant(float)
    Renvoi flottant"""

    if a>b:
        return a
    else:
        return  b


def maxi(a,b,c):
    if a>=b:
        return a
    if b>=c:
        return b
    else:
        return c


def f(x):
    if x>=30:
        resultat=x-10
    if x<30:
        x=x+10
    return x


