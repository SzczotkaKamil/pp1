import turtle
def drawSquare(x,y,n):
    
    pen = turtle.Turtle()
    
    for y in range (3):
        for x in range(4):
            pen.forward(n)
            pen.right(90)
            # Rotate clockwise by 90 degrees
        pen.forward(n)
    pen.right(180)
    pen.forward(n*3)
    pen.right(90)
    pen.forward(n)
    
    turtle.done()
drawSquare(100.0,1.0,34)