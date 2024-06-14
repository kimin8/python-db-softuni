CREATE OR REPLACE FUNCTION fn_full_name(first_name VARCHAR, last_name VARCHAR)
RETURNS VARCHAR AS
$$
    DECLARE
        full_name VARCHAR;

    BEGIN
        full_name := CONCAT(INITCAP($1), ' ', INITCAP($2));
        RETURN full_name;
    END
$$
LANGUAGE plpgsql;