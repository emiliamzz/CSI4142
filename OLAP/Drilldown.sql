-- Add specific region to Fact Table.

SELECT "Fact Table".research_budget, "Fact Table".product_key, "Fact Table".event_key, "Fact Table".affliction_key, "Fact Table".country_key, "Fact Table".year_key, "Event".specific_location
FROM "Fact Table"
INNER JOIN "Event" ON "Fact Table".country_key = "Event".event_location_country;
