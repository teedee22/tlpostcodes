from airtable import Airtable
import csv
import os

airtable = Airtable(
    os.environ["AIRTABLE_BASE_KEY"],
    "People",
    api_key=os.environ["AIRTABLE_API_KEY"],
)

people = airtable.get_all(view="Wanting a course")


def peopleWantingCourse(airtableview):
    peoplewantingcourse = []
    for person in people:
        try:
            entry = person["fields"]["Postcode extract"].strip()
            id = person["id"]
            peoplewantingcourse.append((entry, id))
        except KeyError:
            peoplewantingcourse.append(None)
    return peoplewantingcourse


for person in people:
    try:
        entry = person["fields"]["Postcode extract"].strip()
        id = person["id"]
        with open("wantingcourse.csv", mode="a") as wanting_course:
            outcode_writer = csv.writer(
                wanting_course, delimiter=",", quotechar='"'
            )

            outcode_writer.writerow([entry, id])
    except KeyError:
        print(None)

airtable2 = Airtable(
    os.environ["AIRTABLE_BASE_KEY"],
    "Centres",
    api_key=os.environ["AIRTABLE_API_KEY"],
)

centres = airtable2.get_all(view="Active Centres Postcodes")

for centre in centres:
    try:
        postcode = centre["fields"]["Postcode"]
        id = centre["id"]
        with open("centres.csv", mode="a") as centres:
            outcode_writer = csv.writer(centres, delimiter=",", quotechar='"')

            outcode_writer.writerow([postcode, id])
    except KeyError:
        print(None)
