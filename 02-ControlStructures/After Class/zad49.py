dniMiesiaca=[]
for o in range (1,31):
    dniMiesiaca.append(o)
    
    
nrDniaTygodnia= 2 #Definiowanie który dzień tygodnia jest pierwszym w miesiącu.
nazwaDniaTygodnia=["PN","WT","SR","CZ","PT","SB","ND"]


for x in range(7):
    print(f"| {nazwaDniaTygodnia[x]} ",end="")
print("|")



pomocnicza=0
for y in range(5):
    for q in range(nrDniaTygodnia):
        if y==0:
            print("|    ", end="")
    for z in range(7):
        if z+nrDniaTygodnia==7 and y==0:
            break
        if pomocnicza<30 and pomocnicza<10 and dniMiesiaca[pomocnicza]!=10:
            print(f"|  {dniMiesiaca[pomocnicza]} ",end="")
            pomocnicza+=1
        elif pomocnicza<30 and pomocnicza>=10 and dniMiesiaca[pomocnicza]!=10:
            print(f"| {dniMiesiaca[pomocnicza]} ",end="")
            pomocnicza+=1
        elif dniMiesiaca[9]==10 and pomocnicza<30:
            print(f"| {dniMiesiaca[pomocnicza]} ",end="")
            pomocnicza+=1
        else:
            print("|    ",end="")      
    print("|")
