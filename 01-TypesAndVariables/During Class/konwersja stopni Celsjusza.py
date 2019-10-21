#konwersja stopni Celsjusza na stopnie Fahrenheita oraz stopnie Kelvina
stopnieCelsjusza = float(input ("Podaj dowolną temperaturę wyrażoną w stopniach Celsjusza: "))
skonwertowaneNaFahrenheita = (stopnieCelsjusza * 9/5) + 32
skowertowaneNaKelvina = stopnieCelsjusza + 273.15
print (f"Temperatura w stopniach Celsjusza: {stopnieCelsjusza}°C w stopniach Fahrenheita wynosi: {skonwertowaneNaFahrenheita}°F, a w stopniach Kelvina: {skowertowaneNaKelvina}°K ")
