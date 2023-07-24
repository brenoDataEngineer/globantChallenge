{{ config(materialized='table') }}

with hired_jobs_departments as (

    SELECT EXTRACT(QUARTER FROM h.datetime) AS quarterYear,
    d.department, j.job, count(h.id) as quantity
    FROM globant_hired_employees as h
    JOIN globant_departments as d ON d.id = h.department_id
    JOIN globant_jobs as j ON j.id = h.job_id
    GROUP BY EXTRACT(QUARTER FROM h.datetime), d.department, j.job
    ORDER BY quarterYear
        

)

select *
from hired_jobs_departments
