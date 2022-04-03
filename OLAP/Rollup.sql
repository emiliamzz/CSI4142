-- Rollup the fact table to be per region.

SELECT "Country".region, SUM("Fact Table".sales_total_revenue) sales_total_revenue, SUM("Fact Table".research_budget) research_budget, "Fact Table".product_key, "Fact Table".event_key, "Fact Table".affliction_key, "Fact Table".year_key
FROM "Fact Table"
INNER JOIN "Country" ON "Fact Table".country_key = "Country".country_key
GROUP BY ("Country".region, "Fact Table".product_key, "Fact Table".event_key, "Fact Table".affliction_key, "Fact Table".year_key);
