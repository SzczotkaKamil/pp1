class Statystyka():
    def __init__(self):
        self.zbior=[]

    def minimum(self):
        print('Minimum to: '+str(min(self.zbior)))
    def srednia(self):
        suma=0
        for x in range(len(self.zbior)):
            suma+=self.zbior[x]
        print('Srednia to: '+str(suma/len(self.zbior)))
    def mediana(self):
        import statistics
        print('Mediana to: '+str(statistics.median(self.zbior)))
    def maximum(self):
        print('Maximum to: '+str(max(self.zbior)))
    def dodawanieLiczb(self):
        self.zbior.append(int(input('Wprowadź liczbę którą chcesz dodać do zbioru.')))
    def wyswietlZbior(self):
        print(self.zbior)
    def __str__(self):
        return str(self.zbior)
a=Statystyka()

for x in range (5):
    a.dodawanieLiczb()

a.wyswietlZbior()
a.minimum()
a.maximum()
a.srednia()
a.mediana()