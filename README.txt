CREATE DATABASE contactosdb;
USE contactosdb;

CREATE TABLE contactos(
    id int primary key auto_increment,
    nombres varchar(20),
    telefono varchar(20),
    email varchar(150)

);    






CREATE TABLE productos(
    id int primary key auto_increment,
    producto varchar(50),
    description varchar(50),
    marca varchar(30),
    precio int,
    stock int

);

INSERT INTO productos(description,marca,precio,stock) VALUES ('Licuadora estandar', 'Oster', 25, 2);


# Eliminar una columna
ALTER TABLE productos DROP producto;

# Agregar columna
ALTER TABLE productos ADD producto VARCHAR(20) FIRST;
ALTER TABLE productos ADD producto VARCHAR(20) AFTER id;
