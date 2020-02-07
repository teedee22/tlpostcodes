record = airtable.match('Record Id', 'recwWIEK7zNZGiBvO')
fields = {'firstNearestActiveCentreDist': 12}
airtable.update(record['id'], fields)


airtable = Airtable(os.environ['AIRTABLE_BASE_KEY'], 'People', os.environ['AIRTABLE_API_KEY'])
