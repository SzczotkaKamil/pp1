class University():
# konstruktor obiektu (metoda __init__)
    def __init__(self):
# cechy obiektu (pola)
        self.name='uek'
        self.fullname = 'Uniwersytet Ekonomiczny w Krakowie'
# zachowania obiektu (metody)
    def set_name(self,name):
        self.name = name
    def print_name(self):
        print(self.name)
    def print_fullname(self):
        print(self.fullname)
    def set_fullname(self,fullname):
        self.fullname=fullname

pom = University()
pom.print_fullname()
pom.set_fullname('Akademia Górniczo Hutnicza')
pom.print_fullname()

