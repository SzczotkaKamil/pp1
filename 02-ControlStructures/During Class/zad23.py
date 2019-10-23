try:
    tablica = ["niedostateczny", "mierny", "dostateczny", "dobry", "bardzo dobry", "celujący"]
    ocena = int(input("Podaj ocenę: "))
    if ocena!=0:
        print("Ocena słownie: ",tablica[ocena-1])
    else:
        print("Wprowadź cyfrę z zakresu 1-6")
except:
    print("Wprowadź cyfrę z zakresu 1-6")