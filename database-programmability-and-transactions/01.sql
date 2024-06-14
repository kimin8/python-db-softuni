CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INT AS
$$
    DECLARE
        result INT;

    BEGIN
        SELECT
            COUNT(*) INTO result
        FROM towns AS t
            JOIN addresses AS a
                USING(town_id)
                    JOIN employees AS e
                        USING(address_id)
        WHERE t.name = town_name;
        RETURN result;
    END;
$$
LANGUAGE plpgsql;