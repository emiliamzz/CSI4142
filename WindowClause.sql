--Immunization percentage of all countries from 2005 to 2019 of HepB3
SELECT immunization_percentage, year_key, country_key FROM public."Affliction History"
WHERE name = 'HepB3'
