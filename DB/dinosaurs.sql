-- CREATE TABLE dinosaurs (
--     id INT IDENTITY(1,1) PRIMARY KEY,  -- ID único del dinosaurio
--     nombre_cientifico VARCHAR(255) NOT NULL,  -- Nombre científico
--     nombre_comun VARCHAR(255),  -- Nombre común
--     periodo VARCHAR(100),  -- Período geológico
--     habitat TEXT,  -- Descripción del hábitat
--     dieta VARCHAR(100),  -- Dieta (carnívoro, herbívoro, etc.)
--     longitud_metros DECIMAL(5,2),  -- Longitud en metros
--     longitud_pies DECIMAL(5,2),  -- Longitud en pies
--     peso_kg DECIMAL(10,2),  -- Peso en kilogramos
--     peso_lb DECIMAL(10,2),  -- Peso en libras
--     descripcion TEXT,  -- Descripción detallada
--     clasificacion_orden VARCHAR(100),  -- Orden taxonómico
--     clasificacion_familia VARCHAR(100),  -- Familia taxonómica
--     clasificacion_genero VARCHAR(100),  -- Género taxonómico
--     clasificacion_especie VARCHAR(100),  -- Especie taxonómica
--     curiosidades TEXT,  -- Curiosidades en formato JSON o texto
-- );

INSERT INTO dinosaurs
(nombre_cientifico, nombre_comun, periodo, habitat, dieta, longitud_metros, longitud_pies, peso_kg, peso_lb, descripcion, clasificacion_orden, clasificacion_familia, clasificacion_genero, clasificacion_especie, curiosidades)
VALUES
(
    'Camarasaurus supremus', 'Camarasaurus', 'Jurásico tardío', 'Norteamérica', 'Herbívoro', 18.0, 59.1, 20000.0, 44092.5, 'Un saurópodo robusto con un cuello fuerte y cabeza cuadrada.', 'Saurischia', 'Camarasauridae', 'Camarasaurus', 'supremus', '["Era uno de los saurópodos más comunes de Norteamérica.", "Sus dientes eran más resistentes que los de otros saurópodos."]'
)


SELECT * FROM dinosaurs;


