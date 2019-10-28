tablica = [32, 16, 5, 8, 24, 7]
f=open("liczbyZTablicy.txt","w+")
f.close()
file = open('C:/Users/s-115-28/Desktop/pp1/03-FileHandling/liczbyZTablicy.txt','a')
for x in range(6):   
    liczbaDoDodania = str(tablica[x])+"\r\n"
    file.write(liczbaDoDodania)
    file.close()
