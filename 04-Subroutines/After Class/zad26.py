pomocnicza = 0
def podatek(dochod):
    global pomocnicza
    pomocnicza += dochod
    if dochod <=5000:
        podatek = dochod*0.17
        return podatek
    else:
        podatek= 5000*0.17+(dochod-5000)*0.32
        
        return podatek
podatek(6000)
print("Podany dochód:",pomocnicza)
print("Podatek należny:",podatek(6000))