x = 0
y = 0
if x>0 and y>0:
    print(f"Punkt p({x},{y}) znajduje się w pierwszej ćwiartce.")
elif x<0 and y>0:
    print(f"Punkt p({x},{y}) znajduje się w drugiej ćwiartce.")
elif x<0 and y<0:
    print(f"Punkt p({x},{y}) znajduje się w trzeciej ćwiartce.")
elif x==0 and y==0:
    print(f"Punkt p({x},{y}) znajduje się na początku układu współrzędnych.")
else:
    print(f"Punkt p({x},{y}) znajduje się w czwartej ćwiartce.")