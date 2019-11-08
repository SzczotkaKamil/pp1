jezyki = ["Java","Python","JavaScript","C++","C#","Ruby","Perl","PHP","C","Android"]
wartosci = [61,47,37,32,26,18,14,14,9,7]
def rysujWykres(jezyki,wartosci):
    
    for x in range (len(jezyki)):
        pomocnicza = ""
        print(jezyki[x],end=": ")
        for y in range(round(wartosci[x]/3)):
            pomocnicza+="#"
        print(pomocnicza)
rysujWykres(jezyki,wartosci)
            
