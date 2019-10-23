koniecRange = 100 #Podaj dowolną liczbę naturalną
string2 = ""
for z in range(koniecRange):
    if z<=koniecRange/2:
        string2+="*"
for x in range(1,koniecRange):
    string = ""
    if x<koniecRange/2:
        for y in range(x):
            string +="*"
        print(string)
    else:
        for y in range(x):
            if string2!="":
                string2 = string2[:-1]
                print(string2)
