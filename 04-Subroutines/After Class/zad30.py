import random
tablica=[]
def losowaLiczba(x,y):
    global tablica
    return random.randrange(x,y)
parzyste=0
nieparzyste=0
for x in range(1000):
    pomocnicza=(losowaLiczba(1,51))
    if pomocnicza%2==0:
        parzyste+=1
    elif pomocnicza%2!=0:
        nieparzyste+=1
print("Liczby parzyste wynoszą:",parzyste/10,"%")
print("Liczby nieparzyste wynoszą:",nieparzyste/10,"%")
        
      
