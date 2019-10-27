a=4
b=15
for x in range(a):
    string = ""
    string2 = "*"
    if x==0 or x ==a-1:
        for y in range(b):
            string+="*"
        print(string)
    else:
        if b==2:
            print("**")
        elif b>2:
            for z in range (b-2):
                string2+=" "
            string2+="*"
            print(string2)
        elif b==1:
            print("*")