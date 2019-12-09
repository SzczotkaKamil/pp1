class Utwory():
    def __init__(self,wykonawca,tytul,album,rok):
        self.wykonawca=wykonawca
        self.tytul=tytul
        self.album=album
        self.rok=rok
        
    def __str__(self):
        return 'Wykonawca: '+self.wykonawca+'\nUtwór: '+self.tytul+'\nAlbum: '+self.album+'\nRok: '+self.rok+'\n'
obiekt1=Utwory('Podsiadlo','Nie ma fal','Malomiasteczkowy','2018')
obiekt2=Utwory('NF','The Search','The Search','2019')
obiekt3=Utwory('Nirvana','Smells Like Teen Spirit','Nevermind','1987')
print(obiekt1)
print(obiekt2)
print(obiekt3)
    