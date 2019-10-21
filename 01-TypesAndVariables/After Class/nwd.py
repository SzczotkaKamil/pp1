import math
try:
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    wynik = math.gcd(a,b)
    if a>0 and b>0:
        print(f"Największy wspólny dzielnik liczb {a} i {b}, wynosi: {wynik}")
    else:
        print("Podaj liczby całkowite dodatnie.")
except:
    print("Podaj liczby całkowite dodatnie.")