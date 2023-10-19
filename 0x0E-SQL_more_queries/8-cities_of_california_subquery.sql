-- SELECT FROM DB and its table
SELECT id, name FROM cities, states WHERE cities.id = states.id ORDER BY cities.id ASC;
