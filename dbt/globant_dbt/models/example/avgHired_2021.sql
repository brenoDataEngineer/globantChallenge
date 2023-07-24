{{ config(materialized='table') }}

with hired_avg_2021 as (

SELECT  
    hired, 
    department, 
    year
FROM (
    SELECT 
        h.name,
        COUNT(h.id) AS hired,
        d.department,
        EXTRACT(YEAR FROM h.datetime) AS year,
        AVG(COUNT(h.id)) OVER (PARTITION BY EXTRACT(YEAR FROM h.datetime)) AS mean_hired
    FROM 
        globant_hired_employees AS h
    JOIN 
        globant_departments AS d ON d.id = h.department_id
    JOIN 
        globant_jobs AS j ON j.id = h.job_id
    GROUP BY 
        h.name, d.department, EXTRACT(YEAR FROM h.datetime)
) AS subquery
WHERE 
    year = 2021 AND hired > mean_hired

)

select hired, 
    department, 
    year
from hired_avg_2021









