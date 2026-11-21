"""
Smart Cold Chain IoT - Exposure Layer & REST API
Exposición de datos procesados (BigQuery Gold & Silver) y Gateway de Ingesta
usando FastAPI y Google Cloud Client Libraries.
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, timezone
import json
import os
from google.cloud import bigquery, pubsub_v1

# Inicialización de la aplicación FastAPI
app = FastAPI(
    title="Smart Cold Chain IoT API",
    description="API de exposición analítica y servicios en tiempo real para monitoreo de cadena de frío en Google Cloud Platform.",
    version="1.0.0",
    contact={
        "name": "Guillermo Soto - Data Architecture Team",
        "email": "gsoto1872@gmail.com"
    }
)

# Configuración de CORS para aplicaciones web consumidoras (React, Looker, Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "myfirstproject-508413")
DATASET_ID = "cold_chain_db"
TOPIC_ID = "iot-telemetry-topic"

# Clientes de GCP
bq_client = bigquery.Client(project=PROJECT_ID)
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)


# Modelos Pydantic para validación y contratos de datos
class TelemetryInput(BaseModel):
    device_id: str = Field(..., example="SENSOR-02", description="Identificador único del sensor")
    temperature: float = Field(..., example=10.5, description="Temperatura física registrada en °C")
    humidity: float = Field(..., example=65.2, description="Humedad relativa en %")
    battery_pct: int = Field(..., ge=0, le=100, example=95, description="Porcentaje de batería del dispositivo")
    timestamp: Optional[str] = Field(None, example="2026-11-21T04:30:00Z", description="Estampa temporal ISO 8601")


# -----------------------------------------------------------------------------
# 1. Health Check & Diagnóstico
# -----------------------------------------------------------------------------
@app.get("/health", tags=["Infraestructura"])
def health_check():
    """Verifica la operatividad de la API y la conectividad hacia Google Cloud BigQuery."""
    try:
        query_job = bq_client.query("SELECT 1 AS status")
        query_job.result()
        bq_status = "ONLINE"
    except Exception as e:
        bq_status = f"ERROR: {str(e)}"

    return {
        "service": "Smart Cold Chain Exposure API",
        "status": "UP",
        "cloud_provider": "Google Cloud Platform",
        "project_id": PROJECT_ID,
        "region": "us-central1",
        "bigquery_status": bq_status,
        "timestamp_utc": datetime.now(timezone.utc).isoformat()
    }


# -----------------------------------------------------------------------------
# 2. Hot Path: Telemetría Operacional en Vivo (< 2s)
# -----------------------------------------------------------------------------
@app.get("/api/v1/telemetry/live", tags=["Operaciones en Tiempo Real"])
def get_live_telemetry(
    status: Optional[str] = Query(None, description="Filtrar por estado: 'NORMAL' o 'ALERTA: Exceso de Calor'"),
    limit: int = Query(20, ge=1, le=100)
):
    """
    Retorna el estado más reciente de los sensores en tránsito mediante la vista Hot Path.
    Ideal para torres de control y dashboards operativos.
    """
    sql = f"""
    SELECT 
        FORMAT_TIMESTAMP('%Y-%m-%dT%H:%M:%SZ', timestamp) AS timestamp,
        device_id,
        camara_almacen,
        responsable,
        producto,
        categoria,
        temp_actual,
        temp_min,
        temp_max,
        costo_unitario,
        estado_cadena_frio,
        desviacion_grados
    FROM `{PROJECT_ID}.{DATASET_ID}.v_alertas_cadena_frio`
    """
    if status:
        sql += f" WHERE estado_cadena_frio = '{status}'"
    sql += f" ORDER BY timestamp DESC LIMIT {limit}"

    try:
        query_job = bq_client.query(sql)
        results = [dict(row) for row in query_job.result()]
        return {
            "total_records": len(results),
            "filter_status": status,
            "data": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error consultando BigQuery: {str(e)}")


# -----------------------------------------------------------------------------
# 3. Cold Path: Auditoría de Incidentes Térmicos y Pérdidas (Capa Gold)
# -----------------------------------------------------------------------------
@app.get("/api/v1/incidents", tags=["Analítica & Auditoría"])
def get_thermal_incidents(
    severity: Optional[str] = Query(None, description="Nivel de severidad: 'CRÍTICA', 'MODERADA', 'LEVE'"),
    limit: int = Query(50, ge=1, le=200)
):
    """
    Consulta las infracciones registradas en la tabla de hechos Gold con impacto financiero valorizado en USD.
    Alimenta sistemas de auditoría, reclamos de seguros y cumplimiento normativo.
    """
    sql = f"""
    SELECT 
        incidente_id,
        FORMAT_TIMESTAMP('%Y-%m-%dT%H:%M:%SZ', timestamp) AS timestamp,
        CAST(fecha AS STRING) AS fecha,
        device_id,
        product_id,
        camara_almacen,
        responsable,
        temp_registrada,
        temp_limite,
        desviacion_grados,
        nivel_severidad,
        impacto_financiero_estimado
    FROM `{PROJECT_ID}.{DATASET_ID}.gold_fact_incidentes`
    """
    if severity:
        sev = severity.strip().upper()
        if sev in ["CRITICA", "CRÍTICA"]:
            sql += " WHERE nivel_severidad IN ('CRITICA', 'CRÍTICA')"
        else:
            sql += f" WHERE nivel_severidad = '{sev}'"
    sql += f" ORDER BY fecha DESC, desviacion_grados DESC LIMIT {limit}"

    try:
        query_job = bq_client.query(sql)
        incidents = [dict(row) for row in query_job.result()]
        total_loss_usd = sum(row.get("impacto_financiero_estimado", 0.0) for row in incidents)

        return {
            "total_incidents": len(incidents),
            "severity_filter": severity,
            "total_financial_loss_usd": round(total_loss_usd, 2),
            "incidents": incidents
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error consultando incidentes Gold: {str(e)}")


# -----------------------------------------------------------------------------
# 4. Capa Gold: KPIs y Resumen Diario Agregado
# -----------------------------------------------------------------------------
@app.get("/api/v1/kpis/daily", tags=["Analítica & Auditoría"])
def get_daily_kpis(
    date: Optional[str] = Query(None, example="2026-11-19", description="Fecha en formato YYYY-MM-DD")
):
    """
    Retorna métricas consolidadas por día, dispositivo y producto para tableros ejecutivos.
    """
    sql = f"""
    SELECT 
        CAST(fecha AS STRING) AS fecha,
        device_id,
        product_id,
        camara_almacen,
        total_lecturas,
        temp_promedio,
        temp_minima,
        temp_maxima,
        total_alertas,
        bateria_promedio,
        tiempo_fuera_rango_minutos
    FROM `{PROJECT_ID}.{DATASET_ID}.gold_fact_resumen_diario`
    """
    if date:
        sql += f" WHERE fecha = '{date}'"
    sql += " ORDER BY fecha DESC, total_alertas DESC"

    try:
        query_job = bq_client.query(sql)
        records = [dict(row) for row in query_job.result()]
        return {
            "total_records": len(records),
            "kpis": records
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error consultando KPIs diarios: {str(e)}")


# -----------------------------------------------------------------------------
# 5. Catálogo Maestro de Productos (Batch ERP)
# -----------------------------------------------------------------------------
@app.get("/api/v1/products", tags=["Catálogos Maestros"])
def get_products():
    """Consulta el catálogo maestro de productos y tolerancias térmicas."""
    sql = f"SELECT * FROM `{PROJECT_ID}.{DATASET_ID}.dim_productos` ORDER BY product_id"
    try:
        query_job = bq_client.query(sql)
        products = [dict(row) for row in query_job.result()]
        return {"total_products": len(products), "products": products}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------------------------------------------------------
# 6. Ingesta REST / Gateway hacia Pub/Sub (Canal de Respaldo)
# -----------------------------------------------------------------------------
@app.post("/api/v1/telemetry/ingest", status_code=202, tags=["Ingesta Gateway"])
def ingest_telemetry_via_api(payload: TelemetryInput):
    """
    Gateway de Ingesta HTTP: Permite a dispositivos que no poseen el SDK de Pub/Sub
    enviar telemetría a través de una petición REST estandarizada.
    La API valida el contrato Pydantic y publica el mensaje en Cloud Pub/Sub.
    """
    ts = payload.timestamp or datetime.now(timezone.utc).isoformat()
    message_dict = {
        "device_id": payload.device_id,
        "timestamp": ts,
        "temperature": payload.temperature,
        "humidity": payload.humidity,
        "battery_pct": payload.battery_pct
    }
    try:
        data_str = json.dumps(message_dict)
        future = publisher.publish(topic_path, data_str.encode("utf-8"))
        msg_id = future.result()
        return {
            "status": "ACCEPTED",
            "message_id": msg_id,
            "topic": topic_path,
            "data": message_dict
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Fallo publicando en Pub/Sub: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)
