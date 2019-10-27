try:
    suma=0
    srednia=0
    pomocnicza=0
    wprowadzonaLiczba=1
    while wprowadzonaLiczba!=0:
        wprowadzonaLiczba=int(input("Podaj liczbę: "))
        if wprowadzonaLiczba!=0:
            pomocnicza+=1
            suma+=wprowadzonaLiczba
            srednia=suma/pomocnicza
        else:
            break
    print("Liczb: ",pomocnicza)
    print("Suma:",suma)
    print("Średnia:",srednia)
except:
    print("Wprowadzaj tylko liczby całkowite.")
