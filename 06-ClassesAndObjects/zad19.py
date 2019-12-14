class RachunekBankowy():
    def __init__(self):
        self.nrRachunku=0
        self.saldo=0
    def ustalanieNumeru(self,nrRachunku):
        self.nrRachunku=nrRachunku
    def wplacKwote(self,kwota):
        self.saldo+=kwota
    def wyplacKwote(self,kwota):
        if self.saldo>=kwota:
            self.saldo-=kwota
        else:
            print("Niewystarczająca ilość środków na rachunku.")
    def sprawdzStanKonta(self):
           print('Nr rachunku: '+str(self.nrRachunku)+', '+'Saldo: '+str(self.saldo))
    def __str__(self):
        return 'Nr rachunku: '+str(self.nrRachunku)+', '+'Saldo: '+str(self.saldo)
        
a = RachunekBankowy()
a.ustalanieNumeru(12345655559090111100007722)
a.sprawdzStanKonta()
a.wplacKwote(25.3)
a.sprawdzStanKonta()
a.wyplacKwote(31.70)
a.sprawdzStanKonta()
a.wyplacKwote(14)
a.sprawdzStanKonta()
