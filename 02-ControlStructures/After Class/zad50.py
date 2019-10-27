import math
try:
    podanaLiczbaDziesietna = int(input("Podaj dowolną liczbę całkowitą w systemie dziesiętnym: "))
    i=podanaLiczbaDziesietna*2
    zapisBinarnyLiczby=""
    while i>1:
        i-=math.ceil(i/2)
        if float(i/2)==math.ceil(i/2):
            zapisBinarnyLiczby+="0"
        else:
            zapisBinarnyLiczby+="1"
    zapisBinarnyLiczby=zapisBinarnyLiczby[::-1]
    print(f"Liczba {podanaLiczbaDziesietna} w systemie dwójkowym ma postać: ",zapisBinarnyLiczby)
except:
    print("Podaj liczbę całkowitą.")