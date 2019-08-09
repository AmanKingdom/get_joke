import csv

data = None
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    data = [x[0] for x in reader]

print(len(data))

data = list(set(data))

print(len(data))

with open('data2.csv', 'a', newline='') as f2:
    writer = csv.writer(f2)
    for x in data:
        writer.writerow([x])
