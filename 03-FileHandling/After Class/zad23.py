import re
suma=0
file =open("C:/Users/pc/Desktop/pp1/03-FileHandling/land.txt","r")
cyfryZTekstu = re.findall('\d',file.read())
for x in cyfryZTekstu:
    suma+=int(x)
print(suma)
file.close()