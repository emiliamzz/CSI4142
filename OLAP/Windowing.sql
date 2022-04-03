-- Compare the sales total revenue of a product per country with the aveage sales total revenue for the product.

SELECT "Fact Table".country_key,
    "Fact Table".product_key,
    "Fact Table".sales_total_revenue,
    AVG("Fact Table".sales_total_revenue)
    OVER (PARTITION BY "Fact Table".product_key) AS average_sales_total_revenue
FROM "Fact Table";
