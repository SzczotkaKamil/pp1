from datetime import date
try:
    todaysDate = date.today()
    d1 = todaysDate.strftime("%Y")
    print (d1)
    wprowadzonyPesel = str(input("Podaj numer pesel: "))
    sprawdzenieCzyInt = int(wprowadzonyPesel)
    if len(wprowadzonyPesel)==11 and sprawdzenieCzyInt>=0:
        tablicaPesel = ",".join(wprowadzonyPesel)
        tablicaPesel = tablicaPesel.split(",")
        if int(tablicaPesel[9])%2==0:
            plec = "kobieta"
        else:
            plec = "mężczyzna"
        if int(tablicaPesel[2]+tablicaPesel[3])<=12:
            wiekObywatela = int(d1)-(int(wprowadzonyPesel[:2])+1900)
            print("Płeć:",plec)
            print("Wiek:",wiekObywatela)
        elif int(tablicaPesel[2]+tablicaPesel[3])>=81 and int(tablicaPesel[2]+tablicaPesel[3])<=92:
            wiekObywatela = int(d1)-(int(wprowadzonyPesel[:2])+1800)
            print("Płeć:",plec)
            print("Wiek:",wiekObywatela)
        elif int(tablicaPesel[2]+tablicaPesel[3])>=21 and int(tablicaPesel[2]+tablicaPesel[3])<=32:
            wiekObywatela = int(d1)-(int(wprowadzonyPesel[:2])+2000)
            print("Płeć:",plec)
            print("Wiek:",wiekObywatela)
    else:
        print("Pesel musi składać się z 11 cyfr.")
except:
    print("Pesel musi składać się z 11 cyfr.")