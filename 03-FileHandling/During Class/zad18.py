liczby = []
with open("C:/Users/Kamil/Desktop/pp1/03-FileHandling/numbers.txt","r") as file:
    for line in file:
        liczby.append(int(line))
liczby.sort()
print(liczby)