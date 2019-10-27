try:
    tablica = []
    tablica.append(int(input("Podaj pierwszą liczbę: ")))
    tablica.append(int(input("Podaj drugą liczbę: ")))
    tablica.append(int(input("Podaj trzecią liczbę: ")))
    tablica.sort()
    print("Liczby w kolejności rosnącej:",tablica)
except:
    print("Wprowadź trzy liczby całkowite.")