file = open('C:/Users/s-115-28/Desktop/pp1/03-FileHandling/shoppinglist.txt','a')
nazwaProduktu = input('Podaj nazwę produktu który chcesz dodać do listy zakupów: ')+"\r\n"
file.write(nazwaProduktu)
file.close()
