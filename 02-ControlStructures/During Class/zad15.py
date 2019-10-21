try:
    x = int(input("Podaj liczbę: "))
    for y in range(10):
        wynik = x*(y+1)
        print(f"{x} x {y+1} = {wynik}")
except:
    print("Wprowadź liczbę całkowitą.")