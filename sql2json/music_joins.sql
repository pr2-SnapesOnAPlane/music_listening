-- DROP DATABASE IF EXISTS music;
-- CREATE DATABASE music;

USE music;

-- create table named "music"
DROP TABLE IF EXISTS music;
CREATE TABLE music (
 main_genre VARCHAR(100),
 sub_genre VARCHAR(250),
 artist VARCHAR(100),
 title VARCHAR(250),
 cert_units_mm INTEGER(20)
);

-- Insert into music table
INSERT INTO music
-- Join artists with subgenre
SELECT main_genre.main_genre, subgenre.sub_genre, artists.artist, artists.title, artists.cert_units_mm 
FROM artists
LEFT OUTER JOIN subgenre ON
artists.index = subgenre.index
LEFT OUTER JOIN main_genre ON
subgenre.sub_genre = main_genre.genre;

USE music;
SELECT
json_object('Genre', main_genre,
'Artist', artist,
'Album Title', title,
'Cert Units', cert_units_mm)
from music
limit 5;


