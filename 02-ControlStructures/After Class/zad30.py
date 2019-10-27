kodPin= "0805"
for x in range(3):
    wprowadzonyPin= str(input("Podaj kod PIN: "))
    if wprowadzonyPin==kodPin:
        print("Kod PIN jest poprawny.")
        break
    else:
        print("Kod PIN jest niepoprawny.")
if wprowadzonyPin!=kodPin:
    print("Karta płatnicza zostaje zablokowana.")
        