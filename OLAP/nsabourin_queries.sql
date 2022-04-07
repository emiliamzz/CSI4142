/* Slice */

SELECT "Fact Table".sales_total_revenue, "Product".name
FROM "Fact Table" INNER JOIN "Product" ON "Product".product_key = "Fact Table".product_key
WHERE "Fact Table".year_key = 2020;


/* Iceberg Query */

SELECT "Product".name, "Fact Table".sales_total_revenue 
FROM "Fact Table" INNER JOIN "Product" ON "Product".product_key = "Fact Table".product_key 
WHERE year_key = 2020 
ORDER BY sales_total_revenue DESC 
LIMIT 10;

/* Drill Down and Slice */

SELECT "Fact Table".sales_total_revenue, "Event".name, "Country".region 
FROM ("Fact Table" INNER JOIN "Country" ON "Fact Table".country_key = "Country".country_key) 
INNER JOIN "Event" ON "Event".event_location_country = "Fact Table".country_key 
WHERE "Country".region = 'North America' AND "Fact_table".year_key = 2020;

SELECT "Fact Table".sales_total_revenue, "Event".name, "Country".name 
FROM ("Fact Table" INNER JOIN "Country" ON "Fact Table".country_key = "Country".country_key) 
INNER JOIN "Event" ON "Event".event_location_country = "Fact Table".country_key 
WHERE "Country".name = 'Canada' AND "Fact_table".year_key = 2020;

SELECT "Fact Table".sales_total_revenue, "Event".name, "Event".specific_location 
FROM ("Fact Table" INNER JOIN "Country" ON "Fact Table".country_key = "Country".country_key) 
INNER JOIN "Event" 
ON "Event".event_location_country = "Fact Table".country_key 
WHERE "Event".specific_location = 'Pontiac' AND "Fact_table".year_key = 2020;


/* Rollup and Slice */

SELECT "Country".region, SUM("Fact Table".sales_total_revenue)
FROM "Fact Table" INNER JOIN "Country" ON "Fact Table".country_key = "Country".country_key
WHERE "Fact Table".year_key = 2020 GROUP BY "Country".region;




