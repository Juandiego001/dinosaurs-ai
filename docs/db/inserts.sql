-- Inserción de datos de prueba de Usuarios
INSERT INTO users(
    full_name,
    email,
    password,
    document
)
VALUES (
    'Administrador',
    'juandiego14012003@gmail.com',
    '$2b$12$MXknq8MdOIZIpwnAVNRZD.rM3iWzWPCB.c5vohyqQo8N2Qd03WhyO',
    '1006307292'
);


-- Inserción de grupo administradores
INSERT INTO groups(name) VALUES ('Administradores');

-- Inserción de módulos
INSERT INTO modules(name) VALUES ('users'), ('groups');

-- Inserción de permisos
INSERT INTO permissions(group_id, module_id, "read", "create", "update", "delete")
VALUES (1, 1, true, true, true, true), (1, 2, true, true, true, true);

-- Inserción de user_groups
INSERT INTO user_groups(user_id, group_id)
VALUES (3, 1);

-- Inserción de módulo de searches
INSERT INTO modules(name) VALUES ('searches');

-- Inserción de módulo de dinosaurs
INSERT INTO modules(name) VALUES ('dinosaurs');

-- Inserción de módulo de forums
INSERT INTO modules(name) VALUES ('forums');

-- Inserción de módulo de strapi
INSERT INTO modules(name) VALUES ('strapi');

-- Inserción de permiso de visualización de searches
-- Validar ID del módulo y del grupo!
INSERT INTO permissions(group_id, module_id, "read", "create", "update", "delete")
VALUES (1, 3, true, true, true, true), (1, 2, true, true, true, true);


-- Inserción de permiso de visualización de dinosaurs
INSERT INTO permissions(group_id, module_id, "read", "create", "update", "delete")
VALUES (1, 4, true, true, true, true);


-- Inserción de permiso de visualización de forums
INSERT INTO permissions(group_id, module_id, "read", "create", "update", "delete")
VALUES (1, 5, true, true, true, true);


-- Inserción de permiso de visualización de strapi
INSERT INTO permissions(group_id, module_id, "read", "create", "update", "delete")
VALUES (1, 6, true, true, true, true);