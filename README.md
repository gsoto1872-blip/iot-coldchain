# Proyecto IoT: Smart Cold Chain (Cadena de Frío Inteligente)

Arquitectura End-to-End y Capa de Procesamiento / Transformación en Google Cloud Platform (GCP).

---

## 🏛️ 1. Arquitectura de Datos (Medallion & Star Schema)

```
[ Sensores IoT (Streaming) ]       [ ERP / Catálogos (Batch) ]
             │                                   │
             ▼                                   ▼
    Cloud Pub/Sub (Broker)               Cloud Storage (GCS)
             │                                   │
  ┌──────────┴──────────────┐                    │
  ▼                         ▼                    │
Hot Path (<1s)          Cold Path                │
Stream Processor      BigQuery Direct Ingest     │
(Alertas en Vivo)           │                    │
                            ▼                    │
                   [ Capa Bronze: Raw ]          │
                 bronze_telemetria ◄─────────────┘
                            │
                            ▼
                  [ Capa Silver: Clean ]
                silver_telemetria_clean
               (Deduplicada, Tipificada)
                            │
            ┌───────────────┴───────────────┐
            ▼                               ▼
 [ Capa Gold: Fact Incidentes ]   [ Capa Gold: Fact Resumen Diario ]
     gold_fact_incidentes              gold_fact_resumen_diario
  (Severidad + Pérdida Económica)     (KPIs por Día y Dispositivo)
            │                               │
            └───────────────┬───────────────┘
                            ▼
              [ Dashboards & Analítica ]
               Looker Studio / BigQuery
```

---

## 📦 2. Estructuras de Datos y Modelado Dimensional

### Capa Bronze (Raw Ingestion)
- **`bronze_telemetria`**: Particionada por `DATE(timestamp)` y clusterizada por `device_id`. Recibe JSON continuo desde Pub/Sub.

### Capa Silver (Clean & Enriched)
- **`silver_telemetria_clean`**: 
  - Deduplicación por `(device_id, timestamp)`.
  - Filtro de anomalías físicas espurias (`temperature BETWEEN -50 AND 60`, `humidity BETWEEN 0 AND 100`).
  - Generación de Surrogate Key `telemetria_id` (`MD5`).

### Capa Gold (Esquema en Estrella / Star Schema para Analítica)
- **Tablas de Hechos (Fact Tables):**
  - **`gold_fact_incidentes`**: Contiene cada infracción de temperatura clasificada por severidad (`CRÍTICA`, `MODERADA`, `LEVE`) y su impacto financiero calculado en USD.
  - **`gold_fact_resumen_diario`**: Agregación diaria por sensor y producto con KPIs (temperatura promedio, mínima, máxima, total de alertas y tiempo acumulado en riesgo).
- **Tablas de Dimensiones (Dimension Tables):**
  - **`dim_productos`**: `product_id`, `nombre`, `categoria`, `temp_min`, `temp_max`, `costo_unitario`.
  - **`dim_asignacion_sensores`**: `device_id`, `product_id`, `camara_almacen`, `responsable`.

---

## 🚀 3. Instrucciones de Ejecución

### Activar Entorno Virtual
```bash
cd /home/gsoto1872/iot-coldchain
source .venv/bin/activate
```

### 1. Iniciar Simulación de Sensores IoT (Streaming)
```bash
python iot_simulator.py
```

### 2. Ejecutar Pipeline de Procesamiento Batch (ELT)
Ejecuta la limpieza, enriquecimiento y carga de las tablas Gold en BigQuery:
```bash
python pipelines/batch_pipeline.py
```
*(O ejecutar directamente el script SQL [`pipelines/batch_transformations.sql`](file:///home/gsoto1872/iot-coldchain/pipelines/batch_transformations.sql) en BigQuery Console)*.

### 3. Consultar la Capa Gold en BigQuery
```bash
# Ver incidentes detectados con impacto financiero:
bq query --use_legacy_sql=false 'SELECT * FROM `myfirstproject-508413.cold_chain_db.gold_fact_incidentes` LIMIT 10;'

# Ver resumen diario consolidado para dashboards:
bq query --use_legacy_sql=false 'SELECT * FROM `myfirstproject-508413.cold_chain_db.gold_fact_resumen_diario` LIMIT 10;'
```
