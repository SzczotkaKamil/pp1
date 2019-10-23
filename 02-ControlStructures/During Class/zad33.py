try:
    cyfrySlownie = ["zero","jeden","dwa","trzy","cztery","pięć","sześć","siedem","osiem","dziewięć"]
    podanaLiczbaNaturalna = input("Podaj dowolną liczbę naturalną: ")
    podanaLiczbaNaturalnaString = " ".join(podanaLiczbaNaturalna)
    podanaLiczbaNaturalnaTablica = podanaLiczbaNaturalnaString.split(" ")
    wynik = ""
    for x in range(len(podanaLiczbaNaturalna)):
        wynik+=cyfrySlownie[int(podanaLiczbaNaturalnaTablica[x])]
        wynik+=" "
    print(wynik)
except:
    print("Program obsługuje jedynie liczby naturalne.")