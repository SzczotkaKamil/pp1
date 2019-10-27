for x in range (7):
    a=1
    for y in range(7):
        if a+x<10:
            print("",a+x, end=" ")
            a+=7
        else:
            print(a+x, end=" ")
            a+=7
    
    print("")
