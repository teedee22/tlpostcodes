"""
Reads input file and outputs latitude longtitude to file
postcodeslookup.py inputfile.csv outputfile.cs
"""
import sys
import csv

from pdc import Postcode


def postcodelookup(inFileName, outFileName):
    with open(inFileName) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        for row in readCSV:
            postcode = row[0].split()
            code = Postcode(postcode[0])
            code.writeToFile(outFileName)
        print(f"Succesfully written to {outFileName}")


def main():
    if not len(sys.argv) == 3:
        print(
            "use following format: postcodeslookup.py inputfile.csv outputfile.csv"
        )
    else:
        try:
            postcodelookup(sys.argv[1], sys.argv[2])
        except FileNotFoundError:
            print("your input file is invalid, check it exists")


if __name__ == "__main__":
    main()
