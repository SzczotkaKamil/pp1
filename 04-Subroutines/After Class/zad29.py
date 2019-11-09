import statistics
tablica = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
def mediana(tablica):
    return statistics.median(tablica)


def dominanta(tablica):
    most = max(list(map(tablica.count, tablica)))
    return list(set(filter(lambda x: tablica.count(x) == most, tablica)))
    
    
        
print("Medianą podanego zbioru jest:",mediana(tablica))
print("Dominantą podanego zbioru jest:",dominanta(tablica))