with open('C:/Users/s-115-28/Desktop/pp1/03-FileHandling/numbers.txt','r') as file: 
    wynik = 0
    for line in file:
        wynik+=int(line)
    print("Wynik wynosi:",wynik)
        