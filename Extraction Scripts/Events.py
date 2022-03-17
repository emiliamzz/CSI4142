# What needs to be scraped:
# - event_location_country
# - specific_location
# - name
# - type
# - attendance
# - date

import re
from lxml import html

def parseInfobox(infobox):
    info = {}
    arr = infobox.split("|")
    for item in arr:
        entry = item.split("=", 1)
        if len(entry) != 2:
            continue
        key = entry[0].strip()
        value = entry[1].strip()
        info[key] = value
    return info

def scrape(info):
    year = info.get("year", info.get("date", info.get("dates")))
    country = info.get("country", info.get("countries", info.get("location")))
    location = info.get("city", info.get("cities", info.get("location")))
    attendance = info.get("attendace")
    name = info.get("title", info.get("name"))
    if name == None:
        for key in info.keys():
            if "_name" in key:
                name = info[key]
                break

    if year != None:
        year = re.search("\d{4}", year)
    if year != None:
        year = int(year.group())
    else:
        year = 0

    if country != None:
        for c in countries:
            if c in country:
                country = c
                break

    if location != None:
        location = location.split(",")
        location = location[0]
        location = re.sub("^a-zA-Z", "", location)

    return year, country, location, name, attendance

def toStr(item):
    if item == None:
        return "NULL"
    else:
        return "\"" + str(item) + "\""

tree = html.parse("./event_wiki.xml")
root = tree.getroot()[0]
countries = ["Canada", "USA", "Mexico", "China", "Brazil", "South Africa", "Mongolia", "Egypt", "India"]
i = 0
f = open("Event.sql", "w", encoding="utf-8")

for child in root:
    info = parseInfobox(child.find("infobox").text)
    year, country, location, name, attendance = scrape(info)
    if year < 2005 or year > 2020 or country not in countries:
        continue
    f.write("INSERT INTO event (event_key, event_location_country, specific_location, name, attendance, date) VALUES (" + toStr(i) + ", " + toStr(country) + ", " + toStr(location) + ", " + toStr(name) + ", " + toStr(attendance) + ", " + toStr(year) + ");\n")
    i += 1

f.close()
