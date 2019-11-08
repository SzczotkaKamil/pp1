imiona = ["Janek","Ania","Wojtek","Zosia"]
imie = "Zosia"
def jestImie(imie,imiona):
    pomocnicza = 0
    for x in range(len(imiona)):
        if imie==imiona[x]:
            print("Imiona:",imiona)
            print("Imie:", imie)
            print("Imię zawarte jest w wykazie imion.")
            break
        elif pomocnicza==len(imiona)-1:
            print("Imiona:",imiona)
            print("Imie:", imie)
            print("Imię nie jest zawarte w wykazie imion.")
        else:
            pomocnicza+=1
jestImie(imie,imiona)            