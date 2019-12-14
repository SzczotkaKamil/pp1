class Ulamki():
    def __init__(self):
        self.licznik=0
        self.mianownik=0
    def tworzenieUlamka(self,licznik,mianownik):
        self.licznik=licznik
        self.mianownik=mianownik
    def skracanieUlamka(self):
        import math
        pom =math.gcd(self.licznik,self.mianownik)
        self.licznik=int(self.licznik/pom)
        self.mianownik=int(self.mianownik/pom)
    def __str__(self):
        return f'Ułamek po uproszczeniu ma postać:'+(str(self.licznik)+"/"+str(self.mianownik))
aa = Ulamki()
aa.tworzenieUlamka(110,11)
aa.skracanieUlamka()
print(aa)