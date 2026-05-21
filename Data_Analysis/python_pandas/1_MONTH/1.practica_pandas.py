# -*- coding: utf-8 -*-
"""
Práctica de Pandas - Análisis de Paradas Policiales
Ubicación original: Google Colab
https://colab.research.google.com/drive/1X6Y7rhkHdrrVMFrYs5_Gi9Qf6hIUFE5A#scrollTo=Uuq0xbHzlf3y
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configuración para visualización de gráficos
# %matplotlib inline # Solo necesario en Notebooks; en VS Code usa plt.show() si es necesario

# --- CARGA DE DATOS ---
url = 'https://raw.githubusercontent.com/justmarkham/pycon-2018-tutorial/master/police.csv'
ri = pd.read_csv(url)

# --- EXPLORACIÓN INICIAL ---
ri.head()  # Vista previa de la tabla
ri.shape   # Filas y columnas
ri.dtypes  # Tipos de datos (float para decimales, int para enteros)
ri.isnull().sum() # Conteo de valores nulos

# --- DATASET 1: LIMPIEZA ---

## 1. Eliminar columnas con valores faltantes
# Eliminamos 'county_name' porque está vacía
ri.drop('county_name', axis='columns', inplace=True)

# Verificación de la limpieza
ri.dropna(axis='columns', how='all').isnull().sum()
ri.shape    # Debería mostrar 14 columnas
ri.columns  # Confirmamos que 'county_name' ya no está

# --- ANÁLISIS POR GÉNERO ---

### 2. ¿Quién comete más excesos de velocidad: hombres o mujeres?
ri[ri.violation == 'Speeding'].driver_gender.value_counts()

# Promedio (Normalizado)
ri[ri.violation == 'Speeding'].driver_gender.value_counts(normalize=True)

# Comparativa de violaciones por cada género
ri[ri.driver_gender == 'M'].violation.value_counts(normalize=True) # Hombres
ri[ri.driver_gender == 'F'].violation.value_counts(normalize=True) # Mujeres

# Uso de GroupBy para análisis conjunto
ri.groupby('driver_gender').violation.value_counts(normalize=True)
ri.groupby('driver_gender').violation.value_counts(normalize=True).loc[:, 'Speeding']

### 3. ¿Afecta el género a quién es requisado durante una parada?
ri.search_conducted.value_counts(normalize=True)
ri.search_conducted.mean() # Promedio de casos positivos (True)

ri.groupby('driver_gender').search_conducted.mean()
ri.groupby(['violation', 'driver_gender']).search_conducted.mean()

# --- ANÁLISIS DE BÚSQUEDAS (SEARCH) ---

## 4. ¿Por qué falta tanto el dato en 'search_type'?
ri.isnull().sum()
ri.search_conducted.value_counts() # Coincide con los nulos de search_type

# Verificación de nulos cuando no hubo búsqueda
ri[ri.search_conducted == False].search_type.value_counts(dropna=False)

### 5. Durante una búsqueda, ¿qué tan seguido se cachea al conductor?
ri['frisk'] = ri.search_type.str.contains('Protective Frisk')
ri.frisk.value_counts(dropna=False)
ri.frisk.sum()  # Total de True
ri.frisk.mean() # Tasa de cacheo (Frisk Rate)

# --- ANÁLISIS TEMPORAL ---

### 6. ¿Qué año tuvo el menor número de paradas?
# Conversión a formato Datetime
combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')
ri['stop_datetime'] = pd.to_datetime(combined)

ri.stop_datetime.dt.year.value_counts()

### 7. ¿Cómo cambia la actividad de drogas según la hora del día?
ri.groupby(ri.stop_datetime.dt.hour).drugs_related_stop.mean().plot()
plt.title('Actividad de drogas por hora')
# plt.show() # Descomenta si usas VS Code para ver la gráfica

# --- VISUALIZACIÓN DE TENDENCIAS ---

### 8. ¿La mayoría de las paradas ocurren de noche?
ri.stop_datetime.dt.hour.value_counts().sort_index().plot()

# Análisis por rangos horarios
ri[(ri.stop_datetime.dt.hour > 4) & (ri.stop_datetime.dt.hour < 22)].shape

# --- LIMPIEZA DE DATOS ERRÓNEOS ---

### 9. Corregir datos mal ingresados en 'stop_duration'
# Identificar datos basura ('1' y '2') y convertirlos a NaN real de Numpy
ri.loc[(ri.stop_duration == '1') | (ri.stop_duration == '2'), 'stop_duration'] = np.nan

# Verificación final
ri.stop_duration.value_counts(dropna=False)


