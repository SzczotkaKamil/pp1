tablica = [32, 16, 5, 8, 24, 7]
f=open("liczbyZTablicy.txt","a")
for x in range(6):   
    liczbaDoDodania = str(tablica[x])+"\n"
    f.write(liczbaDoDodania)
f.close()