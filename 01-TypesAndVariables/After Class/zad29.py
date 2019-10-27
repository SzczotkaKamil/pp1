#importowanie biblioteki random w celu uzycia random.randrange
import random
#Zabezpieczenie przed wyrzuceniem błędu
try:
    x = random.randrange(1,6)
    wprowadzonyInput = int(input ("Podaj, ile oczek kostki wyrzucił komputer: "))
    print(f"Komputer wyrzucił: {x} ")
    if wprowadzonyInput == x:
        print(True)
    else:
        print(False)
except:
        print("Wprowadź cyfrę z przedziału od 1 do 6.")
