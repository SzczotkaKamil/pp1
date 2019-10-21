# definiowanie tablicy przy uzyciu tablica = []
tablica = [12,6,4,9,3]
# korzystanie z dwóch pętli for w celu wyświetlenia rezultatu
#pierwszy for przejeżdża przez każdy element tablicy
#drugi for dodaje do zmiennej tmp "*" tyle razy ile wynosi liczba w tablicy 
for x in tablica:
# zdefiniowanie zmiennej tmp i nadanie jej wartości "x: ", gdzie x to okreslony element z tablicy
    tmp = f"{x}: "
    for y in range(x):
        tmp = tmp+"*"
#wyświetlenie wartości tmp dla każdego elementu tablicy
    print(tmp)
    