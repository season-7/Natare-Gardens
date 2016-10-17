import csv

# Read each row and print it
# Open the file declaring each mode that I am going to use
# loop through the rows, checking first the size of the row then printing

with open('booking.csv', 'r') as f:
    r = csv.reader(f, delimiter=' ')
    for row in r:
        if len(row) >= 4:
            print(row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3] + ' ' + row[4])