sum=0
def suma(N):
    sum=N
    if N==0:
        return sum
    else:
        sum+=N
        N-=1
        suma(N)
    
print(suma(2))
