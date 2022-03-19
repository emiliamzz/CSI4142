import random

def toStr(item):
    return "\'" + str(item) + "\'"

def randomPrice():
    return round(random.uniform(1.00, 1000.00), 2)

def randomBudget():
    return round(random.uniform(1.00, 1000000.00), 2)

f = open("facttable.sql", "w")

for i in range(54073):
    for x in range (206):
        for z in range(126):
            for l in range (9):
                for y in range (16):
                    revenue = randomPrice()
                    budget = randomBudget()
                    f.write("INSERT INTO \"Fact Table\" (research_budget, sales_total_revenue, product_key, event_key, affliction_key, country_key, year_key) VALUES (" + toStr(budget) + ", " + toStr(revenue) + ", " + toStr(i) + ", " + toStr(x) + ", " + toStr(z) + ", " + toStr(l) + ", " + toStr(y) + ");\n")

f.close()
