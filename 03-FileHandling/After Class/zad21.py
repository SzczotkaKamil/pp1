import re
liczby = []
with open("C:/Users/pc/Desktop/pp1/03-FileHandling/numbersinrows.txt","r") as file:
    for line in file:
        cos = re.findall(r"\d+",line)
        for x in range(len(cos)):
            liczby.append(cos[x])
print("Liczb w pliku: ",len(liczby))
suma = 0
for y in range(len(liczby)):
    suma+= int(liczby[y])
print("Suma liczb z pliku",suma)
    