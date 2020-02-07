"""
Contains model for postcodes.
"""
import csv


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


def main():
    print("Use one of the command line args to run this program")


if __name__ == "__main__":
    main()
