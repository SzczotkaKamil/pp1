import re
x=0
cos = [30]
file =open("C:/Users/pc/Desktop/pp1/03-FileHandling/Dane.txt","r")
for line in file:
    if re.findall('\d+\,',line)!=[]:
        liczba = re.findall('\d+\,',line)
        liczba[0] = liczba[0][:-1]
        cos.append(int(liczba[0]))
file.close()
file =open("C:/Users/pc/Desktop/pp1/03-FileHandling/Dane.txt","r")
for line in file:
    if cos[x]<30:
        linia = line.split(",")
        print(linia[0],linia[1],linia[4])
    x+=1
file.close()
        
        
