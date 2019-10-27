import random
y = 0
for t in range(3):
    x = random.randrange(1,6)
    print(f"Rezulat {t+1} wynosi: {x}")
    y = y+x
print(f"Suma trzech rzutów to: {y}")
