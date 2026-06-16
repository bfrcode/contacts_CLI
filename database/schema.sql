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
    fk_speciality INTEGER,
    company_note TEXT,
    FOREIGN KEY (fk_speciality)
        REFERENCES speciality(speciality_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS people (
    people_id INTEGER PRIMARY KEY,
    people_first_name TEXT NOT NULL,
    people_name TEXT NOT NULL,
    people_phone_number TEXT,
    people_mail TEXT,
    fk_company INTEGER,
    people_note TEXT,
    FOREIGN KEY (fk_company)
        REFERENCES company(company_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_people_name ON people(people_name);
CREATE INDEX IF NOT EXISTS idx_people_company ON people(fk_company);
CREATE INDEX IF NOT EXISTS idx_company_name ON company(company_name);
CREATE INDEX IF NOT EXISTS idx_speciality_type ON speciality(speciality_type);