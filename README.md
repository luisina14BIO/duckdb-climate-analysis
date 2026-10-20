# Análisis de Datos Meteorológicos con DuckDB

Proyecto analítico que utiliza **DuckDB y SQL** para explorar registros diarios de temperatura de Central Park, Nueva York, utilizando un archivo CSV como fuente de datos.

El proyecto demuestra cómo realizar consultas analíticas directamente sobre archivos, sin necesidad de crear una base de datos persistente.

## Objetivos del Proyecto

* Consultar datos CSV directamente con DuckDB.
* Calcular estadísticas descriptivas y agregaciones de temperatura.
* Comparar patrones de temperatura por año y mes.
* Identificar los días con los mayores rangos diarios de temperatura.
* Aplicar controles básicos de calidad de datos y documentar los tiempos de ejecución de las consultas.

## Dataset

* **Fuente:** NOAA — Global Historical Climatology Network Daily (GHCN-Daily).
* **Estación:** Central Park, Nueva York (`USW00094728`).
* **Período disponible en el dataset procesado:** del 1 de enero de 2021 al 5 de febrero de 2025.
* **Registros:** 1.497 observaciones diarias.
* **Variables:** ID de estación, fecha, temperatura máxima (°C) y temperatura mínima (°C).

Fuente de datos: [NOAA GHCN-Daily — Estación de Central Park](https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/USW00094728.csv).

Durante la preparación de los datos, las temperaturas se convierten de décimas de grado Celsius a grados Celsius. El dataset procesado contiene un registro por fecha, con las temperaturas máximas y mínimas disponibles.

**Nota sobre la cobertura:** el año 2025 contiene únicamente 36 observaciones, desde el 1 de enero hasta el 5 de febrero. Por lo tanto, sus promedios anuales no deben compararse directamente con los promedios de años completos.

## Estructura del Proyecto

```text
duckdb-climate-analysis/
├── data/
│   └── climate_data.csv
├── 01_data_extraction.ipynb
├── analysis.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Tecnologías

* Python
* DuckDB
* SQL
* Pandas
* Jupyter Notebook

## Configuración y Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/luisina14BIO/duckdb-climate-analysis.git
cd duckdb-climate-analysis
```

### 2. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar el análisis

```bash
python analysis.py
```

El script lee `data/climate_data.csv`, crea una vista temporal en DuckDB, filtra los registros con temperaturas faltantes y ejecuta las consultas analíticas.

No se crea ningún archivo de base de datos persistente de DuckDB.

## Consultas Analíticas

El script incluye los siguientes análisis:

1. **Resumen general:** cantidad de registros, temperaturas máximas y mínimas promedio, y extremos históricos de temperatura.
2. **Comparación anual:** cantidad de observaciones y temperaturas promedio por año.
3. **Rango diario de temperatura:** las diez fechas con la mayor diferencia entre las temperaturas máximas y mínimas.
4. **Promedios mensuales:** temperaturas máximas y mínimas promedio agrupadas por mes calendario.
5. **Cobertura temporal:** primera y última fecha disponible, y cantidad de observaciones por año.

Estas consultas permiten aplicar agregaciones, agrupaciones, ordenamientos, métricas derivadas y validaciones de calidad de datos mediante SQL.

## Principales Hallazgos

* El dataset procesado contiene **1.497 observaciones**.
* Temperatura máxima diaria promedio: **17,62 °C**.
* Temperatura mínima diaria promedio: **9,87 °C**.
* Temperatura máxima diaria más alta registrada: **36,7 °C**.
* Temperatura mínima diaria más baja registrada: **−16,0 °C**.
* Julio presenta la temperatura máxima diaria promedio más alta entre los meses calendario incluidos en este dataset.
* El mayor rango diario de temperatura observado es de **27,6 °C**, el 23 de diciembre de 2022.

Los resultados describen las observaciones disponibles y no deben interpretarse como una evaluación climática completa.

## Tiempos de Ejecución de las Consultas

Tiempos de ejecución observados en el entorno de desarrollo:

| Consulta                    | Tiempo (segundos) |
| --------------------------- | ----------------: |
| Resumen general             |            0.2839 |
| Comparación anual           |            0.3490 |
| Rango diario de temperatura |            0.1767 |
| Promedios mensuales         |            0.2704 |

Estas mediciones incluyen la ejecución de las consultas y la conversión de los resultados a DataFrames de Pandas. Los tiempos pueden variar según el equipo y el entorno de ejecución.

## Enfoque de Diseño de Base de Datos

DuckDB se utiliza como un motor SQL analítico integrado. El archivo CSV se consulta directamente y la vista temporal existe únicamente durante la ejecución del script.

Este enfoque evita la necesidad de mantener un archivo de base de datos independiente y permite realizar análisis de datos estructurados mediante SQL.

## Mejoras Futuras

* Ampliar el dataset para incluir un año completo de 2025.
* Visualizar los patrones estacionales y anuales de temperatura.
* Comparar las tendencias de temperatura entre múltiples estaciones meteorológicas.


