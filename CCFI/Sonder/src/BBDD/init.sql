
-- Crea la tabla cancion
CREATE TABLE cancion (
    id INT PRIMARY KEY,
    artista VARCHAR(255),
    titulo VARCHAR(255),
    letra TEXT,
    popularidad DECIMAL(5, 2)
);

-- Inserta los datos desde el CSV
LOAD DATA INFILE '/var/lib/mysql-files/canciones2.csv '
INTO TABLE cancion
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';