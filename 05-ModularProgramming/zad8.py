import turtle
pomocnicza = 0
zejscieWDol = 0
def drawSquare(x,y,n):
    # n= dlugosc boku kwadratu
    #lewy gorny naroznik wspolrzedne (x,y)
    global tmp
    tmp=n
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
    
    
    
for y in range(4):
    for x in range(4):
        drawSquare(-500+pomocnicza,500-zejscieWDol,100)
        pomocnicza+=tmp
    zejscieWDol+=tmp
    pomocnicza=0
            
    