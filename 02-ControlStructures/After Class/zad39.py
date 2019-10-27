for i in range(0,50):
    if i==0:
        liczba1=0
        print(liczba1,end=" ")
    elif i==1:
        liczba2=1
        print(liczba2,end=" ")
    else:
        print(liczba1+liczba2, end=" ")
        pomocnicza=liczba1
        liczba1=liczba2
        liczba2=pomocnicza+liczba1
        
            
