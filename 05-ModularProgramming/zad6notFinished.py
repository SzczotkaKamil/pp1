import csv
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)