def suma(tablica):
    suma =0
    print("Tablica: ",end=" ")
    for x in range(len(tablica)):
        suma+=tablica[x]
        print(tablica[x], end=" ")
    print()
    print("Suma:",suma)
    return suma


suma([4,3,7,1,3])