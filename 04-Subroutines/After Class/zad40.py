tablica =[1,2,3,4,5,6,7,8]
x=list(filter(lambda x:x%2==0,tablica))
print(f"Z tablicy {tablica}, parzyste są:",x)