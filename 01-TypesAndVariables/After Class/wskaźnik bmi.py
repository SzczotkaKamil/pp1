try:
    # Podaj wzrost w cm: 
    wzrost = int(input("Podaj wzrost w cm: "))
    # Podaj wagę w kg: 
    waga = int(input("Podaj wagę w kg: "))
    #Wskaźnik BMI: 
    bmi = waga/(wzrost/100)**2
    if bmi<18.5:
         print(f"Wskaźnik BMI: {bmi} (masz niedowagę)")
    elif bmi>=18.5 and bmi<=24.99:
        print(f"Wskaźnik BMI: {bmi} (wartość prawidłowa)")
    else:
        print(f"Wskaźnik BMI: {bmi} (masz nadwagę)")
except:
    print("Podaj wzrost oraz wagę używając tylko liczb całkowitych.")