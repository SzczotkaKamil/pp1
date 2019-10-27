import math
try:
    pozostalaKwota=0
    podanaKwota = int(input("Podaj kwotę w zł: "))
    if podanaKwota>=5:
        liczbaPiecozlotowek = math.floor(podanaKwota/5)
        pozostalaKwota = podanaKwota-liczbaPiecozlotowek*5
        print("Liczba pięciozłotówek:",liczbaPiecozlotowek)
    if pozostalaKwota>=2:
        liczbaDwuzlotowek = math.floor(pozostalaKwota/2)
        pozostalaKwota -= liczbaDwuzlotowek*2
        print("Liczba dwuzłotówek:",liczbaDwuzlotowek)
    if pozostalaKwota==1:
        liczbaZlotowek=1
        print("Liczba złotówek:",liczbaZlotowek)
    if podanaKwota==4:
        print("Liczba dwuzłotówek:",2)
    if podanaKwota==3:
        print("Liczba dwuzłotówek:",1)
        print("Liczba złotówek:",1)
    if podanaKwota==2:
        print("Liczba dwuzłotówek:",1)
    if podanaKwota==1:
        print("Liczba złotówek:",1)
except:
    print("Podaj liczbę całkowitą.")



