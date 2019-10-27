try:
    numerKontaBankowego=int(input("Podaj nr rachunku bankowego (wprowadź same cyfry): "))
    listNrKontaBankowego =  list(str(numerKontaBankowego))
    ileCyfrWprowadzonych = len(listNrKontaBankowego)
    if ileCyfrWprowadzonych == 26:
        print("Nr rachunku: ",listNrKontaBankowego[0]+listNrKontaBankowego[1],listNrKontaBankowego[2]+listNrKontaBankowego[3]+listNrKontaBankowego[4]+listNrKontaBankowego[5],listNrKontaBankowego[6]+listNrKontaBankowego[7]+listNrKontaBankowego[8]+listNrKontaBankowego[9],listNrKontaBankowego[10]+listNrKontaBankowego[11]+listNrKontaBankowego[12]+listNrKontaBankowego[13],listNrKontaBankowego[14]+listNrKontaBankowego[15]+listNrKontaBankowego[16]+listNrKontaBankowego[17],listNrKontaBankowego[18]+listNrKontaBankowego[19]+listNrKontaBankowego[20]+listNrKontaBankowego[21],listNrKontaBankowego[22]+listNrKontaBankowego[23]+listNrKontaBankowego[24]+listNrKontaBankowego[25])
    else:
        print(f"Twój numer konta bankowego powinien składać się z 26 cyfr, a składa się z: {ileCyfrWprowadzonych}")
except:
    print("Niepoprawny numer rachunku bankowego.")
    
   