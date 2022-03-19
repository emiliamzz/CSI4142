import csv

def toStr(item):
    return "\'" + str(item) + "\'"

def toStrCountry(country):
    if country == "Canada":
        country = "1"
    elif country == "United States":
        country = "2"
    elif country == "Mexico":
        country = "3"
    elif country == "China":
        country = "4"
    elif country == "Brazil":
        country = "5"
    elif country == "South Africa":
        country = "6"
    elif country == "Pakistan":
        country = "7"
    elif country == "Egypt, Arab Rep.":
        country = "8"
    elif country == "India":
        country = "9"
    return toStr(country)

# data = {country: {year dict}}
# year dict = {year: population}

data = {}
countries = ["Canada", "United States", "Mexico", "China", "Brazil", "South Africa", "Pakistan", "Egypt, Arab Rep.", "India"]

csvFile = csv.reader(open("./data.csv"))
next(csvFile)
rows = []

# Get the population of each country
for row in csvFile:
    rows.append(row)
    if "Population, total" in row[0]:
        country = row[2]
        i = 4
        yearDict = {}
        while i <= 19:
            year = 2001 + i
            yearDict[year] = row[i]
            i += 1
        data[country] = yearDict

f = open("CountryHistory.sql", "w")
i = 0

for country in data:
    for year in data[country]:
        if year != 2020:
            f.write("INSERT INTO \"Country History\" (country_history_key, country_key, year_key, population) VALUES (" + toStr(i) + ", " + toStrCountry(country) + ", " + toStr(year) + ", " + toStr(data[country][year]) + ");\n")
            i += 1

f.close()
