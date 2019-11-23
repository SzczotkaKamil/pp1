import csv
def wielkoscKolumny(slowo):
    rozmiar=len(slowo)
    pomocnicza=""
    for x in range(15): #upewnia się, że każda kolumna ma rozmiar 15 znaków
        if rozmiar<x:
            pomocnicza+=" "
    return slowo+pomocnicza
with open('employees.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    header = next(reader)
    linia=""
    for y in range(90):
        linia+="="
    print(wielkoscKolumny("#"),wielkoscKolumny(header[0]).upper(),wielkoscKolumny(header[1]).upper(),wielkoscKolumny(header[2]).upper(),wielkoscKolumny(header[3]).upper())
    x = 1
    print(linia)
    for row in reader:
        print(wielkoscKolumny(str(x)),wielkoscKolumny(row[0]).upper(),wielkoscKolumny(row[1]),wielkoscKolumny(row[2]),wielkoscKolumny(row[3]))
        x+=1
