class Student():
    licznik = 100000
    def __init__(self,imie,nazwisko,kierunek):
        self.imie =imie
        self.nazwisko=nazwisko
        self.nrAlbumu=Student.licznik
        Student.licznik+1
        self.kierunek=kierunek
    def __str__(self):
        return self.imie.capitalize()+' '+self.nazwisko.upper()+' '+f'({str(self.nrAlbumu)}),'+self.kierunek.capitalize()+','+'UEK Kraków'
    
a=Student('kamil','szczotka','informatyka Stosowana')
print(a)