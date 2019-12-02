class University():
# konstruktor obiektu (metoda __init__)
    def __init__(self):
# cechy obiektu (pola)
        self.name='uek'
# zachowania obiektu (metody)
    def set_name(self,new_name):
        self.name = new_name
    def print_name(self):
        print(self.name)
University().set_name('AGH')
University().print_name()
