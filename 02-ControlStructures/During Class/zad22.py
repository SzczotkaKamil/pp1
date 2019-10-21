suma = 0
dzielnik=0
tablica = [15,8,31,47,2,19]
for y in tablica:
    if y%2!=0:
       suma = suma+y
       dzielnik=dzielnik+1
    
print(f"Średnia arytmetyczna liczb nieparzystych z tablicy wynosi: {suma/dzielnik}")