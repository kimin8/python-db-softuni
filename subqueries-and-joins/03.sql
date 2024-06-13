SELECT
    e.employee_id,
    CONCAT(e.first_name, ' ', e.last_name) AS full_name,
    ep.project_id,
    p.name
FROM employees AS e
    JOIN employees_projects AS ep
        ON e.employee_id = ep.employee_id
    JOIN projects AS p
        ON ep.project_id = p.project_id
WHERE ep.project_id = 1;

/*
Done using subquery

SELECT
    e.employee_id,
    CONCAT(e.first_name, ' ', e.last_name) AS full_name,
    ep.project_id,
    (SELECT name FROM projects WHERE projects.project_id = ep.project_id )
FROM employees AS e
    JOIN employees_projects AS ep
        ON e.employee_id = ep.employee_id
WHERE ep.project_id = 1;

*/