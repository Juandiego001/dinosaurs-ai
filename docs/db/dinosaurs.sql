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
    'Stegosaurus stenops',
    'Stegosaurus',
    'Jurásico tardío',
    'Norteamérica',
    'Herbívoro',
    9.0,
    29.5,
    3000.0,
    6614.0,
    'Stegosaurus es fácilmente reconocible por las grandes placas óseas a lo largo de su espalda y las púas en su cola. Se cree que estas estructuras servían para la defensa, la regulación térmica o la exhibición.',
    'Ornithischia',
    'Stegosauridae',
    'Stegosaurus',
    'stenops',
    '["Su cerebro era del tamaño de una nuez en comparación con su cuerpo.", "Las placas de su espalda estaban cubiertas de piel y podían haber tenido colores vivos."]'
);


SELECT *
FROM dinosaurs;
-- SELECT * FROM dinosaurs WHERE nombre_comun = 'coelurus';
-- SELECT * FROM dinosaurs WHERE nombre_cientifico = 'Aardonyx' OR nombre_comun = 'Aardonyx' FOR JSON AUTO;

-- SELECT curiosidades FROM dinosaurs WHERE nombre_cientifico = 'Borogovia gracilicrus';
