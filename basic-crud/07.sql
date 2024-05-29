CREATE VIEW hr_result AS
SELECT employees.id, employees.first_name, employees.last_name,
       employees.job_title, employees.department_id, employees.salary
FROM employees ORDER BY salary DESC LIMIT 1;

SELECT * FROM hr_result;