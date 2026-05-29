#ETL COMPLETO ESTRUCTURA Pipeline
import sqlite3
from io import StringIO
import pandas as pd

# Datos CSV
datos = """
id,producto,precio_unidad,cantidad,fecha
101, sUnScReEn SpRaY ,25.00,2,2026-05-20
102,HAIR SERUM,45.00,1,2026-05-21
103,french gray salt,12.50,4,2026-05-22
"""

df = pd.DataFrame(datos)
df.to_csv("ventas_brutas.csv", index=False)

def extraer():
    print("Extrayendo datos desde cvs....")
    return pd.read_csv("ventas_brutas.cvs")

def transformar_datos(df):
    df_limpio = df.copy()
    
    #limpiar espacios y mayusculas
    df_limpio["producto"] = df_limpio["producto"].str.strip().str.upper()
    #Limpieza tiempo: asegurar formato de fecha correcta
    df_limpio["fecha"] = pd.to_datetime(df_limpio["fecha"])
    #Transformacion: calcular una nueva columna (ingreso total)
    df_limpio["total_ingreso"]= (
        df_limpio["precio_unidad"] * df_limpio["cantidad"]
    )

    df_filtrar = df_limpio[df_limpio["total_ingreso"]  >= 40]
    return df_filtrar



def cargar_datos(df, ruta_salida):
    print(f"Guradando datos procesados en {ruta_salida}...")
    # index = false evita que se guarde la columna de indices de pandas
    df.to_csv(ruta_salida, index=False)
    print("pipeline ejecutado")

#E EJECUCION
if __name__ == "__main__":
    archivo_origen = "ventas_brutas.csv"
    archivo_destino ="ventas_procesadas.cvs"

# Correr el flujo
df_origen = extraer_datos(archivo_origen)
df_transformado = transformar_datos(df_origen)
cargar_datos(df_transformado,archivo_destino)