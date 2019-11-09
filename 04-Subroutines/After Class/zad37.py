tablica = [1,3,5,3,2,7,2,1,3,77,5]
pojedyncze = []
def czyPowtarza(tablica):
    global pojedyncze
    pomocnicza = 0
    for i in range(len(tablica)):
        for j in range(len(tablica)):
            if tablica[i]==tablica[j]:
                pomocnicza+=1
        if pomocnicza<2:
            pojedyncze.append(tablica[i])
        pomocnicza=0
czyPowtarza(tablica)
print(f"Liczby z tablicy {tablica} które się nie powtarzają to: {pojedyncze}")