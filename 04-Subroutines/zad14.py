def sprawdzenieCzyWystepuje(liczba, tablica):
    tmp=0
    for x in range(len(tablica)):
        if liczba==tablica[x]:
            print("Podana liczba występuje w tablicy.")
            tmp +=1
    if tmp==0:
        print("Podana liczba nie występuje w tablicy.")
            
        
        
    
sprawdzenieCzyWystepuje(23,[15, 38, 7, 23, 14])