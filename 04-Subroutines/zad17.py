import random
def rzucKostka():
    x = random.randint(1,6)
    return x
liczba1=rzucKostka()
liczba2=rzucKostka()
liczba3=rzucKostka()
suma = liczba1+liczba2+liczba3
print("Wyrzucone oczka:",liczba1,liczba2,liczba3)
print("Suma: ",suma)

