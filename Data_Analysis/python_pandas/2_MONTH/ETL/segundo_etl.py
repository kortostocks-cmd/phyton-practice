import sqlite3

# EXTRACT
def extract():
    pedidos = [
        {"cliente": "Abra", "precio": 20, "cantidad": 3},
        {"cliente": "Luis", "precio": 15, "cantidad": 2}
    ]

    return pedidos

# TRANSFORM
def transform(pedidos):
    return [
        
        {"cliente": pedido["cliente"],
        "total": pedido["precio"] * pedido["cantidad"]
        }
        for pedido in pedidos
    ] 

    

# LOAD
def load(datos):
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ventas (
            cliente TEXT,
            total REAL
        )
    """)

    for fila in datos:
        cursor.execute("""
            INSERT INTO ventas (cliente, total)
            VALUES (?, ?)
        """, (fila["cliente"], fila["total"]))

    conexion.commit()
    conexion.close()

# RUN
def run_etl():
    pedidos = extract()
    limpios = transform(pedidos)
    load(limpios)

run_etl()