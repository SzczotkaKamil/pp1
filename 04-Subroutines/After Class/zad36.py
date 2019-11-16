tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]
def Suma(tab):
    suma =0
    for x in tab:
        if isinstance(x, int)==True:
            suma+=x
        else:
            suma+=(Suma(x))
    return suma
print(Suma(tab))