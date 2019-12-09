class Ksiazka():
  def __init__(self,cena,tytul,autor):
    self.cena = cena
    self.tytul = tytul
    self.autor = autor

  def myfunc(self):
    print("Autor to: " + self.autor)
    print("Cena wynosi: " + str(self.cena))
    print("Tytul to: " + self.tytul)
    print()

ksiazka1 = Ksiazka(20,'It','S.King')
ksiazka1.myfunc()
ksiazka2 = Ksiazka(40,'Harry Potter','J.K. Rowling')
ksiazka2.myfunc()
ksiazka3 = Ksiazka(30,'Percy Jackson','Rick Riordian')
ksiazka3.myfunc()
