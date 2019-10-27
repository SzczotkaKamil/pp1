import math
try:
    a = float(input("Wprowadź wartość a: "))
    b = float(input("Wprowadź wartość b: "))
    c = float(input("Wprowadź wartość c: "))
    delta = b*b - (4*a*c)
    if delta>0:
        x1=(-b-math.sqrt(delta)/2*a)
        x2=(-b+math.sqrt(delta)/2*a)
        print("Pierwszym miejscem zerowym jest:",x1)
        print("Drugim miejscem zerowym jest:",x2)
        
    elif delta==0:
        x0=-b/(2*a)
        print("Miejscem zerowym jest:",x0)
    else:
       print("Nie ma miejsc zerowych.") 
except:
    print("Wprowadź pod zmienne a,b oraz c liczby rzeczywiste.")