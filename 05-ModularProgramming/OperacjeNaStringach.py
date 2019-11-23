import re
def wspak(tekst):
    tablica=re.findall(".",tekst)
    odwrocone=""
    for x in range(len(tablica)):
        odwrocone+=tablica[len(tablica)-x-1]
    print(odwrocone)
def rozstrzelony(tekst):
    tablica=re.findall(".",tekst)
    rozstrzelone=""
    for x in range(len(tablica)):
        rozstrzelone+=tablica[x]+" "
    print(rozstrzelone)
def duzaLitera(tekst):
    tablica=re.findall(".",tekst)
    rozstrzelone=""
    for x in range(len(tablica)):
        if tablica[x-1]==" ":
            rozstrzelone+=tablica[x].upper()
        elif x==0:
            rozstrzelone+=tablica[x].upper()
        else:
            rozstrzelone+=tablica[x].lower()
    print(rozstrzelone)




