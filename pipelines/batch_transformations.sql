-- =============================================================================
-- PIPELINE DE TRANSFORMACIÓN BATCH (ELT EN BIGQUERY)
-- Proyecto: Smart Cold Chain IoT
-- Capas: Bronze -> Silver -> Gold (Esquema en Estrella)
-- =============================================================================

-- -----------------------------------------------------------------------------
-- 1. TRANSFORMACIÓN CAPA SILVER: LIMPIEZA, DEDUPLICACIÓN Y VALIDACIÓN
-- -----------------------------------------------------------------------------
INSERT INTO `myfirstproject-508413.cold_chain_db.silver_telemetria_clean`
(telemetria_id, device_id, timestamp, temperature, humidity, battery_pct, temp_valida, bateria_baja, fecha)
WITH deduplicated AS (
    SELECT 
        device_id,
        timestamp,
        temperature,
        humidity,
        battery_pct,
        -- Deduplicación por sensor y marca de tiempo
        ROW_NUMBER() OVER(PARTITION BY device_id, timestamp ORDER BY timestamp DESC) as rn
    FROM `myfirstproject-508413.cold_chain_db.bronze_telemetria`
    WHERE timestamp IS NOT NULL
)
SELECT 
    -- Generación de surrogate key (Llave subrogada determinística)
    TO_HEX(MD5(CONCAT(device_id, "-", CAST(timestamp AS STRING)))) AS telemetria_id,
    device_id,
    timestamp,
    temperature,
    humidity,
    battery_pct,
    -- Reglas de calidad de datos (Rango físico posible de operación)
    (temperature BETWEEN -50.0 AND 60.0 AND humidity BETWEEN 0.0 AND 100.0) AS temp_valida,
    (battery_pct < 20) AS bateria_baja,
    DATE(timestamp) AS fecha
FROM deduplicated
WHERE rn = 1
  AND (temperature BETWEEN -50.0 AND 60.0);

-- -----------------------------------------------------------------------------
-- 2. TRANSFORMACIÓN CAPA GOLD: TABLA DE HECHOS DE INCIDENTES (STAR SCHEMA)
-- Cruce multifuente (Streaming Silver + Dimensiones Batch de Catálogo)
-- -----------------------------------------------------------------------------
INSERT INTO `myfirstproject-508413.cold_chain_db.gold_fact_incidentes`
(incidente_id, timestamp, fecha, device_id, product_id, camara_almacen, responsable, temp_registrada, temp_limite, desviacion_grados, nivel_severidad, impacto_financiero_estimado)
SELECT 
    TO_HEX(MD5(CONCAT("INC-", s.telemetria_id))) AS incidente_id,
    s.timestamp,
    s.fecha,
    s.device_id,
    p.product_id,
    a.camara_almacen,
    a.responsable,
    s.temperature AS temp_registrada,
    CASE 
        WHEN s.temperature > p.temp_max THEN p.temp_max
        ELSE p.temp_min
    END AS temp_limite,
    -- Cálculo del exceso térmico
    ROUND(ABS(s.temperature - CASE WHEN s.temperature > p.temp_max THEN p.temp_max ELSE p.temp_min END), 2) AS desviacion_grados,
    -- Lógica de clasificación de severidad
    CASE 
        WHEN ABS(s.temperature - CASE WHEN s.temperature > p.temp_max THEN p.temp_max ELSE p.temp_min END) >= 5.0 THEN "CRÍTICA"
        WHEN ABS(s.temperature - CASE WHEN s.temperature > p.temp_max THEN p.temp_max ELSE p.temp_min END) >= 2.0 THEN "MODERADA"
        ELSE "LEVE"
    END AS nivel_severidad,
    -- Estimación del impacto financiero en dólares (Lote promedio = 50 unidades)
    ROUND(p.costo_unitario * 50 * (ABS(s.temperature - CASE WHEN s.temperature > p.temp_max THEN p.temp_max ELSE p.temp_min END) / 5.0), 2) AS impacto_financiero_estimado
FROM `myfirstproject-508413.cold_chain_db.silver_telemetria_clean` s
JOIN `myfirstproject-508413.cold_chain_db.dim_asignacion_sensores` a ON s.device_id = a.device_id
JOIN `myfirstproject-508413.cold_chain_db.dim_productos` p ON a.product_id = p.product_id
WHERE s.temperature > p.temp_max OR s.temperature < p.temp_min;

-- -----------------------------------------------------------------------------
-- 3. TRANSFORMACIÓN CAPA GOLD: RESUMEN ANALÍTICO DIARIO (AGREGACIONES EJECUTIVAS)
-- -----------------------------------------------------------------------------
INSERT INTO `myfirstproject-508413.cold_chain_db.gold_fact_resumen_diario`
(fecha, device_id, product_id, camara_almacen, total_lecturas, temp_promedio, temp_minima, temp_maxima, total_alertas, bateria_promedio, tiempo_fuera_rango_minutos)
SELECT 
    s.fecha,
    s.device_id,
    p.product_id,
    a.camara_almacen,
    COUNT(1) AS total_lecturas,
    ROUND(AVG(s.temperature), 2) AS temp_promedio,
    MIN(s.temperature) AS temp_minima,
    MAX(s.temperature) AS temp_maxima,
    COUNTIF(s.temperature > p.temp_max OR s.temperature < p.temp_min) AS total_alertas,
    ROUND(AVG(s.battery_pct), 1) AS bateria_promedio,
    -- Estimación de tiempo acumulado de exposición térmica (cada lectura representa ~0.5 min)
    CAST(ROUND(COUNTIF(s.temperature > p.temp_max OR s.temperature < p.temp_min) * 0.5) AS INT64) AS tiempo_fuera_rango_minutos
FROM `myfirstproject-508413.cold_chain_db.silver_telemetria_clean` s
JOIN `myfirstproject-508413.cold_chain_db.dim_asignacion_sensores` a ON s.device_id = a.device_id
JOIN `myfirstproject-508413.cold_chain_db.dim_productos` p ON a.product_id = p.product_id
GROUP BY s.fecha, s.device_id, p.product_id, a.camara_almacen;
