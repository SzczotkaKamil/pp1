import re
pom=0
def sumaCyfr(liczba):
    global pom,licznik,wynik,cyfry
    if pom==0:
        cyfry=re.findall("\d",liczba)
        wynik=0
        licznik = 0
        pom+=1
    if licznik<len(cyfry):
        wynik+=int(cyfry[licznik])
        licznik+=1 
        return sumaCyfr(liczba)
    else:
        return wynik

print(sumaCyfr(str(120023)))
