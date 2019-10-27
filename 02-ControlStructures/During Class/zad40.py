import random
jeden=0
dwa=0
trzy=0
cztery=0
piec=0
szesc=0
for i in range (100):
    losowa=random.randrange(1,7)
    if losowa==1:
        jeden+=1
    elif losowa==2:
        dwa+=1
    elif losowa==3:
        trzy+=1
    elif losowa==4:
        cztery+=1
    elif losowa==5:
        piec+=1
    else:
        szesc+=1
print("Szóstka:",szesc)
print("Piątka:",piec)
print("Czwórka:",cztery)
print("Trójka:",trzy)
print("Dwójka:",dwa)
print("Jedynka:",jeden)