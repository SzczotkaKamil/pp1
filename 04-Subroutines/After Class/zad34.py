pom =0
def fib(n):
    global a,b,pom
    if pom==0:
        
        a,b = 0,1
        pom+=1
    
    if n>0:
        a,b = b,a+b
        n-=1
        return fib(n)
    else:
        return a

for x in range (20):
    print(fib(x), end=", ")
    a,b,pom=None,None,0