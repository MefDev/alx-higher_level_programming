-- SELECT FROM DB and its table
SELECT cs.id, cs.name, ss.name FROM cities cs JOIN states ss ON cs.state_id = ss.id ORDER BY cs.id ASC;

