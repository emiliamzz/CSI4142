# - name
# - communicable
# - cases_reported
# - death_rate
# - immunization_percentage
# - country

import csv

def toStr(item):
    if item == None:
        return "NULL"
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
# year dict = {year: [affliction dict, population]}
# affliction dict = {affliction: [communicable, cases_reported, death_rate, immunization_percentage]}

data = {}
afflictions = ["HIV/AIDS", "ARI", "Diarrhea", "Malaria", "Tuberculosis", "Diabetes", "Hypertension", "Tobacco use", "BCG", "HepB3", "Measles", "Pol3", "DPT", "Hib3"]
countries = ["Canada", "United States", "Mexico", "China", "Brazil", "South Africa", "Pakistan", "Egypt, Arab Rep.", "India"]

# Initialize the data dict
for country in countries:
    i = 2005
    yearDict = {}
    while i <= 2020:
        afflictionDict = {}
        for affliction in afflictions:
            if affliction == "Diabetes" or affliction == "Hypertension" or affliction == "Tobacco use":
                afflictionDict[affliction] = ["False", None, None, None]
            else:
                afflictionDict[affliction] = ["True", None, None, None]
        yearDict[i] = [afflictionDict, None]
        i += 1
    data[country] = yearDict

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
            yearDict[year] = [data[country][year][0], row[i]]
            i += 1
        data[country] = yearDict

# Get the other numbers of each country
for row in rows:
    affliction = None
    if "HIV" in row[0] or "AIDS" in row[0]:
        affliction = "HIV/AIDS"
    else:
        for aff in afflictions:
            if aff.lower() in row[0].lower():
                affliction = aff
                break
    if affliction == None:
        continue
    country = row[2]
    i = 4
    while i <= 19:
        if row[i] != "..":
            year = 2001 + i
            if "death" in row[0]:
                if affliction == "AIDS/HIV": # affliction will be AIDS
                    data[country][year][0][affliction][2] = float(row[i]) / float(data[country][year][1]) * 100000
                else: 
                    data[country][year][0][affliction][2] = row[i]
            elif "Immunization" in row[0]:
                data[country][year][0][affliction][3] = row[i]
            else: # will be cases_reported
                if affliction == "Tuberculosis":
                    data[country][year][0][affliction][1] = float(row[i]) / 100000 * float(data[country][year][1])
                elif affliction == "HIV/AIDS" or affliction == "malaria":
                    data[country][year][0][affliction][1] = float(row[i]) / 1000 * float(data[country][year][1])
                else: # will be one of the non-communicable diseases
                    data[country][year][0][affliction][1] = float(row[i]) / 100 * float(data[country][year][1])
        i += 1

f = open("Affliction.sql", "w")
i = 0
j = 0

for country in data:
    for year in data[country]:
        for affliction in data[country][year][0]:
            info = data[country][year][0][affliction]
            if year == 2020:
                f.write("INSERT INTO \"Affliction\" (affliction_key, name, communicable, cases_reported, death_rate, immunization_percentage, country_key) VALUES (" + toStr(i) + ", " + toStr(affliction) + ", " + toStr(info[0]) + ", " + toStr(info[1]) + ", " + toStr(info[2]) + ", " + toStr(info[3]) + ", " + toStrCountry(country) + ");\n")
                i += 1
            else:
                f.write("INSERT INTO \"Affliction History\" (affliction_history_key, name, communicable, cases_reported, death_rate, immunization_percentage, country_key, year_key) VALUES (" + toStr(j) + ", " + toStr(affliction) + ", " + toStr(info[0]) + ", " + toStr(info[1]) + ", " + toStr(info[2]) + ", " + toStr(info[3]) + ", " + toStrCountry(country) + ", " + toStr(year) + ");\n")
                j += 1

f.close()
