CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 0b5b57f03435

INSERT INTO alembic_version (version_num) VALUES ('0b5b57f03435');

-- Running upgrade 0b5b57f03435 -> 1d16c6290170

ALTER TABLE patients ADD COLUMN gender VARCHAR(10) NOT NULL;

UPDATE alembic_version SET version_num='1d16c6290170' WHERE alembic_version.version_num = '0b5b57f03435';
