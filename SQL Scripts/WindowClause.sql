--Immunization percentage of Canada from 2005 to 2019 of HepB3
SELECT Distinct "Affliction History".immunization_percentage, "Affliction History".name, "Fact Table".year_key, "Fact Table".country_key, "Country".name
FROM ("Fact Table" INNER JOIN "Affliction History" ON "Fact Table".year_key = "Affliction History".year_key AND "Fact Table".country_key = "Affliction History".country_key
	 INNER JOIN "Country" ON "Fact Table".country_key = "Country".country_key
	 )
WHERE "Affliction History".name = 'HepB3' AND "Fact Table".country_key = 1
WINDOW "Fact Table" AS(
	PARTITION BY "Affliction History".immunization_percentage
	ORDER BY "Fact Table".year_key
)