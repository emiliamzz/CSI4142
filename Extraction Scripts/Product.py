# What needs to be scraped:
# - name
# - status 
# - type
# - price_per_unit

import json
import pandas
import re
from difflib import SequenceMatcher

def cleanName(item):
    name = item.split(",")[0]
    name = re.sub("\(.*?\)", "", name)
    name = re.sub("\d", "", name)
    return name.strip()
    
def toStr(item):
    if item == None:
        return "NULL"
    else:
        return "\"" + str(item) + "\""

namesFile = open("./drugs.json", encoding="utf-8")
names = json.load(namesFile)

statusesFile = open("./status.json", encoding="utf-8")
statuses = json.load(statusesFile)

typesFile = open("./administration.json", encoding="utf-8")
types = json.load(typesFile)

pricesFile = pandas.read_excel("./wac.xlsx")
prices = json.loads(pricesFile.to_json())

info = {}
f = open("Product.sql", "w")

for name in names:
    info[name["drug_code"]] = [name["brand_name"], None, None, None]

for status in statuses:
    info[status["drug_code"]][1] = status["status"]

for type in types:
    info[type["drug_code"]][2] = type["route_of_administration_name"]

for i in range(len(prices["OSHPD ID"])):
    priceName = cleanName(prices["Drug Product Description"][str(i)])
    price = prices["WAC After Increase"][str(i)]
    for item in info:
        itemName = cleanName(info[item][0])
        if SequenceMatcher(None, priceName, itemName).ratio() >= 0.8:
            info[item][3] = price
            break

i = 0
for item in info:
    f.write("INSERT INTO product (product_key, name, status, type, price_per_unit) VALUES (" + toStr(i) + ", " + toStr(info[item][0]) + ", " + toStr(info[item][1]) + ", " + toStr(info[item][2]) + ", " + toStr(info[item][3]) + ");\n")
    i += 1

f.close()
