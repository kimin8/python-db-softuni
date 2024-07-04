SELECT
    t.town_id AS town_id,
    t.name AS town_name,
    a.address_text AS address_text
FROM towns AS t
    JOIN addresses AS a
        ON t.town_id = a.town_id
WHERE name IN ('Sofia', 'San Francisco', 'Carnation')
ORDER BY town_id, address_id;