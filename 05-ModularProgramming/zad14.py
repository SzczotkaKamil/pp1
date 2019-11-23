import csv
import statistics
wiek=[]
with open('employees.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        wiek.append(row['age'])
wiekInt=[]

for x in range(len(wiek)):
    wiekInt.append(int(wiek[x]))
print(wiek)
mediana = statistics.median(wiekInt)
suma=0
odchylenie = statistics.stdev(wiekInt)
for y in range(len(wiekInt)):
    suma+=wiekInt[x]
srednia=suma/len(wiekInt)
print("Tablica z wiekiem wszystkich pracowników:",wiekInt)
print("Mediana wynosi:",mediana)
print("Średnia wynosi:",srednia)
print("Odchylenie standardowe wynosi:",odchylenie)
