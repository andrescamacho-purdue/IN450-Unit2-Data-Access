-- IN450 Unit 2 — Create Tables and Load CSVs

CREATE TABLE IF NOT EXISTS in450a(
    time DECIMAL,
    source INET,
    destination INET,
    packets INTEGER,
    bytes BIGINT
);

CREATE TABLE IF NOT EXISTS in450b(
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS in450c(
    domain VARCHAR(100),
    description VARCHAR(255)
);

-- Load data from CSVs
\copy in450a FROM '/Users/L015811/Library/CloudStorage/OneDrive-EliLillyandCompany/2025/Software Engineering Apprenticeship/IN450/Unit2/Andres_Camacho_Unit2_IN450/in450a.csv' WITH (FORMAT csv, HEADER true);
\copy in450b FROM '/Users/L015811/Library/CloudStorage/OneDrive-EliLillyandCompany/2025/Software Engineering Apprenticeship/IN450/Unit2/Andres_Camacho_Unit2_IN450/in450b.csv' WITH (FORMAT csv, HEADER true);
\copy in450c FROM '/Users/L015811/Library/CloudStorage/OneDrive-EliLillyandCompany/2025/Software Engineering Apprenticeship/IN450/Unit2/Andres_Camacho_Unit2_IN450/in450c.csv' WITH (FORMAT csv, HEADER true);

-- Quick verification
SELECT COUNT(*) AS rows_in450a FROM in450a;
SELECT COUNT(*) AS rows_in450b FROM in450b;
SELECT COUNT(*) AS rows_in450c FROM in450c;