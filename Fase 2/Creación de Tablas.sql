CREATE TABLE Clientes (
    Apellido_nombre NVARCHAR2(50),
    Ciudad NVARCHAR2(50),
    Especialidad NVARCHAR2(50),
    Direccion NVARCHAR2(50)
);


CREATE TABLE DMF (
    Apellido_nombre NVARCHAR2(50),
    Prescriber_id_bridge NUMERIC PRIMARY KEY,
    Adress_city NVARCHAR2(50),
    Specialty_id_1 NVARCHAR2(50),
    Dirección NVARCHAR2(50)
);
