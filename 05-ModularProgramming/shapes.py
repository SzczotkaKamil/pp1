import turtle
def drawSquare(x,y,n):
    # n= dlugosc boku kwadratu
    #lewy gorny naroznik wspolrzedne (x,y)
    zolw = turtle.Turtle()
    zolw.penup()                 
    zolw.setposition(x,y)
    zolw.pendown()
    zolw.forward(n)
    zolw.setheading(270)
    zolw.forward(n)
    zolw.setheading(180)
    zolw.forward(n)
    zolw.setheading(90)
    zolw.forward(n)
    zolw.setheading(0)
def drawCircle(x,y,n):
    kolko=turtle.Turtle()
    kolko.penup()
    kolko.setposition(x,y-n/2)
    kolko.pendown()
    kolko.circle(50)
def drawTriangle(x,y,m):
    trojkat=turtle.Turtle()
    trojkat.penup()
    trojkat.setposition(x,y)
    trojkat.pendown()
    trojkat.setheading(0)
    trojkat.forward(m)
    trojkat.setheading(120)
    trojkat.forward(m)
    trojkat.setheading(240)
    trojkat.forward(m)
def drawStar(x,y,n):
    t = turtle.Turtle()
    for i in range(5):
      t.forward(150)
      t.right(144)
      
def drawBlackSquare(x,y,m):
    # n= dlugosc boku kwadratu
    #lewy gorny naroznik wspolrzedne (x,y)
    zolw = turtle.Turtle()
    zolw.fillcolor("black")
    zolw.begin_fill()
    zolw.penup()                 
    zolw.setposition(x,y)
    zolw.pendown()
    zolw.forward(m)
    zolw.setheading(270)
    zolw.forward(m)
    zolw.setheading(180)
    zolw.forward(m)
    zolw.setheading(90)
    zolw.forward(m)
    zolw.setheading(0)
    zolw.end_fill()
    
def szachownica(m):
    pomocnicza = 0
    zejscieWDol = 0
    pom=1
    for y in range(4):        
        for x in range(4):
            if pom%2==0:
                drawSquare(-500+pomocnicza,500-zejscieWDol,m)
                pom=x+y
                pomocnicza+=m
            else:
                drawBlackSquare(-500+pomocnicza,500-zejscieWDol,m)
                pomocnicza+=m
                pom=x+y
        pom+=1
        zejscieWDol+=m
        pomocnicza=0 