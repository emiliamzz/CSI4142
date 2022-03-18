# What needs to be scraped:
# - name
# - status 
# - type
# - price_per_unit

import json
import random
import re

def randomPrice():
    return round(random.uniform(1.00, 1000.00), 2)

def toStr(item):
    if item == None or item == "":
        item = "UNKNOWN"
    return "\"" + str(item) + "\""

namesFile = open("./drugs.json", encoding="utf-8")
names = json.load(namesFile)

statusesFile = open("./status.json", encoding="utf-8")
statuses = json.load(statusesFile)

typesFile = open("./administration.json", encoding="utf-8")
types = json.load(typesFile)

info = {}
f = open("Product.sql", "w")

for name in names:
    info[name["drug_code"]] = [name["brand_name"], None, None, randomPrice()]

for status in statuses:
    info[status["drug_code"]][1] = status["status"]

for type in types:
    info[type["drug_code"]][2] = type["route_of_administration_name"]

i = 0
for item in info:
    f.write("INSERT INTO product (product_key, name, status, type, price_per_unit) VALUES (" + toStr(i) + ", " + toStr(info[item][0]) + ", " + toStr(info[item][1]) + ", " + toStr(info[item][2]) + ", " + toStr(info[item][3]) + ");\n")
    i += 1

f.close()
