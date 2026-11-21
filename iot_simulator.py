import json
import random
import time
from datetime import datetime, timezone
import os
from google.cloud import pubsub_v1

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_PATH = os.path.join(BASE_DIR, "sa-iot-key.json")
PROJECT_ID = "myfirstproject-508413"
TOPIC_ID = "iot-telemetry-topic"

# Autenticación con la Service Account creada
publisher = pubsub_v1.PublisherClient.from_service_account_file(KEY_PATH)
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

print(f"==================================================")
print(f"🚀 [SMART COLD CHAIN - IoT SIMULATOR]")
print(f"Proyecto GCP: {PROJECT_ID}")
print(f"Tópico Pub/Sub: {topic_path}")
print(f"Credenciales: {KEY_PATH}")
print(f"==================================================\n")

# Sensores y perfiles térmicos
DEVICES = {
    "SENSOR-01": {"base_temp": 4.5, "range": 0.5},   # Vacunas (2°C a 8°C)
    "SENSOR-02": {"base_temp": 2.0, "range": 0.8},   # Carnes (-1°C a 4°C)
    "SENSOR-03": {"base_temp": -20.0, "range": 0.5}  # Congelados (-22°C a -18°C)
}

try:
    cycle = 1
    while True:
        print(f"--- Ciclo de Telemetría #{cycle} ---")
        for device_id, profile in DEVICES.items():
            noise = random.uniform(-profile["range"], profile["range"])
            temp = round(profile["base_temp"] + noise, 2)
            
            # Inyección de anomalía intencional (15% de probabilidad)
            is_anomaly = False
            if random.random() < 0.15:
                is_anomaly = True
                temp = round(temp + random.uniform(6.0, 9.5), 2)

            payload = {
                "device_id": device_id,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "temperature": temp,
                "humidity": round(random.uniform(55.0, 75.0), 1),
                "battery_pct": random.randint(85, 100)
            }

            data_bytes = json.dumps(payload).encode("utf-8")
            future = publisher.publish(topic_path, data_bytes)
            message_id = future.result()

            if is_anomaly:
                print(f"  ⚠️  [ALERTA TÉRMICA] {device_id} -> {temp}°C (ID: {message_id})")
            else:
                print(f"  ✅  [NORMAL] {device_id} -> {temp}°C (ID: {message_id})")

        cycle += 1
        time.sleep(3)

except KeyboardInterrupt:
    print("\n🛑 Simulación finalizada por el usuario.")
