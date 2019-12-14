class KostkaDoGry():
    def __init__(self):
        self.rzut=0
    def rzuc(self):
        import random
        self.rzut=random.randint(1,6)
        return self.rzut

        
       
a= KostkaDoGry()
a.rzuc()
print('Trzy losowe rzuty kostką:')
suma=0
for x in range (3):
    rzut=a.rzuc()
    suma+=rzut
    print(rzut)
print('Dają w sumie:',suma)