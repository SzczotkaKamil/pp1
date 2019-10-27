#Obliczanie pola trójkąta z uzyciem wzoru Herona 
import math
a = float(input("Podaj dlugosc pierwszego boku: "))
b = float(input("Podaj dlugosc drugiego boku: "))
c = float(input("Podaj dlugosc trzeciego boku: "))
p = (a+b+c)/2
wynik = math.sqrt(p*(p-a)*(p-b)*(p-c))
print (f"Pole trójkąta którego boki wynoszą: {a}, {b} i {c} jest równe: {wynik}")
