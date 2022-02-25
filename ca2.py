import csv

with open('2019_lar.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in csvfile:
        lines = row.split("\n")
        if len(lines) < 7:
            continue
            for row in reader:
                if row[3] == 'CA':
                    print(row)
