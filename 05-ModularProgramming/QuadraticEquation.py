import math
def czytajWspolczynniki():
    global wspolczynniki
    a = float(input("Podaj wspolczynnik a:"))
    b = float(input("Podaj wspolczynnik b:"))
    c = float(input("Podaj wspolczynnik c:"))    
    wspolczynniki=[a,b,c]
    return wspolczynniki
# oblicz deltę
def obliczDelte(wspolczynniki):
    global delta
    delta = wspolczynniki[1]*wspolczynniki[1]-(4*wspolczynniki[0]*wspolczynniki[2])
    return delta
def obliczPierwiastki(wspolczynniki):
    if delta>0:
        global pierwiastki
        x1=((-wspolczynniki[1]-math.sqrt(delta))/(2*wspolczynniki[0]))
        x2=((-wspolczynniki[1]+math.sqrt(delta))/(2*wspolczynniki[0]))
        pierwiastki=[x1,x2]
        return pierwiastki
    elif delta==0:
        x0=(-wspolczynniki[1]/(2*wspolczynniki[0]))
        pierwiastki=[x0]
        return pierwiastki
    else:
        pierwiastki=[]
        return pierwiastki
def wyswietlPierwiastki(pierwiastki):
    if len(pierwiastki)>1:
        print(f"Równanie kwadratowe postaci:{wspolczynniki[0]}x^2+({wspolczynniki[1]}x)+({wspolczynniki[2]})")
        print("Pierwiastki równania:",pierwiastki[0], end=" ")
        print(",",pierwiastki[1])
    elif len(pierwiastki)==1:
        print(f"Równanie kwadratowe postaci:{wspolczynniki[0]}x^2+({wspolczynniki[1]}x)+({wspolczynniki[2]})")
        print("Pierwiastek równania:",pierwiastki[0], end=" ")
    else:
        print(f"Równanie kwadratowe postaci:{wspolczynniki[0]}x^2+({wspolczynniki[1]}x)+({wspolczynniki[2]})")
        print("Delta ujemna.")
        