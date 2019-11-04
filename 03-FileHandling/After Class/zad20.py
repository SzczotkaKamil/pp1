liczby = []
with open('C:/Users/Kamil/Desktop/pp1/03-FileHandling/numbers.txt','r') as file: 
    for line in file:
        liczby.append(int(line))
with open('C:/Users/Kamil/Desktop/pp1/03-FileHandling/During Class/evennumbers.txt','w+') as f:
    for x in range(len(liczby)):
        if liczby[x]%2==0:
            liczbaParzysta=str(liczby[x])+"\n"
            f.write(liczbaParzysta)
