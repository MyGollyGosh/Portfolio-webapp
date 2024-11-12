DROP TABLE IF EXISTS test_table;

CREATE TABLE test_table (id SERIAL PRIMARY KEY, name VARCHAR(255));

INSERT INTO test_table (name) VALUES ('first_record');