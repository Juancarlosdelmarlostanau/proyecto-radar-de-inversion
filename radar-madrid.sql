CREATE DATABASE IF NOT EXISTS radar_madrid_alquileres;

USE radar_madrid_alquileres;

DROP TABLE IF EXISTS demografia;
DROP TABLE IF EXISTS renta_distrito;
DROP TABLE IF EXISTS renta_seccion;
DROP TABLE IF EXISTS alquiler;
DROP TABLE IF EXISTS secciones;
DROP TABLE IF EXISTS distritos;

CREATE TABLE distritos
(cod_dis CHAR(7) NOT NULL,
PRIMARY KEY (cod_dis));

CREATE TABLE secciones
(cod_sec CHAR(10) NOT NULL,
cod_dis CHAR(7) NOT NULL,
PRIMARY KEY (cod_sec),
FOREIGN KEY (cod_dis) REFERENCES distritos (cod_dis));

CREATE TABLE alquiler
(cod_sec CHAR(10) NOT NULL,
año INT NOT NULL,
n_alquileres DOUBLE,
eur_m2_media DOUBLE,
eur_m2_p25 DOUBLE,
eur_m2_p75 DOUBLE,
alq_inmueble_media DOUBLE,
alq_inmueble_p25 DOUBLE,
alq_inmueble_p75 DOUBLE,
PRIMARY KEY (cod_sec, año),
FOREIGN KEY (cod_sec) REFERENCES secciones (cod_sec));

CREATE TABLE renta_seccion
(cod_sec CHAR(10) NOT NULL,
año INT NOT NULL,
renta_hogar DOUBLE,
renta_persona DOUBLE,
PRIMARY KEY (cod_sec, año),
FOREIGN KEY (cod_sec) REFERENCES secciones (cod_sec));

CREATE TABLE renta_distrito
(cod_dis CHAR(7) NOT NULL,
año INT NOT NULL,
renta_hogar DOUBLE,
renta_persona DOUBLE,
PRIMARY KEY (cod_dis, año),
FOREIGN KEY (cod_dis) REFERENCES distritos (cod_dis));

CREATE TABLE demografia
(cod_sec CHAR(10) NOT NULL,
año INT NOT NULL,
poblacion DOUBLE,
edad_media DOUBLE,
tam_hogar DOUBLE,
pct_unipersonal DOUBLE,
pct_65mas DOUBLE,
PRIMARY KEY (cod_sec, año),
FOREIGN KEY (cod_sec) REFERENCES secciones (cod_sec));

SHOW TABLES;























