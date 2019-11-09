import re
string = "Kamil Szczotka Uniwerstet Ekonomiczny w KRAKOWIE."
def czyDuzeLitery(string):
    global pomocnicza,wynik
    pomocnicza=re.findall("[A-Z]",string)
    wynik = ""
    for x in range(len(pomocnicza)):
        wynik+=pomocnicza[x]
        
czyDuzeLitery(string)

print(f'W ciągu znaków "{string}", występują następujące wielkie litery:',wynik)

