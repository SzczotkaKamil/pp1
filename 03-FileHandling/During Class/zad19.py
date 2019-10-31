uniwersytety = []
file = open("C:/Users/Kamil/Desktop/pp1/03-FileHandling/universities.txt","r+")
for line in file:
    uniwersytety.append(line.strip())
uniwersytety.sort()
print(uniwersytety)
file.truncate(0)
for x in range(len(uniwersytety)):   
    strDoDodania = uniwersytety[x]+"\n"
    file.write(strDoDodania)
file.close()