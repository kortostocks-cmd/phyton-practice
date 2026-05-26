-- =========================================
-- TABLA CLIENTES
-- =========================================

CREATE TABLE clientes (
    id INT PRIMARY KEY ,
    nombre VARCHAR(100),
    email VARCHAR(150),
    ciudad VARCHAR(100),
    fecha_registro DATETIME
);

-- =========================================
-- TABLA PRODUCTOS
-- =========================================

CREATE TABLE productos (
    id INT PRIMARY KEY ,
    nombre VARCHAR(120),
    categoria VARCHAR(80),
    precio DECIMAL(10,2),
    stock INT
);

-- =========================================
-- TABLA ORDENES
-- =========================================

CREATE TABLE ordenes (
    id INT PRIMARY KEY,
    cliente_id INT,
    producto_id INT,
    cantidad INT,
    total DECIMAL(10,2),
    estado VARCHAR(50),
    fecha_orden DATETIME,

    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

-- =========================================
-- INSERTAR CLIENTES
-- =========================================

INSERT INTO clientes (nombre, email, ciudad, fecha_registro)
VALUES
('Juan Perez', 'juan@gmail.com', 'Panama', CURRENT_TIMESTAMP),
('Maria Lopez', 'maria@gmail.com', 'Colon', CURRENT_TIMESTAMP),
('Carlos Ruiz', 'carlos@gmail.com', 'David', CURRENT_TIMESTAMP),
('Ana Torres', 'ana@gmail.com', 'Panama', CURRENT_TIMESTAMP),
('Luis Gomez', 'luis@gmail.com', 'Chitre', CURRENT_TIMESTAMP);

-- =========================================
-- INSERTAR PRODUCTOS
-- =========================================

INSERT INTO productos (nombre, categoria, precio, stock)
VALUES
('Laptop HP', 'Tecnologia', 1200.00, 15),
('Mouse Gamer', 'Tecnologia', 45.00, 100),
('Teclado Mecanico', 'Tecnologia', 80.00, 50),
('Monitor Samsung', 'Pantallas', 300.00, 20),
('iPhone', 'Telefonos', 999.00, 10);

-- =========================================
-- INSERTAR ORDENES
-- =========================================

INSERT INTO ordenes
(cliente_id, producto_id, cantidad, total, estado, fecha_orden)
VALUES
(1, 1, 1, 1200.00, 'entregado', NOW()),
(2, 2, 2, 90.00, 'pendiente', NOW()),
(3, 3, 1, 80.00, 'entregado', NOW()),
(1, 4, 1, 300.00, 'cancelado', NOW()),
(4, 5, 1, 999.00, 'pendiente', NOW());

-- =========================================
-- PRACTICAS
-- =========================================

-- 1. QUERY LENTA
SELECT * FROM ordenes
WHERE estado = 'pendiente';

-- CREA UN INDEX PARA MEJORARLA
CREATE INDEX idx_estado
ON ordenes(estado);

-- 2. QUERY CON JOIN
SELECT
    c.nombre,
    p.nombre,
    o.total
FROM ordenes o
JOIN clientes c ON o.cliente_id = c.id
JOIN productos p ON o.producto_id = p.id;

-- ANALIZA SI NECESITA INDEXES


-- 3. QUERY DE FECHAS
SELECT *
FROM ordenes
WHERE fecha_orden >= '2025-01-01';

-- CREA INDEX PARA FECHA


-- 4. QUERY CON ORDER BY
SELECT *
FROM productos
ORDER BY precio DESC;

-- REVISA PERFORMANCE


-- 5. QUERY CON GROUP BY
SELECT
    estado,
    COUNT(*) AS total_ordenes
FROM ordenes
GROUP BY estado;

-- AGREGA INDEX Y COMPARA


-- =========================================
-- TUS RETOS
-- =========================================

-- A) Crear index simple
-- B) Crear index compuesto
-- C) Usar EXPLAIN
-- D) Comparar antes y después
-- E) Encontrar full table scans
-- F) Probar queries malas y optimizarlas


-- =========================================
-- EJEMPLOS DE INDEXES
-- =========================================

-- INDEX SIMPLE
-- CREATE INDEX idx_estado ON ordenes(estado);

-- INDEX COMPUESTO
-- CREATE INDEX idx_estado_fecha
-- ON ordenes(estado, fecha_orden);

-- VER PLAN DE EJECUCION
-- EXPLAIN SELECT * FROM ordenes WHERE estado='pendiente';