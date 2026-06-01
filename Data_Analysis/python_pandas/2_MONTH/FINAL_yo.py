import pandas as pd
from io import StringIO

# 1. PREPARACIÓN DE DATOS SIMULADOS
# Usamos StringIO para que pandas lo lea como si fuera un archivo real
datos_string = """id,producto,precio_unidad,cantidad,fecha
101, sUnScReEn SpRaY ,25.00,2,2026-05-20
102,HAIR SERUM,45.00,1,2026-05-21
103,french gray salt,12.50,4,2026-05-22"""

# Creamos el dataframe original y lo guardamos como CSV origen
df_inicial = pd.read_csv(StringIO(datos_string))
archivo_origen = "ventas_brutas.csv"
df_inicial.to_csv(archivo_origen, index=False)


# 2. COMPONENTES DEL PIPELINE ETL
def extraer(ruta_archivo):
    print(f"Extraer datos desde {ruta_archivo}...")
    return pd.read_csv(ruta_archivo)


def transformar_datos(df):
    print("Transformando datos...")
    # Agregamos los paréntesis () para hacer la copia correctamente
    df_limpio = df.copy()
    
    # Limpia espacios en blanco y convierte a mayúsculas
    df_limpio["producto"] = df_limpio["producto"].str.strip().str.upper()
    
    # Convierte la fecha a tipo datetime
    df_limpio["fecha"] = pd.to_datetime(df_limpio["fecha"])
    
    # Corrección de "canntidad" a "cantidad"
    df_limpio["total_ingreso"] = (
        df_limpio["precio_unidad"] * df_limpio["cantidad"]
    )
    
    # Filtra los ingresos mayores o iguales a 40
    df_filtrar = df_limpio[df_limpio["total_ingreso"] >= 40]
    return df_filtrar


def cargar_datos(df, ruta_salida):
    print(f"Guardando datos procesados en {ruta_salida}...")
    # Se corrige la extensión .cvs por .csv
    df.to_csv(ruta_salida, index=False)
    print("¡PIPELINE EJECUTADO CON ÉXITO!")
    

# 3. EJECUCIÓN DEL PIPELINE
if __name__ == "__main__":
    archivo_destino = "ventas_procesadas.csv"

    # Correr el flujo de manera ordenada
    df_origen = extraer(archivo_origen)
    df_transformado = transformar_datos(df_origen)
    cargar_datos(df_transformado, archivo_destino)
    
    # Opcional: Mostrar el resultado final en consola para verificar
    print("\nResultado Final:")
    print(df_transformado)