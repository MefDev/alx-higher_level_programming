-- CRreate a unique id for a user from DB
CREATE TABLE IF NOT EXISTS unique_id
(id INT DEFAULT 1, name VARCHAR(256), UNIQUE(id));

