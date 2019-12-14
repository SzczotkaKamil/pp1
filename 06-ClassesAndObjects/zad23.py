class Kontakt():
    def __init__(self,nazwa,email,telefon):
        self.nazwa=nazwa
        self.email=email
        self.telefon=telefon
    def wyswietlKontakt(self):
        print(self.nazwa,",",self.email,",",self.telefon)       
class ListaKontaktow():
    def __init__(self):
        self.kontakty=[]
    def dodaj(self,kontakt):
        self.kontakty.append(kontakt)
    def wyswietlKontakty(self):
        for kontakt in self.kontakty:
            kontakt.wyswietlKontakt()
k1=Kontakt('Kowalski Jan','jank@onet.pl','555234000')
k2=Kontakt('Borek Patrycja','bp@o2.pl','232000199')
k3=Kontakt('Maj Piotr','maj@google.com','222999100')
k4=Kontakt('Adamczyk Anna','ada@poczta.pl','100200300')
pom=ListaKontaktow()
pom.dodaj(k1)
pom.dodaj(k2)
pom.dodaj(k3)
pom.dodaj(k4)
pom.wyswietlKontakty()