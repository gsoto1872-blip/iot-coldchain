"""
Unit Tests for Smart Cold Chain Exposure API
Valida la conectividad de los endpoints REST hacia BigQuery y Pub/Sub.
"""
from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "UP"
    assert data["bigquery_status"] == "ONLINE"
    print("✅ /health pasó exitosamente:", data)

def test_live_telemetry():
    response = client.get("/api/v1/telemetry/live?limit=5")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    print(f"✅ /api/v1/telemetry/live pasó exitosamente: {data['total_records']} registros obtenidos.")

def test_incidents():
    response = client.get("/api/v1/incidents?limit=5")
    assert response.status_code == 200
    data = response.json()
    assert "incidents" in data
    print(f"✅ /api/v1/incidents pasó exitosamente: Pérdida total valorizada = ${data.get('total_financial_loss_usd')} USD.")

def test_products():
    response = client.get("/api/v1/products")
    assert response.status_code == 200
    data = response.json()
    assert data["total_products"] >= 3
    print(f"✅ /api/v1/products pasó exitosamente: {data['total_products']} productos en catálogo.")

if __name__ == "__main__":
    print("Iniciando pruebas de la Capa de Exposición API...")
    test_health()
    test_live_telemetry()
    test_incidents()
    test_products()
    print("🎉 Todas las pruebas de la API finalizaron con éxito.")
