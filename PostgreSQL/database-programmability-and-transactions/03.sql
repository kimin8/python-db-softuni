CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id(
    id INT
) AS
$$
    BEGIN
        UPDATE
            employees
        SET
            salary = salary * 1.05
        WHERE
            $1 = employee_id;

        IF (SELECT salary FROM employees WHERE employee_id = $1) IS NULL THEN
            ROLLBACK;
            RETURN;
        END IF;

        COMMIT;
    END;
$$
LANGUAGE plpgsql;



CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id(
    id INT
) AS
$$
    BEGIN
        IF (SELECT COUNT(employee_id) FROM employees WHERE employee_id = id) != 1 THEN
            ROLLBACK;
        ELSE
            UPDATE
                employees
           SET
                salary = 1.05 * salary
            WHERE
                employee_id = id;
        END IF;
        COMMIT;
    END;
$$
LANGUAGE plpgsql;