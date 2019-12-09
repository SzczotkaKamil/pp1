class University():
# konstruktor obiektu (metoda __init__)
    def __init__(self):
# cechy obiektu (pola)
        self.name='uek'
# zachowania obiektu (metody)
    def set_name(self,name):
        self.name = name
    def print_name(self):
        print(self.name)
        
pom = University()
pom.set_name('AGH')
pom.print_name()
