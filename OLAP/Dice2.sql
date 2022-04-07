--Comparing the GDP between Canada and South Africa--
SELECT DISTINCT "Country".name, "Country".gdp, "Fact Table".country_key
FROM ("Fact Table" INNER JOIN "Country" ON "Fact Table".country_key = "Country".country_key)
WHERE "Fact Table".country_key = 1 OR "Fact Table".country_key = 6