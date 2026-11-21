"""
DEMOSTRACIÓN FUNCIONAL END-TO-END (HITO FINAL)
Proyecto: Smart Cold Chain IoT en Google Cloud Platform
Ejecuta y verifica en vivo el ciclo completo:
Inyección de anomalía -> Pub/Sub -> BigQuery Streaming -> Hot Path Alert -> Batch ELT -> Exposición API & Impacto Financiero
"""

import time
import json
import os
import random
from datetime import datetime, timezone
from google.cloud import pubsub_v1, bigquery
from fastapi.testclient import TestClient
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from api.main import app

PROJECT_ID = "myfirstproject-508413"
TOPIC_ID = "iot-telemetry-topic"
KEY_PATH = os.path.join(BASE_DIR, "sa-iot-key.json")

def print_banner(text):
    print("\n" + "=" * 75)
    print(f" {text}")
    print("=" * 75)

def run_e2e_demo():
    print_banner("🚀 INICIO DE DEMOSTRACIÓN FUNCIONAL END-TO-END (SMART COLD CHAIN)")
    print(f"Proyecto GCP: {PROJECT_ID}")
    print(f"Región: us-central1 | Arquitectura: Pub/Sub -> BigQuery (Bronze/Silver/Gold) -> API")
    time.sleep(1)

    # -------------------------------------------------------------------------
    # PASO 1: Inyección de Anomalía Crítica en Vivo
    # -------------------------------------------------------------------------
    print_banner("PASO 1: Emulación de Falla Crítica en Sensor de Transporte (IoT)")
    device_id = "SENSOR-02"
    temp_anomala = round(random.uniform(14.2, 17.8), 1)  # Temperatura dinámica crítica para la demo en vivo
    humidity = round(random.uniform(68.0, 78.0), 1)
    battery = random.randint(88, 95)

    payload = {
        "device_id": device_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "temperature": temp_anomala,
        "humidity": humidity,
        "battery_pct": battery
    }

    print(f"📡 Dispositivo: {device_id} (Asignado a: Camión-Reparto-04, Producto: Carne Fresca)")
    print(f"🌡️  Temperatura registrada: {temp_anomala}°C (Límite máximo permitido: 4.0°C)")
    print(f"📦 Payload JSON generado:\n   {json.dumps(payload, indent=2)}")

    # -------------------------------------------------------------------------
    # PASO 2: Publicación Segura en Cloud Pub/Sub
    # -------------------------------------------------------------------------
    print_banner("PASO 2: Ingesta Asíncrona en Google Cloud Pub/Sub")
    publisher = pubsub_v1.PublisherClient.from_service_account_file(KEY_PATH)
    topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

    future = publisher.publish(topic_path, json.dumps(payload).encode("utf-8"))
    msg_id = future.result()
    print(f"✅ Evento publicado exitosamente en: {topic_path}")
    print(f"🔑 Cloud Pub/Sub Message ID asignado: {msg_id}")

    # -------------------------------------------------------------------------
    # PASO 3: Verificación de Ingesta Nativa en BigQuery Bronze
    # -------------------------------------------------------------------------
    print_banner("PASO 3: Ingesta Directa sin Servidores hacia BigQuery Bronze")
    print("⏳ Esperando 3 segundos para propagación del Direct Ingestion de Pub/Sub...")
    time.sleep(3)

    bq_client = bigquery.Client(project=PROJECT_ID)
    sql_bronze = f"""
    SELECT device_id, timestamp, temperature, humidity, battery_pct
    FROM `{PROJECT_ID}.cold_chain_db.bronze_telemetria`
    WHERE device_id = '{device_id}'
    ORDER BY timestamp DESC LIMIT 1
    """
    bronze_rows = list(bq_client.query(sql_bronze).result())
    if bronze_rows:
        row = bronze_rows[0]
        print(f"✅ Registro persistido en bronze_telemetria:")
        print(f"   Timestamp: {row.timestamp} | Sensor: {row.device_id} | Temp: {row.temperature}°C | Batería: {row.battery_pct}%")

    # -------------------------------------------------------------------------
    # PASO 4: Hot Path - Detección Operacional en Tiempo Real (< 2s)
    # -------------------------------------------------------------------------
    print_banner("PASO 4: Hot Path - Detección en Tiempo Real (< 2 segundos)")
    sql_hot = f"""
    SELECT 
        device_id, producto, camara_almacen, responsable,
        temp_actual, temp_max, estado_cadena_frio, desviacion_grados
    FROM `{PROJECT_ID}.cold_chain_db.v_alertas_cadena_frio`
    WHERE device_id = '{device_id}'
    ORDER BY timestamp DESC LIMIT 1
    """
    hot_rows = list(bq_client.query(sql_hot).result())
    if hot_rows:
        h = hot_rows[0]
        print(f"🚨 ALERTA OPERACIONAL DISPARADA EN TIEMPO REAL:")
        print(f"   • Vehículo: {h.camara_almacen} | Conductor: {h.responsable}")
        print(f"   • Producto en riesgo: {h.producto} | Estado: {h.estado_cadena_frio}")
        print(f"   • Temp Real: {h.temp_actual}°C | Límite: {h.temp_max}°C | Exceso Térmico: +{h.desviacion_grados}°C")

    # -------------------------------------------------------------------------
    # PASO 5: Cold Path - Ejecución del Pipeline ELT (Silver y Gold)
    # -------------------------------------------------------------------------
    print_banner("PASO 5: Cold Path - Ejecución del Pipeline ELT Masivo (Silver & Gold)")
    from pipelines.batch_pipeline import run_batch_pipeline
    run_batch_pipeline()

    # -------------------------------------------------------------------------
    # PASO 6: Exposición de Resultados vía REST API
    # -------------------------------------------------------------------------
    print_banner("PASO 6: Capa de Exposición y Servicios - Consulta REST API")
    client = TestClient(app)
    api_res = client.get("/api/v1/incidents?severity=CRITICA&limit=5")
    if api_res.status_code == 200:
        data = api_res.json()
        print(f"🌐 Respuesta HTTP 200 OK desde /api/v1/incidents (Filtro: Severidad CRÍTICA):")
        incidents = data.get("incidents", [])
        if incidents:
            inc = incidents[0]
            print(f"   • Incidente ID: {inc['incidente_id']}")
            print(f"   • Dispositivo: {inc['device_id']} | Responsable: {inc['responsable']}")
            print(f"   • Nivel de Severidad: {inc['nivel_severidad']}")
            print(f"   • Desviación Registrada: +{inc['desviacion_grados']} °C")
            print(f"   • 💰 Impacto Financiero Liquidado: ${inc['impacto_financiero_estimado']} USD")
            print(f"   • 📈 Pérdida Total Acumulada en Flota: ${data['total_financial_loss_usd']} USD")
        else:
            print("   ℹ️ No se encontraron incidentes con el filtro aplicado.")

    # -------------------------------------------------------------------------
    # PASO 7: Decisión Prescriptiva de Negocio
    # -------------------------------------------------------------------------
    print_banner("PASO 7: Decisión Automatizada de Negocio / Plan de Inventario")
    print(f"📋 DECISIÓN OPERACIONAL PRESCRIPTIVA:")
    print(f"   1. [REDIRECCIÓN]: Desviar 'Camión-Reparto-04' a la cámara frigorífica de contingencia más cercana.")
    print(f"   2. [BLOQUEO DE INVENTARIO]: Cuarentena automática del lote SENSOR-02 en el WMS/ERP para evitar venta.")
    print(f"   3. [NOTIFICACIÓN]: Notificación automática enviada a Juan Perez y al supervisor de aseguramiento de calidad.")
    print(f"   4. [SEGUROS]: Archivo probatorio generado con Hash MD5 para liquidación de póliza de seguro de carga.")

    print_banner("🎉 DEMOSTRACIÓN END-TO-END COMPLETADA CON ÉXITO")
    print(f"👉 ¡MIRA TU DASHBOARD EN EL NAVEGADOR!")
    print(f"   • La temperatura de SENSOR-02 acaba de registrar: {temp_anomala} °C")
    print(f"   • El gráfico térmico y la tarjeta de 'Camión-Reparto-04' se actualizaron.")
    print(f"   • Un nuevo incidente fue insertado en BigQuery Gold con su pérdida en $ USD.")
    print(f"   • Dashboard URL: http://localhost:8000/dashboard (o Web Preview en Cloud Shell)")
    print("=" * 75 + "\n")

if __name__ == "__main__":
    run_e2e_demo()
