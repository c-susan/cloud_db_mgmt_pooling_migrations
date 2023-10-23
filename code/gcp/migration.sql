CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 8a2ccec82ca8

INSERT INTO alembic_version (version_num) VALUES ('8a2ccec82ca8');

-- Running upgrade 8a2ccec82ca8 -> 36a65470de6c

ALTER TABLE doctors ADD COLUMN extension VARCHAR(10);

UPDATE alembic_version SET version_num='36a65470de6c' WHERE alembic_version.version_num = '8a2ccec82ca8';

