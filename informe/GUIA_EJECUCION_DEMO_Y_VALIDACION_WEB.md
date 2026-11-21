# GUÍA OPERACIONAL: EJECUCIÓN DE LA DEMO END-TO-END Y VALIDACIÓN EN LA WEB
## Proyecto: Smart Cold Chain IoT en Google Cloud Platform (Lakehouse Medallion & REST Services)

---

### FICHA TÉCNICA Y METADATOS DEL PROYECTO

| Parámetro | Detalle de Operación |
| :--- | :--- |
| **Proyecto en GCP:** | `myfirstproject-508413` |
| **Región de Cómputo:** | `us-central1` (Iowa, Estados Unidos) |
| **Dataset Analítico:** | `cold_chain_db` (BigQuery) |
| **Tópico de Ingesta:** | `iot-telemetry-topic` (Cloud Pub/Sub) |
| **Suscripción Directa:** | `iot-telemetry-bq-sub` (BigQuery Direct Ingestion) |
| **Repositorio GitHub:** | [https://github.com/gsoto1872-blip/iot-coldchain](https://github.com/gsoto1872-blip/iot-coldchain) |
| **Autor:** | Guillermo Soto |
| **Fecha:** | Noviembre 2026 |

---

## ÍNDICE DE LA GUÍA

1. [Resumen del Flujo de la Demostración](#1-resumen-del-flujo-de-la-demostración)
2. [Fase 1: Preparación del Entorno en Cloud Shell](#2-fase-1-preparación-del-entorno-en-cloud-shell)
3. [Fase 2: Ejecución de la Demo Automatizada End-to-End](#3-fase-2-ejecución-de-la-demo-automatizada-end-to-end)
4. [Fase 3: Validación en la Web (Paso a Paso)](#4-fase-3-validación-en-la-web-paso-a-paso)
   - 4.1. Validación Web 1: Swagger UI de FastAPI (Web Preview Cloud Shell Puerto 8000)
   - 4.2. Validación Web 2: Consola de Google Cloud (BigQuery Studio & Pub/Sub)
   - 4.3. Validación Web 3: Pitch Deck Interactivo de Diapositivas (Puerto 8080)
   - 4.4. Validación Web 4: Repositorio Oficial y Código en GitHub
5. [Fase 4: Ejecución Manual Paso a Paso (Demostración en Pantalla Dividida)](#5-fase-4-ejecución-manual-paso-a-paso-demostración-en-pantalla-dividida)
6. [Fase 5: Matriz de Verificación Rápida y Troubleshooting](#6-fase-5-matriz-de-verificación-rápida-y-troubleshooting)

---

# 1. RESUMEN DEL FLUJO DE LA DEMOSTRACIÓN

La demostración funcional comprueba en vivo cómo un fallo mecánico real en carretera es capturado, procesado y resuelto en menos de 5 segundos a través de 7 hitos consecutivos:

```
+-------------------------------------------------------------------------------------------------------------------------+
|                                             FLUJO OPERACIONAL DE LA DEMOSTRACIÓN                                        |
+-------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                         |
|  [1. FALLO IoT]              [2. INGESTA PUB/SUB]            [3. INGESTA DIRECTA BQ]         [4. HOT PATH ALERT]        |
|  Sensor: SENSOR-02           Topic:                          Tabla:                          Vista:                     |
|  Temp sube a +13.5°C  ====>  `iot-telemetry-topic`   =====>  `bronze_telemetria`     =====>  `v_alertas_cadena_frio`    |
|  (Límite: +4.0°C)            (Message ID generado)           (Latencia < 2.5 seg)            (Alarma: +9.5°C exceso)    |
|                                                                                                         |               |
|                                                                                                         v               |
|  [7. DECISIÓN NEGOCIO]       [6. EXPOSICIÓN API]             [5. PIPELINE BATCH ELT]                 [DESVÍO RUTA]      |
|  - Desvío a cámara fría      Endpoint:                       Capa Silver (Deduplicación) <====       Orden en cabina    |
|  - Cuarentena WMS/ERP  <===  `GET /api/v1/incidents`  <====  Capa Gold (Star Schema)                 a Juan Perez       |
|  - Expediente seguro         (HTTP 200 / $1,187.50 USD)      (Cálculo financiero merma)                                 |
|                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------+
```

---

# 2. FASE 1: PREPARACIÓN DEL ENTORNO EN CLOUD SHELL

Abre tu terminal en Google Cloud Shell y ejecuta los siguientes comandos para posicionarte en el directorio y activar el entorno virtual con todas las dependencias necesarias:

```bash
# 1. Ir al directorio raíz del proyecto
cd /home/gsoto1872/iot-coldchain

# 2. Activar el entorno virtual de Python
source .venv/bin/activate

# 3. Configurar el proyecto activo de Google Cloud
gcloud config set project myfirstproject-508413

# 4. Asegurar las credenciales de ejecución
export GOOGLE_APPLICATION_CREDENTIALS="/home/gsoto1872/iot-coldchain/sa-iot-key.json"
export GOOGLE_CLOUD_PROJECT="myfirstproject-508413"
```

---

# 3. FASE 2: EJECUCIÓN DE LA DEMO AUTOMATIZADA END-TO-END

### Comando de Ejecución:
Con el entorno virtual activo, ejecuta el script maestro de demostración:

```bash
python demo/demo_e2e.py
```

### ¿Qué sucede durante la ejecución? (Explicación de los 7 Pasos):

1. **Paso 1: Emulación de Falla Crítica en Sensor de Transporte (IoT):**
   - El script genera un evento sintético para el dispositivo `SENSOR-02` (instalado en el camión `Camión-Reparto-04`, que transporta *Carne Fresca*).
   - Genera una lectura de temperatura anómala de **+13.5°C** (cuando el rango permitido es de 0.0°C a 4.0°C).
2. **Paso 2: Ingesta Asíncrona en Cloud Pub/Sub:**
   - Publica el payload JSON al tópico `iot-telemetry-topic`.
   - Google Cloud responde de inmediato devolviendo un identificador unívoco de mensaje de Pub/Sub (`Message ID`).
3. **Paso 3: Ingesta Directa sin Servidores hacia BigQuery Bronze:**
   - La suscripción nativa `iot-telemetry-bq-sub` (*BigQuery Direct Ingestion*) escribe el mensaje directamente en la tabla `bronze_telemetria`.
   - El script consulta BigQuery tras 3 segundos y confirma la persistencia física de la fila.
4. **Paso 4: Hot Path - Detección en Tiempo Real (< 2 segundos):**
   - Se ejecuta una consulta sobre la vista SQL `v_alertas_cadena_frio`.
   - La vista evalúa el exceso térmico (+9.5°C) y clasifica el estado como `ALERTA: Exceso de Calor`.
5. **Paso 5: Cold Path - Ejecución del Pipeline ELT Masivo (Silver & Gold):**
   - Ejecuta secuencialmente las transformaciones de `pipelines/batch_transformations.sql`:
     - **Capa Silver (`silver_telemetria_clean`):** Deduplica por `(device_id, timestamp)` con `ROW_NUMBER()` y valida rangos físicos.
     - **Capa Gold Incidentes (`gold_fact_incidentes`):** Cruza con el catálogo maestro y cuantifica el daño financiero en dólares.
     - **Capa Gold Resumen (`gold_fact_resumen_diario`):** Agrega totales diarios, temperaturas promedio y minutos fuera de rango.
6. **Paso 6: Capa de Exposición y Servicios - Consulta REST API:**
   - Realiza una petición interna a la API FastAPI en el endpoint `GET /api/v1/incidents?severity=CRITICA`.
   - La API responde con **HTTP 200 OK**, mostrando la liquidación financiera de **$1,187.50 USD** para el incidente.
7. **Paso 7: Decisión Automatizada de Negocio:**
   - El sistema emite la recomendación prescriptiva: redirección del camión a cámara de contingencia, cuarentena del lote en WMS/ERP y notificación al asegurador de carga.

---

# 4. FASE 3: VALIDACIÓN EN LA WEB (PASO A PASO)

Existen cuatro formas complementarias de validar y auditar el proyecto a través de interfaces web interactivas:

---

### 4.1. Validación Web 1: Swagger UI de FastAPI (Web Preview de Cloud Shell)

Esta es la forma más impresionante para que el jurado o los evaluadores interactúen directamente con la API en vivo.

#### Paso A: Iniciar el servidor web de la API
En una terminal de Cloud Shell, ejecuta:
```bash
cd /home/gsoto1872/iot-coldchain
source .venv/bin/activate
uvicorn api.main:app --host 0.0.0.0 --port 8000
```
Verás un mensaje indicando: `Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)`.

#### Paso B: Abrir la Vista Previa en la Web (Web Preview)
1. En la barra superior derecha de tu ventana de Google Cloud Shell, localiza el ícono de **Vista previa en la Web** (se asemeja a una pantalla con un ojo o un recuadro de monitor).
2. Haz clic en él y selecciona **"Vista previa en el puerto 8000"** *(si no aparece el puerto 8000, haz clic en "Cambiar puerto", escribe `8000` y haz clic en "Cambiar y obtener vista previa")*.
3. Se abrirá una nueva pestaña en tu navegador con una URL segura de Google:
   `https://8000-cs-XXXXXXXX.cloudshell.dev/`

#### Paso C: Acceder a la documentación interactiva Swagger
En la barra de direcciones de esa nueva pestaña, agrega `/docs` al final de la URL:
👉 **`https://8000-cs-XXXXXXXX.cloudshell.dev/docs`**

#### Paso D: Probar los Endpoints en Vivo desde el Navegador:
* **Prueba 1: Salud del Sistema (`GET /health`):**
  - Haz clic en `GET /health` ➔ Clic en **"Try it out"** ➔ Clic en **"Execute"**.
  - Verás la respuesta con código `200`:
    ```json
    {
      "status": "healthy",
      "project_id": "myfirstproject-508413",
      "region": "us-central1",
      "version": "1.0.0"
    }
    ```
* **Prueba 2: Telemetría en Tiempo Real Hot Path (`GET /api/v1/telemetry/live`):**
  - Haz clic en `GET /api/v1/telemetry/live` ➔ **"Try it out"** ➔ **"Execute"**.
  - Muestra las últimas lecturas térmicas registradas en vuelo de toda la flota.
* **Prueba 3: Incidentes Críticos y Mermas en Dólares (`GET /api/v1/incidents`):**
  - Haz clic en `GET /api/v1/incidents` ➔ **"Try it out"**.
  - En el campo `severity` escribe: `CRITICA`.
  - Haz clic en **"Execute"**.
  - Verás el listado de incidentes valorizados con el cálculo exacto de pérdida financiera en dólares ($ USD).
* **Prueba 4: Resumen de KPIs Diarios (`GET /api/v1/kpis/daily`):**
  - Haz clic en `GET /api/v1/kpis/daily` ➔ **"Try it out"** ➔ **"Execute"**.
  - Muestra la consolidación de lecturas, temperatura promedio, máxima, mínima y minutos acumulados fuera de rango.
* **Prueba 5: Inyectar Nueva Lectura Vía Web Gateway (`POST /api/v1/telemetry/ingest`):**
  - Haz clic en `POST /api/v1/telemetry/ingest` ➔ **"Try it out"**.
  - Pega este payload en el cuerpo de la petición:
    ```json
    {
      "device_id": "SENSOR-03",
      "temperature": 18.5,
      "humidity": 65.0,
      "battery_pct": 88
    }
    ```
  - Haz clic en **"Execute"**.
  - Recibirás `200 OK` con el `message_id` generado por Cloud Pub/Sub, demostrando que la API también actúa como Gateway de Ingesta web.

---

### 4.2. Validación Web 2: Consola de Google Cloud (BigQuery Studio & Pub/Sub)

Para verificar que los datos están físicamente persistidos en los servicios de Google Cloud:

#### A) BigQuery Studio (Inspección de las Capas Medallion):
1. Abre tu navegador e ingresa a:  
   👉 **[https://console.cloud.google.com/bigquery?project=myfirstproject-508413](https://console.cloud.google.com/bigquery?project=myfirstproject-508413)**
2. En el panel lateral izquierdo "Explorador", despliega:  
   `myfirstproject-508413` ➔ `cold_chain_db`.
3. Haz clic en las tablas para ver su esquema y vista previa:
   - **`bronze_telemetria`:** Haz clic en la pestaña **"Vista previa"** para ver las lecturas crudas recién llegadas de Pub/Sub.
   - **`silver_telemetria_clean`:** Observa los registros sin duplicados y con las columnas booleanas de control de calidad (`temp_valida`, `bateria_baja`).
   - **`gold_fact_incidentes`:** Observa la columna `impacto_financiero_estimado` donde se cuantifica la pérdida en dólares.
   - **`v_alertas_cadena_frio`:** Abre una pestaña de consulta SQL en BigQuery Studio y ejecuta:
     ```sql
     SELECT * 
     FROM `myfirstproject-508413.cold_chain_db.v_alertas_cadena_frio`
     ORDER BY timestamp DESC
     LIMIT 5;
     ```

#### B) Google Cloud Pub/Sub Console:
1. Ingresa a la consola de Pub/Sub:  
   👉 **[https://console.cloud.google.com/cloudpubsub/topic/detail/iot-telemetry-topic?project=myfirstproject-508413](https://console.cloud.google.com/cloudpubsub/topic/detail/iot-telemetry-topic?project=myfirstproject-508413)**
2. Verás los gráficos de tráfico de mensajes publicados en tiempo real.
3. Haz clic en la pestaña **"Suscripciones"** y selecciona **`iot-telemetry-bq-sub`**.
4. Podrás confirmar que el tipo de entrega es **"Escribir en BigQuery" (Direct Ingestion)** con estado **En buen estado (Healthy)**.

---

### 4.3. Validación Web 3: Pitch Deck Interactivo de Diapositivas (Puerto 8080)

Para presentar las diapositivas interactivas en tu navegador durante la sustentación:

#### Paso A: Iniciar el servidor web estático en Cloud Shell
Abre una terminal y ejecuta:
```bash
cd /home/gsoto1872/iot-coldchain
python3 -m http.server 8080
```

#### Paso B: Abrir en Vista Previa Web
1. En la esquina superior derecha de Cloud Shell, haz clic en **"Vista previa en la Web"**.
2. Selecciona **"Cambiar puerto"**, escribe `8080` y haz clic en **"Cambiar y obtener vista previa"**.
3. En la lista de archivos que aparece en el navegador, haz clic en la carpeta `informe/` y luego en:  
   👉 **`SLIDES_SUSTENTACION.html`**

#### Atajos de Teclado del Presentador:
* Presiona **`F`** para entrar o salir del modo pantalla completa (*Full Screen*).
* Presiona **`Flecha Derecha`** o **`N`** para avanzar a la siguiente diapositiva.
* Presiona **`Flecha Izquierda`** o **`P`** para retroceder.
* Presiona **`T`** para abrir o cerrar el cajón inferior con las **Notas del Orador y Guión de Defensa**.

*(Alternativa: También puedes descargar el archivo directamente a tu computadora con `cloudshell download /home/gsoto1872/iot-coldchain/informe/SLIDES_SUSTENTACION.html` y abrirlo haciendo doble clic en Chrome).*

---

### 4.4. Validación Web 4: Repositorio Oficial y Código en GitHub

El jurado y los evaluadores pueden revisar el repositorio público y su historial de commits en:  
👉 **[https://github.com/gsoto1872-blip/iot-coldchain](https://github.com/gsoto1872-blip/iot-coldchain)**

Archivos clave para mostrar en la sustentación:
* [README.md](https://github.com/gsoto1872-blip/iot-coldchain/blob/main/README.md): Portada ejecutiva, diagrama de arquitectura e instrucciones de despliegue.
* [api/main.py](https://github.com/gsoto1872-blip/iot-coldchain/blob/main/api/main.py): Código limpio y asíncrono de la API REST con FastAPI.
* [pipelines/batch_transformations.sql](https://github.com/gsoto1872-blip/iot-coldchain/blob/main/pipelines/batch_transformations.sql): Lógica declarativa ELT de deduplicación analítica y modelo dimensional en estrella.
* [demo/demo_e2e.py](https://github.com/gsoto1872-blip/iot-coldchain/blob/main/demo/demo_e2e.py): Script de la demostración end-to-end.
* [informe/ARQUITECTURA_DETALLADA_Y_FAQ.md](https://github.com/gsoto1872-blip/iot-coldchain/blob/main/informe/ARQUITECTURA_DETALLADA_Y_FAQ.md): Dossier completo de arquitectura, objetivos, solución de negocio y preguntas de defensa.

---

# 5. FASE 4: EJECUCIÓN MANUAL PASO A PASO (DEMOSTRACIÓN EN PANTALLA DIVIDIDA)

Si el jurado evaluador solicita ver la ejecución desacoplada en tiempo real (por ejemplo, mostrando la terminal a la izquierda y el navegador web a la derecha):

```
+------------------------------------------+------------------------------------------+
|      TERMINAL (Cloud Shell)              |       NAVEGADOR WEB (Swagger / BQ)       |
|                                          |                                          |
|  1. Ejecutar uvicorn api.main:app        |  1. Refrescar /docs                      |
|  2. Inyectar anomalía vía python o curl  |  2. Consultar GET /api/v1/telemetry/live |
|  3. Ejecutar batch_pipeline.py           |  3. Consultar GET /api/v1/incidents      |
+------------------------------------------+------------------------------------------+
```

### Paso 1: Levantar la API REST (Terminal 1)
```bash
cd /home/gsoto1872/iot-coldchain && source .venv/bin/activate
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

### Paso 2: Inyectar Anomalía Térmica Manualmente (Terminal 2)
Puedes enviar un payload con una temperatura de **+16.0°C** para una vacuna biológica mediante cURL:
```bash
curl -X POST "http://localhost:8000/api/v1/telemetry/ingest" \
     -H "Content-Type: application/json" \
     -d '{
       "device_id": "SENSOR-03",
       "temperature": 16.0,
       "humidity": 60.0,
       "battery_pct": 85
     }'
```
*Respuesta:* `{"status": "published", "message_id": "...", "timestamp": "..."}`.

### Paso 3: Verificar la Detección Inmediata Hot Path
En el navegador (o mediante cURL en Terminal 2), consulta la vista en vivo:
```bash
curl -s "http://localhost:8000/api/v1/telemetry/live?limit=1" | jq .
```
Comprobarás que la anomalía aparece en menos de 2 segundos.

### Paso 4: Ejecutar el Pipeline Batch ELT
Ejecuta la consolidación analítica en BigQuery:
```bash
python pipelines/batch_pipeline.py
```

### Paso 5: Consultar la Liquidación Financiera en Swagger
En la interfaz web de Swagger UI (`/docs`), ejecuta `GET /api/v1/incidents?severity=CRITICA` y observa cómo el nuevo incidente aparece liquidado con su impacto financiero calculado en dólares.

---

# 6. FASE 5: MATRIZ DE VERIFICACIÓN RÁPIDA Y TROUBLESHOOTING

| Síntoma / Situación | Causa Probable | Solución Inmediata |
| :--- | :--- | :--- |
| **Error `Address already in use` al iniciar uvicorn** | Había otra instancia previa de uvicorn en el puerto 8000 | Ejecuta: `fuser -k 8000/tcp` y vuelve a iniciar uvicorn. |
| **Error `403 Forbidden` o `Permission Denied`** | Falta autenticación de Application Default Credentials | Ejecuta: `export GOOGLE_APPLICATION_CREDENTIALS="/home/gsoto1872/iot-coldchain/sa-iot-key.json"` |
| **Web Preview muestra pantalla en blanco** | El puerto del Web Preview no coincide con el del comando | Verifica que en Web Preview esté seleccionado el puerto `8000` (para API) o `8080` (para slides). |
| **Poco espacio o desconexión en Cloud Shell** | Sesión inactiva de Google Cloud Shell | Presiona `Enter`, reactiva el entorno virtual con `source .venv/bin/activate` y continúa. |

---

### COMANDO PARA DESCARGAR ESTA GUÍA EN TU COMPUTADORA:
```bash
cloudshell download /home/gsoto1872/iot-coldchain/informe/GUIA_EJECUCION_DEMO_Y_VALIDACION_WEB.md
```
O consúltala directamente en el repositorio:  
👉 **[https://github.com/gsoto1872-blip/iot-coldchain/blob/main/informe/GUIA_EJECUCION_DEMO_Y_VALIDACION_WEB.md](https://github.com/gsoto1872-blip/iot-coldchain/blob/main/informe/GUIA_EJECUCION_DEMO_Y_VALIDACION_WEB.md)**
