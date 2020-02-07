"""
functions handling airtable api read interaction
"""

from airtable import Airtable
import os


def connectToAirtable(table, viewName):
    airtable = airtable = Airtable(
        os.environ["AIRTABLE_BASE_KEY"],
        table,
        api_key=os.environ["AIRTABLE_API_KEY"],
    )
    return airtable.get_all(view=viewName)


def getPeopleWantingCourse():
    people = connectToAirtable("People", "Wanting a course")
    peoplewantingcourse = {}
    for person in people:
        try:
            entry = person["fields"]["Postcode extract"].strip()
            id = person["id"]
            peoplewantingcourse[entry] = id
        except KeyError:
            peoplewantingcourse["error"] = "KeyError"
    return peoplewantingcourse


def getCentres():
    centres = connectToAirtable("Centres", "Active Centres Postcodes")
    centreslist = {}
    for centre in centres:
        try:
            postcode = centre["fields"]["Postcode"]
            id = centre["id"]
            centreslist[postcode] = id
        except KeyError:
            centreslist["error"] = "keyError"
    return centreslist
