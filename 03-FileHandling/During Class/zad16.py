import re
komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
sredniaTemperatura = 0
for x in range(len(cyfry)):
    sredniaTemperatura+=int(cyfry[x])
print(f"Średnia temperatura wynosi: {sredniaTemperatura/len(cyfry)}")