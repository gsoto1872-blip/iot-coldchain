"""
Stream Processor (Hot Path - Tiempo Real)
Consume eventos de baja latencia directo de Pub/Sub para detección inmediata
de anomalías críticas operacionales antes del procesamiento batch.
"""
import json
import os
from google.cloud import pubsub_v1

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY_PATH = os.path.join(BASE_DIR, "sa-iot-key.json")
PROJECT_ID = "myfirstproject-508413"
SUBSCRIPTION_ID = "iot-realtime-alerts-sub"
TOPIC_ID = "iot-telemetry-topic"

# Umbrales críticos en memoria para reacción sub-segundo
THRESHOLDS = {
    "SENSOR-01": {"min": 2.0, "max": 8.0, "producto": "Vacunas ARN"},
    "SENSOR-02": {"min": -1.0, "max": 4.0, "producto": "Carne Fresca"},
    "SENSOR-03": {"min": -22.0, "max": -18.0, "producto": "Helado Gourmet"}
}

def process_message(message):
    try:
        data = json.loads(message.data.decode("utf-8"))
        device_id = data.get("device_id")
        temp = data.get("temperature")
        timestamp = data.get("timestamp")

        rule = THRESHOLDS.get(device_id)
        if rule:
            if temp > rule["max"] or temp < rule["min"]:
                desvio = round(abs(temp - (rule["max"] if temp > rule["max"] else rule["min"])), 2)
                print(f"🚨 [STREAM ALERT < 1s] Dispositivo: {device_id} | Producto: {rule['producto']}")
                print(f"   Temperatura: {temp}°C (Rango: {rule['min']}°C a {rule['max']}°C) | Desvío: +{desvio}°C")
                print(f"   Timestamp: {timestamp} -> Disparando alerta inmediata a sala de control...")
            else:
                print(f"🟢 [STREAM OK] {device_id}: {temp}°C dentro de rango.")

        message.ack()
    except Exception as e:
        print(f"❌ Error procesando mensaje streaming: {e}")
        message.nack()

def start_stream_listener():
    print("=" * 60)
    print("⚡ [STREAM PROCESSING - HOT PATH]")
    print(f"Escuchando eventos en tiempo real con baja latencia...")
    print("=" * 60)

    subscriber = pubsub_v1.SubscriberClient()
    sub_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)

    streaming_pull_future = subscriber.subscribe(sub_path, callback=process_message)
    print(f"Suscrito a: {sub_path}")

    try:
        streaming_pull_future.result(timeout=10) # 10s para demo o timeout
    except Exception:
        streaming_pull_future.cancel()

if __name__ == "__main__":
    start_stream_listener()
