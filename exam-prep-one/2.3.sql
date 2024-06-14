UPDATE animals
SET owner_id = (SELECT id FROM owners WHERE name = 'Kaloqn Stoqnov')
WHERE animals.owner_id IS NULL;