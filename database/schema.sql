CREATE TABLE IF NOT EXISTS speciality (
    speciality_id INTEGER PRIMARY KEY,
    speciality_type TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS company (
    company_id INTEGER PRIMARY KEY,
    company_name TEXT NOT NULL UNIQUE,
    company_address TEXT,
    company_phone TEXT,
    company_mail TEXT,
    company_note TEXT
);

CREATE TABLE IF NOT EXISTS company_speciality (
    fk_company_id INTEGER NOT NULL,
    fk_speciality_id INTEGER NOT NULL,
    is_main INTEGER NOT NULL DEFAULT 0 CHECK (is_main IN (0, 1)),
    PRIMARY KEY (fk_company_id, fk_speciality_id),
    FOREIGN KEY (fk_company_id)
        REFERENCES company(company_id)
        ON DELETE CASCADE,

    FOREIGN KEY (fk_speciality_id)
        REFERENCES speciality(speciality_id)
        ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS people (
    people_id INTEGER PRIMARY KEY,
    people_first_name TEXT NOT NULL,
    people_name TEXT NOT NULL,
    people_phone_number TEXT,
    people_mail TEXT,
    fk_company_id INTEGER,
    people_note TEXT,
    FOREIGN KEY (fk_company_id)
        REFERENCES company(company_id)
        ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_people_name ON people(people_name);
CREATE INDEX IF NOT EXISTS idx_people_company ON people(fk_company_id);
CREATE UNIQUE INDEX IF NOT EXISTS idx_one_main ON company_speciality(fk_company_id) WHERE is_main = 1;
CREATE INDEX IF NOT EXISTS idx_speciality_id ON company_speciality(fk_speciality_id);