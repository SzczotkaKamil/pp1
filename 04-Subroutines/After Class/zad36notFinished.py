tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]
licznik,wynik,wynikPomocniczy=0,0,0
def sumowanieTablicy(tablica):
    global licznik,wynikPomocniczy
    if licznik<len(tablica):
        wynikPomocniczy+=tablica[licznik]
        licznik+=1
        return sumowanieTablicy(tablica)
    else:
        return wynikPomocniczy
        licznik,wynik=0,0
        
print(sumowanieTablicy([1,5,3,2,1]))

def sumowanieWielowymiarowej(tab):
    global wynik,licznik
    if licznik<len(tab) and isinstance(tab[licznik],int)==False:
        wynik+=sumowanieTablicy(tab[licznik])
        licznik+=1
        return sumowanieWielowymiarowej(tab)
    elif licznik<len(tab):
        wynik+=tab[licznik]
        licznik+=1
        return sumowanieWielowymiarowej(tab)
    else:
        return wynik
print(sumowanieWielowymiarowej(tab))