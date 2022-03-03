# What needs to be scraped:
# - event_location_country
# - specific_location
# - name
# - type
# - attendance
# - date

from lxml import html

def parseInfobox(infobox):
    info = {}
    arr = infobox.split("|")
    for item in arr:
        key = item.split("=", 1)[0]
        key = key[1:]
        key = key.strip()
        value = item.split("=", 1)[1]
        value = value.strip()
        info[key] = value
    return info

def scrape(type, info):
    if type == "international football competition":
        year = int(info["year"])
        country = info["country"]
        location = info["city"]
        name = info["tourney_name"]
        attendance = info["attendance"]
    # TODO: the rest of the event types
    return year, country, location, name, attendance

tree = html.parse("./event_wiki.xml")
root = tree.getroot()[0]
countries = ["Canada", "USA", "Mexico", "China", "Brazil", "South Africa", "Mongolia", "Egypt", "India"]
i = 0
f = open("Event.sql", "w")

for child in root:
    type = child.find("type").text
    info = parseInfobox(child.find("infobox").text)
    year, country, location, name, attendance = scrape(type, info)
    if year < 2005 or year > 2020 or country not in countries:
        continue
    f.write("INSERT INTO event (event_key, event_location_country, specific_location, name, attendance, date) VALUES (", i, ", ", country, ", ", location, ", ", name, ", ", attendance, ", ", year)
    i += 1

f.close()
