--Comparing the population between China and India--
SELECT DISTINCT "Country".name, "Country".population, "Fact Table".country_key
FROM ("Fact Table" INNER JOIN "Country" ON "Fact Table".country_key = "Country".country_key)
WHERE "Fact Table".country_key = 4 OR "Fact Table".country_key = 9