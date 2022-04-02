--Drill down and drice of products of type oral that have been canceled post market, comparing price per unit
SELECT name, price_per_unit FROM public."Product"
WHERE type = 'Oral' AND status = 'Cancelled Post Market'
