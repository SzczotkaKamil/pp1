import statistics
try:
    mediana=[]
    liczba1 = int(input("Podaj pierwszą liczbę: "))
    liczba2 = int(input("Podaj drugą liczbę: "))
    liczba3 = int(input("Podaj trzecią liczbę: "))
    mediana.append(liczba1)
    mediana.append(liczba2)
    mediana.append(liczba3)
    print(f"Medianą liczb {liczba1}, {liczba2} i {liczba3} jest:",statistics.median(mediana))
except:
    print("Podaj liczby całkowite.")