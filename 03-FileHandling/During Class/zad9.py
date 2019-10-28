with open('C:/Users/s-115-28/Desktop/pp1/03-FileHandling/NoEducation.txt','r') as file:
    i = 1    
    for line in file:
        print(f"{i}.",line, end='')
        i+=1