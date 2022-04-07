-- Rollup the fact table to be per region and dice to show the total_sales_revenue per region per product in the year 2015.

SELECT "Country".region, SUM("Fact Table".sales_total_revenue) sales_total_revenue, "Fact Table".product_key, "Fact Table".year_key
FROM "Fact Table"
INNER JOIN "Country" ON "Fact Table".country_key = "Country".country_key
WHERE "Fact Table".year_key = 2015
GROUP BY ("Country".region, "Fact Table".product_key, "Fact Table".year_key);
