## Postcode Finder

This was developed to:
- lookup postcodes in a csv file,
- find their latitude and longdtitude and write to a new csv file.
- Given a new postcode, find which postcodes in the new csv file are closest.

postcodeslookup.py
Postcodes must be entered as a single column in a file saved in .csv format:
```
random-postcodes.csv:
ts16 0HE
SO15 5PL
CV4
SA14 8AQ
sO15 5PL
SW17
```
Either as solely the first part or the first and last part separated by a space

You can then call the postcodeslookup.py function as follows.
The second part can be totally made up, the program will create the file if it doesn't exist.
input:
```
python postcodeslookup.py random-postcodes.csv random-postcodesoutput.csv
```
output:
```
Succesfully written to random-postcodesoutput.csv
```
inside random-postcodeoutput.csv we expect to find:
```
TS16,54.52393,-1.35257
SO15,50.91629,-1.42381
CV4,52.39794,-1.56492
SA14,51.73245,-4.10721
SO15,50.91629,-1.42381
SW17,51.43030,-0.16283
```
