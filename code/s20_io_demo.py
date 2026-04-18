import csv

# Read CSV (each row becomes a dict)
with open('students.csv') as f:
    for row in csv.DictReader(f):
        print(f"{row['name']}: {row['grade']}")

# Write CSV
data = [{'name': 'Alice', 'grade': 95},
        {'name': 'Bob', 'grade': 87}]
with open('output.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'grade'])
    writer.writeheader()
    writer.writerows(data)