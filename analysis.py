from pathlib import Path
import duckdb
import time

# Ruta del archivo CSV limpio
CSV_PATH = Path(__file__).parent / "data" / "climate_data.csv"

# Verificar que el archivo de datos existe
if not CSV_PATH.exists():
    raise FileNotFoundError(
        f"No se encontró el archivo de datos: {CSV_PATH}"
    )

# Crear una conexión temporal a DuckDB en memoria
con = duckdb.connect(database=":memory:")


# Crear una vista temporal a partir del CSV y excluir temperaturas nulas

con.read_csv(str(CSV_PATH)).filter(
    "tmax_c IS NOT NULL AND tmin_c IS NOT NULL"
).create_view("climate_data", replace=True)

print("Vista temporal 'climate_data' creada correctamente.")

# Consulta 1: resumen general de las temperaturas del período

query_resumen = """
    SELECT
        COUNT(*) AS cantidad_registros,
        ROUND(AVG(tmax_c), 2) AS temperatura_maxima_promedio,
        ROUND(AVG(tmin_c), 2) AS temperatura_minima_promedio,
        ROUND(MAX(tmax_c), 2) AS temperatura_maxima_registrada,
        ROUND(MIN(tmin_c), 2) AS temperatura_minima_registrada
    FROM climate_data
"""

inicio = time.perf_counter()

resultado_resumen = con.execute(
    query_resumen).df()

tiempo = time.perf_counter() - inicio

print("\n--- Resumen general del período ---")
print(resultado_resumen.to_string(index=False))
print(f"Tiempo de ejecución: {tiempo:.4f} segundos")


# Consulta 2: resumen de temperaturas por año

query_anual = """
    SELECT
        EXTRACT(YEAR FROM CAST(date AS DATE)) AS anio,
        COUNT(*) AS cantidad_registros,
        ROUND(AVG(tmax_c), 2) AS tmax_promedio,
        ROUND(AVG(tmin_c), 2) AS tmin_promedio
    FROM climate_data
    GROUP BY anio
    ORDER BY anio
"""

inicio = time.perf_counter()

resultado_anual = con.execute(
    query_anual).df()

tiempo = time.perf_counter() - inicio

print("\n--- Temperaturas promedio por año ---")
print(resultado_anual.to_string(index=False))
print(f"Tiempo de ejecución: {tiempo:.4f} segundos")


# Consulta 3: días con mayor amplitud térmica

query_amplitud = """
    SELECT
        CAST(date AS DATE) AS fecha,
        ROUND(tmax_c, 2) AS temperatura_maxima,
        ROUND(tmin_c, 2) AS temperatura_minima,
        ROUND(tmax_c - tmin_c, 2) AS amplitud_termica
    FROM climate_data
    ORDER BY amplitud_termica DESC
    LIMIT 10
"""

inicio = time.perf_counter()

resultado_amplitud = con.execute(
    query_amplitud).df()

tiempo = time.perf_counter() - inicio

print("\n--- Top 10 días con mayor amplitud térmica ---")
print(resultado_amplitud.to_string(index=False))
print(f"Tiempo de ejecución: {tiempo:.4f} segundos")


# Consulta 4: temperatura máxima promedio por mes

query_mensual = """
    SELECT
        EXTRACT(MONTH FROM CAST(date AS DATE)) AS mes,
        COUNT(*) AS cantidad_registros,
        ROUND(AVG(tmax_c), 2) AS tmax_promedio,
        ROUND(AVG(tmin_c), 2) AS tmin_promedio
    FROM climate_data
    GROUP BY mes
    ORDER BY mes
"""

inicio = time.perf_counter()

resultado_mensual = con.execute(
    query_mensual).df()

tiempo = time.perf_counter() - inicio

print("\n--- Temperaturas promedio por mes ---")
print(resultado_mensual.to_string(index=False))
print(f"Tiempo de ejecución: {tiempo:.4f} segundos")


# Consulta 5: verificar la cobertura temporal de los datos

query_cobertura = """
    SELECT
        EXTRACT(YEAR FROM CAST(date AS DATE)) AS anio,
        MIN(CAST(date AS DATE)) AS primera_fecha,
        MAX(CAST(date AS DATE)) AS ultima_fecha,
        COUNT(*) AS cantidad_registros,
        COUNT(DISTINCT CAST(date AS DATE)) AS fechas_unicas
    FROM climate_data
    GROUP BY anio
    ORDER BY anio
"""

resultado_cobertura = con.execute(
    query_cobertura).df()

print("\n--- Cobertura temporal por año ---")
print(resultado_cobertura.to_string(index=False))