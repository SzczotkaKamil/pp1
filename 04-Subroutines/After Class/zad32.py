import array
macierz = [[1,2,3],[0,0,3],[5,1,1]]
transpozycjaMac = []

def transpozycja(macierz):
    global transpozycjaMac
    for x in range (len(macierz)):
        pomocnicza = []
        for y in range(len(macierz[x])):
            pomocnicza.append(macierz[y][x])
        transpozycjaMac.insert(x,pomocnicza)
    return transpozycjaMac


(transpozycja(macierz))
print("Macierz:")
for x in range (len(macierz)):
    print (macierz[x])
print("Macierz transponowana:")
for x in range (len(macierz)):
    print (transpozycjaMac[x])


