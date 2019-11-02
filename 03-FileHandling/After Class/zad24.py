tablica=[['Imie','Nazwisko','E-mail'],['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'
],['Piotr','Wyga','wygap@gop.pl']]

with open('zad24.csv', 'w')as file:
    for y in tablica:
        for x in y:
            if x!=y[-1]:
                file.write(f'{x},')
            else:
                file.write(f'{x}\n')