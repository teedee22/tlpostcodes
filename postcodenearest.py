import sys
import csv
import geopy.distance
from pdc import Postcode


def postcodenearest(inCode, inFileName):
    code = Postcode(inCode)
    distances = []
    with open(inFileName) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        for row in readCSV:
            newrow = row[0].split()
            tempcode = Postcode(newrow[0])
            distances.append(
                (
                    round(
                        geopy.distance.vincenty(
                            (tempcode.latitude, tempcode.longtitude),
                            (code.latitude, code.longtitude),
                        ).miles,
                        2,
                    ),
                    row[0],
                )
            )
    distances.sort()

    return (distances[0], distances[1], distances[2])


def main():
    if not len(sys.argv) == 3:
        print(
            "use following format: postcodeslookup.py postcode searchfile.csv"
        )
    print(f"These are the nearest addresses to {sys.argv[1]}: ")
    print(postcodenearest(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":
    main()
