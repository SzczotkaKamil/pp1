wynik=0
def suma(N):
    global wynik
    if N==0:
        return wynik
    else:
        wynik+=N
        N-=1
        return suma(N)
    
print(suma(500))
