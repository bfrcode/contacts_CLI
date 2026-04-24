CREATE TABLE IF NOT EXISTS speciality (
    speciality_id INTEGER PRIMARY KEY,
    speciality_type TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS enterprise (
    enterprise_id INTEGER PRIMARY KEY,
    enterprise_name TEXT NOT NULL,
    enterprise_address TEXT,
    enterprise_phone TEXT,
    enterprise_mail TEXT,
    fk_speciality INTEGER,
    enterprise_note TEXT,
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
    fk_enterprise INTEGER,
    people_note TEXT,
    FOREIGN KEY (fk_enterprise)
        REFERENCES enterprise(enterprise_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

CREATE INDEX idx_people_name ON people(people_name);
CREATE INDEX idx_people_enterprise ON people(fk_enterprise);
CREATE INDEX idx_enterprise_name ON enterprise(enterprise_name);
CREATE INDEX idx_speciality_type ON speciality(speciality_type);