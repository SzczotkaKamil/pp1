try:
    wprowadzonaIloscLiczb=int(input("Wprowadź dowolną liczbę całkowitą: "))
    for x in range(2,wprowadzonaIloscLiczb+1):
        pomocnicza=0
        for y in range(2,x//2+1):
            if(x%y==0):
                pomocnicza+=1
        if(pomocnicza<=0):
            print(x, end=" ")
except:
    print("Wprowadź liczbę całkowitą.")