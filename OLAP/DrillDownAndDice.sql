--Drill down and drice of products of type oral that have been canceled post market, comparing price per unit
SELECT "Product".name, "Product".price_per_unit, "Product".type, "Product".status, "Fact Table".product_key
FROM ("Fact Table" INNER JOIN "Product" ON "Fact Table".product_key = "Product".product_key)
WHERE type = 'Oral' AND status = 'Cancelled Post Market'
