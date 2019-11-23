import shapes
zejscieWDol=0
pomocnicza=0
tmp=100
for y in range(4):
    for x in range(4):
        shapes.drawSquare(-500+pomocnicza,500-zejscieWDol,tmp)
        pomocnicza+=tmp
    zejscieWDol+=tmp
    pomocnicza=0