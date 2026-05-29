import sqlite3
from datetime import datetime
import requests

API_URL = "https://api.open-meteo.com/v1/forecast?latitude=8.98&longitude=-79.52&current_weather=true"

#PASO 1 E EXTRACT
def extract():
    print("1. Buscando el clima en internet....")
    respuesta = requests.get(API_URL)
    respuesta.raise_for_status()
    return respuesta.json()["current_weather"]

#PASO 2 T TRANSFORM
def transform(datos_crudos):
    print("2. Limpiando datos y calculando grados...")
    temp_c = datos_crudos.get("temperature")

    #CREAMOS NUETRA CAJITA DE DATOS LIMPIOS
    datos_limpios = {
        "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperatura_c": temp_c,
        "temperatura_f": round((temp_c * 9 / 5) + 32, 2), # Aquí se aplica la fórmula farenheait
        "viento": datos_crudos.get("windspeed")
    }

    return datos_limpios

# PASO 3: CARGAR (Guardar en la jarra)
def load(datos_limpios):
    print("3. Guardando los datos en la libreta (Base de datos)...")
    conexion = sqlite3.connect("mi_libreta_del_clima.db")
    cursor = conexion.cursor()
    
    # Dibujamos la tabla si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clima (
            fecha_hora TEXT,
            temperatura_c REAL,
            temperatura_f REAL,
            viento REAL
        )
    """)

    # Anotamos los datos
    cursor.execute("""
        INSERT INTO clima (fecha_hora, temperatura_c, temperatura_f, viento)
        VALUES (?, ?, ?, ?) 
    """, (datos_limpios["fecha_hora"], datos_limpios["temperatura_c"], datos_limpios["temperatura_f"], datos_limpios["viento"]))
    conexion.commit()
    conexion.close()

# PASO 4: EL BOTÓN DE INICIO
def run_etl():
    try:
        naranjas = extract()            # Extraemos
        jugo = transform(naranjas)      # Transformamos
        load(jugo)                      # Cargamos 
        print("¡Éxito! Tu primer proceso ETL ha terminado.")
    except Exception as error:
        print(f"Oops, algo salió mal: {error}")

if __name__ == "__main__":
    run_etl()