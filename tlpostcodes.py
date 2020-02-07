# for postcode in file 1
# find top three nearest in file 2
# write them to file 3
# py tlpostcodes.py clientpostcodes coursepostcodes filetowriteto
import csv
from postcodenearest import postcodenearest
import os
from at import getCentres, getPeopleWantingCourse
from airtable import Airtable

airtable = Airtable(
    os.environ["AIRTABLE_BASE_KEY"],
    "People",
    api_key=os.environ["AIRTABLE_API_KEY"],
)

# people = airtable.get_all(view="Wanting a course")


centredict = {}
centres = getCentres()
for centre in centres:
    centredict[centre[0]] = centre[1]
print(centredict)
"""
with open("airtable/wantingcourse.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    for row in readCSV:
        rowammend = row[0].split()
        nearest = postcodenearest(rowammend[0], "airtable/centres.csv")
        print(row[0])
        print(nearest[0][1])
        print(nearest[0][0])

        record = airtable.match("Record Id", row[1])
        fields = {
            "firstNearestActiveCentreDist": nearest[0][0],
            "firstNearestActiveCentre": [centredict[nearest[0][1]]],
            "secondNearestActiveCentreDist": nearest[1][0],
            "secondNearestActiveCentre": [centredict[nearest[1][1]]],
            "thirdNearestActiveCentreDist": nearest[2][0],
            "thirdNearestActiveCentre": [centredict[nearest[2][1]]],
        }
        airtable.update(record["id"], fields)
"""
