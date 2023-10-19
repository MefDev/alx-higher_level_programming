-- SELECT FROM DB and its table
SELECT cs.id, cs.name FROM cities cs, states ss WHERE cs.id = ss.id ORDER BY cs.id ASC;

