-- A table with a unique Id
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    NAME varchar(256)
);