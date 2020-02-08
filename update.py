from postcodenearest import postcodenearest
import os
from at import getCentres, getPeopleWantingCourse
from airtable import Airtable


def updateAirtable():
    airtable = Airtable(
        os.environ["AIRTABLE_BASE_KEY"],
        "People",
        api_key=os.environ["AIRTABLE_API_KEY"],
    )
    pwc = getPeopleWantingCourse()
    for person in pwc:
        firstcode = person.split()
        centres = getCentres()
        nearest = postcodenearest(firstcode[0], centres)
        fields = {
            "firstNearestActiveCentreDist": nearest[0][0],
            "firstNearestActiveCentre": [centres[nearest[0][1]]],
            "secondNearestActiveCentreDist": nearest[1][0],
            "secondNearestActiveCentre": [centres[nearest[1][1]]],
            "thirdNearestActiveCentreDist": nearest[2][0],
            "thirdNearestActiveCentre": [centres[nearest[2][1]]],
        }
        record = airtable.match("Record Id", pwc[person])
        airtable.update(record["id"], fields)
        print("Updated row" + pwc[person])


def main():
    updateAirtable()


if __name__ == "__main__":
    main()
