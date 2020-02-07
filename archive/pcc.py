import csv


postcode = input("Enter first part of the postcode (in caps): ")

postcode = postcode.upper()

with open('postcode-outcodes.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[1] == postcode:
            print("latitude: " + row[2])
            print("longtitude: " + row[3])
