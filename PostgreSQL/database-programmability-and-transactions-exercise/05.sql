CREATE OR REPLACE FUNCTION fn_difficulty_level(IN level INT)
RETURNS VARCHAR AS
$$
    DECLARE
        difficulty_level VARCHAR;
    BEGIN
        IF
            level <= 40
            THEN
                difficulty_level := 'Normal Difficulty';
        ELSEIF
            level BETWEEN 41 AND 60
            THEN
                difficulty_level := 'Nightmare Difficulty';
        ELSEIF
            level > 60
            THEN
            difficulty_level := 'Hell Difficulty';
        END IF;
        RETURN difficulty_level;
    END;
$$
LANGUAGE plpgsql;

SELECT
    "user_id",
    "level",
    "cash",
    fn_difficulty_level(users_games.level)
FROM
    users_games
ORDER BY
    user_id;