try:
    podanyLimitPredkosci = int(input("Podaj limit prędkości: "))
    podanaPredkosc = int(input("Podaj prędkość pojazdu: "))
    if podanaPredkosc-podanyLimitPredkosci<=0:
        mandat=0
        print("Mandat (zł):",mandat)
    elif podanaPredkosc-podanyLimitPredkosci>0 and podanaPredkosc-podanyLimitPredkosci<=10:
        mandat=(podanaPredkosc-podanyLimitPredkosci)*5
        print("Mandat (zł):",mandat)
    elif podanaPredkosc-podanyLimitPredkosci>10:
        mandat=50+(podanaPredkosc-10-podanyLimitPredkosci)*15
        print("Mandat (zł):",mandat)
except:
    print("Wprowadź dwie liczby całkowite.")