"""
Batch ELT Pipeline Execution Script
Ejecuta la limpieza, enriquecimiento y modelado dimensional (Bronze -> Silver -> Gold)
usando BigQuery client en Python.
"""
import os
import sys
from google.cloud import bigquery

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQL_FILE = os.path.join(BASE_DIR, "pipelines", "batch_transformations.sql")
PROJECT_ID = "myfirstproject-508413"

def run_batch_pipeline():
    print("=" * 60)
    print("🔄 [BATCH PIPELINE] Iniciando ciclo de transformación ELT...")
    print(f"Proyecto GCP: {PROJECT_ID}")
    print(f"Leyendo SQL: {SQL_FILE}")
    print("=" * 60)

    client = bigquery.Client(project=PROJECT_ID)

    with open(SQL_FILE, "r") as f:
        sql_content = f.read()

    # Dividir las sentencias por bloque de inserción
    statements = [stmt.strip() for stmt in sql_content.split(";") if stmt.strip()]

    labels = [
        "Capa Silver (Limpieza y Deduplicación)",
        "Capa Gold (Tabla de Hechos de Incidentes)",
        "Capa Gold (Resumen Analítico Diario)"
    ]

    for idx, stmt in enumerate(statements):
        label = labels[idx] if idx < len(labels) else f"Etapa #{idx+1}"
        print(f"\n▶️ Ejecutando: {label}...")
        
        job_config = bigquery.QueryJobConfig(
            labels={"pipeline": "batch-coldchain", "stage": f"step-{idx+1}"}
        )
        query_job = client.query(stmt, job_config=job_config)
        query_job.result()  # Esperar a que finalice

        print(f"   ✅ Finalizado con éxito (Job ID: {query_job.job_id})")
        if query_job.num_dml_affected_rows is not None:
            print(f"   📊 Filas afectadas: {query_job.num_dml_affected_rows}")

    print("\n" + "=" * 60)
    print("🎉 Pipeline Batch completado exitosamente.")
    print("=" * 60)

if __name__ == "__main__":
    run_batch_pipeline()
