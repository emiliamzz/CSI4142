import csv
import numpy

def convertToInt(str):
    if str == '':
        return None
    else:
        return round(float(str))

file = open('./CSV/ProductStatuses.csv')
reader = csv.reader(file)
next(reader)
i = 0
productStatuses = {}
for row in reader:
    productStatuses[row[0]] = i
    i += 1
file.close()

file = open('./CSV/ProductTypes.csv')
reader = csv.reader(file)
next(reader)
i = 0
productTypes = {}
for row in reader:
    productTypes[row[0]] = i
    i += 1
file.close()

def booleanEncoding(value):
    if value == "t":
        return 1
    elif value == "f":
        return 0

def countryRegionEncoding(value):
    if value == "Africa":
        return 0
    elif value == "Asia":
        return 1
    elif value == "North America":
        return 2
    elif value == "South America":
        return 3

def productStatusEncoding(value):
    return productStatuses[value]

def productTypeEncoding(value):
    return productTypes[value]

# key, name, communicable, cases_reported, death_rate, immunization_percentage, country_key
file = open('./CSV/Affliction.csv')
reader = csv.reader(file)
afflictions = {}
for row in reader:
    afflictions[row[0]] = row
file.close()

# key, name, communicable, cases_reported, death_rate, immunization_percentage, country_key, year_key
file = open('./CSV/AfflictionHistory.csv')
reader = csv.reader(file)
afflictionHistories = {}
for row in reader:
    afflictionHistories[row[0]] = row
file.close()

# key, name, region, gdp, landlocked, population, rural
file = open('./CSV/Country.csv')
reader = csv.reader(file)
countries = {}
for row in reader:
    countries[row[0]] = row
file.close()

# key, country_key, year_key, population
file = open('./CSV/CountryHistory.csv')
reader = csv.reader(file)
countryHistories = {}
for row in reader:
    countryHistories[row[0]] = row
file.close()

# key, event_location_country, name, attendance, specific_location, date
file = open('./CSV/Event.csv')
reader = csv.reader(file)
events = {}
for row in reader:
    events[row[0]] = row
file.close()

# key, name, type, price_per_unit, status
file = open('./CSV/Product.csv')
reader = csv.reader(file)
products = {}
for row in reader:
    products[row[0]] = row
file.close()

# research_budget, sales_total_revenue, product_key, event_key, affliction_key, country_key, year_key
file = open('./CSV/FactTable.csv')
reader = csv.reader(file)
data = []
for row in reader:
    researchBudget = convertToInt(row[0])
    salesTotalRevenue = convertToInt(row[1])
    productKey = row[2]
    eventKey = row[3]
    afflictionKey = row[4]
    countryKey = row[5]
    year = int(row[6])

    product = products[productKey]
    productType = productTypeEncoding(product[2])
    productPricePerUnit = convertToInt(product[3])
    productStatus = productStatusEncoding(product[4])

    event = events[eventKey]
    eventCountry = int(event[1])
    eventAttendance = convertToInt(event[3])

    affliction = afflictions[afflictionKey]
    country = countries[countryKey]
    countryRegion = countryRegionEncoding(country[2])
    countryGDP = convertToInt(country[3])
    countryLandlocked = booleanEncoding(country[4])
    countryPopulation = convertToInt(country[5])
    countryRural = booleanEncoding(country[6])

    if year < 2020:
        for i in afflictionHistories:
            if year == int(afflictionHistories[i][7]) and affliction[1] == afflictionHistories[i][1] and affliction[6] == afflictionHistories[i][6]:
                affliction = afflictionHistories[i]
                break

        for i in countryHistories:
            if year == int(countryHistories[i][2]) and country[0] == countryHistories[i][1]:
                countryPopulation = countryHistories[i][3]
                break
    
    afflictionCommunicable = booleanEncoding(affliction[2])
    afflictionCasesReported = convertToInt(affliction[3])
    afflictionDeathRate = convertToInt(affliction[4])
    afflictionImmunizationPercentage = convertToInt(affliction[5])
    afflictionCountry = int(affliction[6])

    data.append([researchBudget, salesTotalRevenue, productType, productPricePerUnit, productStatus, eventCountry, eventAttendance, afflictionCommunicable, afflictionCasesReported, afflictionDeathRate, afflictionImmunizationPercentage, afflictionCountry, countryRegion, countryGDP, countryLandlocked, countryPopulation, countryRural])
file.close()

a = numpy.array(data)
numpy.savetxt('preprocessed.csv', a, delimiter=',', fmt='%s')
