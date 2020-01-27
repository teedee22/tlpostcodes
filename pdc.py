import csv
import geopy.distance


class Postcode:
    def __init__(self, code):
        self.code = code.upper()
        self.latitude = None
        self.longtitude = None
        self.latlong()

    def hello(self):
        pass

    def latlong(self):
        with open("all-uk-postcodes.csv") as csvfile:
            readCSV = csv.reader(csvfile, delimiter=",")
            for row in readCSV:
                if row[1] == self.code:
                    self.latitude = row[2]
                    self.longtitude = row[3]


#    def postcodeInput(self):
#        self.code = input("Enter first part of the first postcode: ".upper()


postcode1 = Postcode("CV8")
postcode2 = Postcode("B3")

print(postcode1.latitude)
print(postcode1.longtitude)
print(postcode2.latitude)
print(postcode2.longtitude)

print(
    geopy.distance.vincenty(
        (postcode1.latitude, postcode1.longtitude),
        (postcode2.latitude, postcode2.longtitude),
    )
)
# Distance calculator
