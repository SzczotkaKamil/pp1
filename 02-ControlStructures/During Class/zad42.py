try:
    licznik = float(input("Podaj licznik: "))
    mianownik = float(input("Podaj mianownik: "))
    if mianownik!=0:
        wynik=licznik/mianownik
        print("Licznik:",licznik)
        print("Mianownik:",mianownik)
        print("Wynik z dzielenia:",wynik)
    else:
        print("Nie dziel przez 0!")
except:
    print("Wprowadź liczby rzeczywiste.")