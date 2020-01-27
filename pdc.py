import csv
import geopy.distance


class Postcode:
    def __init__(self, code):
        self.code = code.upper()
        self.latitude = None
        self.longtitude = None
        self.latlong()

    def writeToFile(self, outFileName):
        with open(outFileName, mode="a") as outcodes:
            outcode_writer = csv.writer(outcodes, delimiter=",", quotechar='"')

            outcode_writer.writerow(
                [self.code, self.latitude, self.longtitude]
            )

    def latlong(self):
        with open("postcodedata/all-uk-postcodes.csv") as csvfile:
            readCSV = csv.reader(csvfile, delimiter=",")
            for row in readCSV:
                if row[1] == self.code:
                    self.latitude = row[2]
                    self.longtitude = row[3]


def postcodelookup(inFileName, outFileName):
    with open(inFileName) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        for row in readCSV:
            postcode = row[0].split()
            code = Postcode(postcode[0])
            code.writeToFile(outFileName)


def postcodenearest(inCode, inFileName):
    code = Postcode(inCode)
    distances = []
    with open(inFileName) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        for row in readCSV:
            distances.append(
                (
                    geopy.distance.vincenty(
                        (row[1], row[2]), (code.latitude, code.longtitude),
                    ),
                    row[0],
                )
            )
    distances.sort()
    print(f"These are the nearest 5 addresses to {code.code}: ")
    for i in range(5):
        print(f"{distances[i][1]} : {distances[i][0]}")


def main():
    postcodelookup("random-postcodes.csv", "out-random-postcodes.csv")
    postcodenearest("SW17", "out-random-postcodes.csv")


if __name__ == "__main__":
    main()
