x = int(input("Wprowadź pierwszą liczbę: "))
y = int(input("Wprowadź drugą liczbę: "))
if x<0 or y<0:
    print(f"Jedna z liczb {x} lub {y} jest ujemna.")
else:
    print(f"Żadna z liczb {x} lub {y} nie jest ujemna.")