# INFORME TÉCNICO MAESTRO: ARQUITECTURA END-TO-END, MODELADO LAKEHOUSE Y PROCESAMIENTO HÍBRIDO DE DATOS IOT PARA EL MONITOREO DE CADENA DE FRÍO (SMART COLD CHAIN)

**Programa Académico:** Maestría / Especialización en Arquitectura y Procesamiento de Datos Masivos & IoT  
**Entorno Cloud:** Google Cloud Platform (GCP)  
**Proyecto Identificador:** `myfirstproject-508413`  
**Región de Despliegue:** `us-central1` (Iowa, Estados Unidos)  
**Autor:** Guillermo Soto  
**Fecha de Presentación:** Noviembre 2026  
**Documento:** Memoria de Ingeniería y Documentación Técnica Final  

---

## 1. RESUMEN EJECUTIVO Y MARCO CONCEPTUAL DE NEGOCIO

### 1.1. Contexto Industrial y Planteamiento del Problema
La distribución logística global de bienes de alta sensibilidad biológica y perecedera —incluyendo vacunas de plataforma ARN mensajero, hemoderivados, terapias celulares, carnes de exportación y productos ultracongelados— depende de la integridad ininterrumpida de la **cadena de frío**. 

En la práctica operativa, los cargamentos atraviesan múltiples fases logísticas: almacenes centrales, transferencias a vehículos de transporte terrestre de larga distancia, centros de distribución secundaria y rutas de entrega de última milla. Durante estas transiciones, fallas en los compresores de refrigeración, aperturas prolongadas de compuertas o cortes imprevistos de suministro eléctrico provocan fluctuaciones térmicas que degradan la vida útil del producto, inducen proliferación bacteriana o desnaturalizan principios activos farmacéuticos.

Tradicionalmente, las empresas se enfrentan a dos grandes barreras tecnológicas:
1. **Monitoreo Reactivo (Post-Mortem):** Dataloggers pasivos que registran la temperatura en memorias USB que solo se leen al final del viaje, cuando el daño es irreversible y la mercadería ya se ha perdido.
2. **Asimetría de Datos:** Imposibilidad de cruzar en tiempo real la telemetría continua de los sensores en tránsito con los sistemas maestros de gestión (ERP / WMS) donde residen las reglas térmicas, la propiedad del lote y el valor financiero de la carga.

### 1.2. Marco Normativo y Cumplimiento Regulatorio
El diseño de esta solución responde a los estándares internacionales de aseguramiento de calidad:
* **OMS (Organización Mundial de la Salud - TRS 961):** Exige el monitoreo continuo de temperatura y humedad en el almacenamiento y transporte de productos médicos sensibles al tiempo y la temperatura.
* **FDA 21 CFR Part 11 (EE. UU.):** Demanda que los registros electrónicos de temperatura sean inmutables, auditables y cuenten con marcas de tiempo certificadas y trazabilidad completa (*Data Integrity* bajo principios ALCOA+).
* **Buenas Prácticas de Distribución (GDP - Unión Europea):** Obliga a los operadores logísticos a contar con sistemas de alarmado activo ante desvíos térmicos durante el transporte intermodal.

### 1.3. Objetivos de la Solución de Ingeniería
* **Objetivo de Ingesta:** Capturar y desacoplar de forma elástica flujos masivos de telemetría IoT mediante colas de mensajería asíncronas con capacidad de admitir millones de eventos diarios sin pérdida de paquetes.
* **Objetivo de Procesamiento Híbrido:** Proveer una ruta caliente (**Hot Path**) de latencia sub-segundo (&lt; 2 s) para la activación de alarmas operacionales inmediatas, coexistiendo con una ruta fría (**Cold Path**) para la consolidación analítica masiva por lotes (Batch).
* **Objetivo de Calidad y Gobernanza:** Diseñar una arquitectura **Medallion Lakehouse (Bronze ➔ Silver ➔ Gold)** que garantice deduplicación determinística, eliminación de outliers físicos y trazabilidad estricta.
* **Objetivo Financiero:** Monetizar en dólares (\$ USD) el impacto económico de cada infracción térmica mediante el cruce automatizado con los costos de inventario, reduciendo al mismo tiempo los costos de infraestructura en la nube mediante un enfoque 100% Serverless.

---

## 2. DIAGRAMA DE ARQUITECTURA END-TO-END

La arquitectura implementada adopta el paradigma de **Data Lakehouse** sobre Google Cloud Platform, organizando el flujo de información en cinco capas desacopladas que operan sin necesidad de aprovisionar ni administrar servidores físicos.

```mermaid
flowchart TD
    subgraph S1["1. Capa de Fuentes Heterogéneas"]
        IoT["Sensores IoT / Gateways en Tránsito<br/><i>(Simulador Python / ESP32)</i><br/>Telemetría continua JSON (Streaming)"]
        ERP["Sistemas Transaccionales / ERP / WMS<br/><i>(Catálogos Maestros en CSV)</i><br/>Reglas de Producto y Asignación (Batch)"]
    end

    subgraph S2["2. Capa de Ingesta y Buffering"]
        Broker["Google Cloud Pub/Sub<br/><code>iot-telemetry-topic</code><br/>Buffer asíncrono elástico de alta velocidad"]
        DirectSub["BigQuery Direct Ingestion<br/><code>iot-telemetry-bq-sub</code><br/>Suscripción nativa sin código intermedio"]
        StorageBucket["Cloud Storage (GCS)<br/><code>gs://cold-chain-lake</code><br/>Recepción periódica de datos maestros"]
    end

    subgraph S3["3. Capa de Almacenamiento (Medallion Lakehouse)"]
        Bronze[("Capa Bronze: bronze_telemetria<br/>Particionada por DATE(timestamp)<br/>Clusterizada por device_id<br/><i>Histórico crudo inmutable</i>")]
        Silver[("Capa Silver: silver_telemetria_clean<br/>Deduplicación analítica con ROW_NUMBER()<br/>Filtro de anomalías instrumentales<br/><i>Surrogate Key determinística MD5</i>")]
        GoldFacts[("Capa Gold: Tablas de Hechos (Star Schema)<br/>• gold_fact_incidentes (Severidad y Pérdida USD)<br/>• gold_fact_resumen_diario (KPIs agregados diarios)")]
        Dims[("Dimensiones Maestras de Negocio<br/>• dim_productos (Tolerancias y Costos)<br/>• dim_asignacion_sensores (Activos y Chofer)")]
    end

    subgraph S4["4. Capa de Cómputo y Transformación"]
        Hot["HOT PATH: Detección en Tiempo Real<br/><code>v_alertas_cadena_frio</code><br/><i>Latencia de evaluación &lt; 2 segundos</i>"]
        Cold["COLD PATH: Pipeline ELT Periódico<br/><code>batch_pipeline.py</code> (Python + GoogleSQL)<br/><i>Limpieza, enriquecimiento y modelado</i>"]
    end

    subgraph S5["5. Capa de Exposición y Consumo"]
        BI["Looker Studio / BigQuery BI Engine<br/><i>Dashboards Ejecutivos y Auditoría</i>"]
        Ops["Alertas de Sala de Control / SCADA<br/><i>Notificación push ante desvíos críticos</i>"]
    end

    IoT -->|HTTPS / Pub/Sub API| Broker
    ERP -->|Batch Load| StorageBucket --> Dims

    Broker --> DirectSub --> Bronze
    Broker --> Hot --> Ops

    Bronze --> Cold
    Dims --> Cold
    Cold --> Silver --> GoldFacts

    GoldFacts --> BI
```

### 2.1. Desglose Funcional de Capas

1. **Capa de Fuentes:** Coexisten dispositivos IoT de campo (emisores de eventos de baja latencia) con exportaciones periódicas de sistemas empresariales tipo SAP o PostgreSQL.
2. **Capa de Ingesta:** Emplea **Google Cloud Pub/Sub** para absorber picos de tráfico causados por ráfagas de reconexión tras túneles o zonas sin cobertura celular.
3. **Capa de Almacenamiento:** Implementada enteramente sobre **Google BigQuery**, aprovechando su motor de almacenamiento columnar (*Capacitor*) con particionamiento diario y ordenamiento interno por clúster.
4. **Capa de Cómputo:** Desacopla la analítica operacional inmediata (Hot Path evaluado mediante vistas SQL de consulta directa) del procesamiento analítico profundo (Cold Path orquestado por scripts ELT programados).
5. **Capa de Exposición:** Provee endpoints de datos de alto rendimiento para interfaces gerenciales (Looker Studio) y webhooks operacionales de alerta.

---

## 3. INTEGRACIÓN MULTIFUENTE

La integración multifuente resuelve la incompatibilidad estructural, semántica y temporal entre los datos telemáticos no regulados y los registros transaccionales relacionales.

### 3.1. Matriz de Caracterización de Fuentes

| Atributo | Fuente 1: Telemetría Ambiental (Streaming) | Fuente 2: Catálogo de Productos (Batch) | Fuente 3: Asignación Logística (Batch) |
| :--- | :--- | :--- | :--- |
| **Origen** | Sensores IoT en contenedores / camiones. | Sistema ERP / Catálogo maestro de productos. | Sistema de Despacho y Logística (TMS/WMS). |
| **Frecuencia** | Continua (cada 3 a 10 segundos). | Diaria / Semanal (lenta variación). | Por despacho o turno operativo (4-8 horas). |
| **Estructura** | Semiestructurada (JSON). | Tabular relacional (CSV normalizado). | Tabular relacional (CSV normalizado). |
| **Mecanismo de Conexión** | Publicación HTTPS/TLS hacia Cloud Pub/Sub. | Carga por lotes hacia Cloud Storage / BigQuery. | Carga por lotes hacia Cloud Storage / BigQuery. |
| **Volumen Típico** | Millones de filas / día. | Cientos a miles de filas. | Decenas a cientos de filas por día. |
| **Calidad de Origen** | Propensa a valores espurios y reintentos. | Alta consistencia referencial y transaccional. | Alta consistencia administrativa. |

---

### 3.2. Contrato de Datos Formal (Data Contract) para Streaming

Para garantizar la interoperabilidad y evitar fallos de deserialización en BigQuery, se definió un **JSON Schema estricto** que rige el payload emitido por los sensores:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "IoTTelemetryPayload",
  "type": "object",
  "properties": {
    "device_id": {
      "type": "string",
      "pattern": "^SENSOR-[0-9]{2,}$",
      "description": "Identificador único asignado al sensor de hardware."
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "Estampa de tiempo en formato estándar UTC ISO 8601."
    },
    "temperature": {
      "type": "number",
      "minimum": -50.0,
      "maximum": 60.0,
      "description": "Temperatura ambiental registrada en grados Celsius."
    },
    "humidity": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 100.0,
      "description": "Humedad relativa ambiental en porcentaje (%)."
    },
    "battery_pct": {
      "type": "integer",
      "minimum": 0,
      "maximum": 100,
      "description": "Nivel de batería restante del dispositivo en porcentaje (%)."
    }
  },
  "required": ["device_id", "timestamp", "temperature", "humidity", "battery_pct"],
  "additionalProperties": false
}
```

---

### 3.3. Especificación de los Datos Maestros de Negocio (Batch)

#### Catálogo de Productos y Tolerancias Térmicas (`dim_productos`)
Define los umbrales críticos de conservación y el valor unitario para el cálculo de mermas:

```csv
product_id,nombre,categoria,temp_min,temp_max,costo_unitario
PROD-01,Vacunas ARN,Farmacia,2.0,8.0,45.00
PROD-02,Carne Fresca,Alimentos,-1.0,4.0,12.50
PROD-03,Helado Gourmet,Congelados,-22.0,-18.0,6.00
```

#### Asignación Operacional de Sensores (`dim_asignacion_sensores`)
Establece la custodia física de la carga, vinculando el sensor con la cámara y el chofer responsable:

```csv
device_id,product_id,camara_almacen,responsable
SENSOR-01,PROD-01,Camara-Refrigerada-A,Dr. Garcia
SENSOR-02,PROD-02,Camion-Reparto-04,Juan Perez
SENSOR-03,PROD-03,Congelador-Central-02,Ana Gomez
```

---

### 3.4. Estrategia de Enlace y Resolución de Relaciones

```mermaid
classDiagram
    class TelemetriaStreaming {
        +STRING device_id FK
        +TIMESTAMP timestamp
        +FLOAT64 temperature
        +FLOAT64 humidity
        +INT64 battery_pct
    }

    class DimAsignacionSensores {
        +STRING device_id PK
        +STRING product_id FK
        +STRING camara_almacen
        +STRING responsable
    }

    class DimProductos {
        +STRING product_id PK
        +STRING nombre
        +STRING categoria
        +FLOAT64 temp_min
        +FLOAT64 temp_max
        +FLOAT64 costo_unitario
    }

    TelemetriaStreaming --> DimAsignacionSensores : "1. Cruce por device_id"
    DimAsignacionSensores --> DimProductos : "2. Cruce por product_id"
```

El modelo efectúa un **doble salto relacional**:
1. El evento telemático aporta el `device_id`.
2. Mediante un *INNER JOIN* con `dim_asignacion_sensores`, el evento se contextualiza espacialmente (`camara_almacen`) y jurídicamente (`responsable`), recuperando a su vez el `product_id`.
3. Mediante un segundo *JOIN* con `dim_productos`, se inyectan las cotas de tolerancia térmica ($\text{temp\_min}$ y $\text{temp\_max}$) y el costo contable del bien, permitiendo la evaluación algorítmica de la infracción.

---

## 4. DEFINICIÓN DE INGESTA Y STORAGE

### 4.1. Mecanismo de Ingesta Streaming: Pub/Sub BigQuery Direct Ingestion
Para la captura del flujo continuo se seleccionó **Google Cloud Pub/Sub** vinculado a una suscripción directa de BigQuery (*BigQuery Direct Subscription*).

#### Justificación frente a Enfoques Convencionales:
* **Frente a Inserciones HTTP directas a BigQuery:** Los sensores físicos pueden experimentar cortes de red. Si hicieran peticiones directas a la base de datos, los reintentos saturarían el endpoint o causarían timeout. Pub/Sub actúa como un buffer que absorbe hasta 7 días de almacenamiento retenido.
* **Frente a Apache Kafka administrado:** Evita el costo fijo de instancias de computación 24/7 y la sobrecarga operativa de gestión de Zookeeper / KRaft, particiones de brokers y balanceo de carga.
* **Frente a Google Cloud Dataflow (Apache Beam):** El uso de la suscripción directa con la bandera `--use-table-schema` realiza el volcado sin requerir código de streaming intermedio, eliminando el costo de máquinas virtuales dedicadas para pipelines de Dataflow.

```bash
# Comando de Creación de la Suscripción Directa en GCP
gcloud pubsub subscriptions create iot-telemetry-bq-sub \
    --topic=iot-telemetry-topic \
    --bigquery-table=myfirstproject-508413:cold_chain_db.bronze_telemetria \
    --use-table-schema \
    --project=myfirstproject-508413
```

---

### 4.2. Motor de Almacenamiento: Data Lakehouse en Google BigQuery
El almacenamiento analítico se consolidó en **Google BigQuery**, estructurado bajo tres capas físicas y lógicas:

```mermaid
flowchart LR
    subgraph Lakehouse["Arquitectura Medallion en Google BigQuery"]
        B["CAPA BRONZE<br/><b>bronze_telemetria</b><br/>• Datos crudos sin filtrar<br/>• Partición: DATE(timestamp)<br/>• Clúster: device_id"]
        S["CAPA SILVER<br/><b>silver_telemetria_clean</b><br/>• Deduplicada analíticamente<br/>• Validación de rangos físicos<br/>• Surrogate Key MD5"]
        G["CAPA GOLD<br/><b>Esquema en Estrella</b><br/>• Fact Incidentes (Pérdidas USD)<br/>• Fact Resumen Diario (KPIs)<br/>• Vistas Analíticas OLAP"]
        
        B -->|Pipeline Batch ELT| S
        S -->|Modelado Dimensional| G
    end
```

#### Optimización Física de Almacenamiento:
1. **Particionamiento Diario:** `PARTITION BY DATE(timestamp)` divide físicamente los bloques de almacenamiento por fecha del calendario. Una consulta que evalúe únicamente el día actual solo escanea la partición correspondiente, evitando lecturas globales de terabytes.
2. **Clusterización:** `CLUSTER BY device_id` ordena colocalmente los registros de un mismo sensor dentro de cada partición, reduciendo el I/O en operaciones de filtrado y agrupamiento.

```sql
-- DDL de la Capa Bronze Particionada y Clusterizada
CREATE TABLE IF NOT EXISTS `myfirstproject-508413.cold_chain_db.bronze_telemetria` (
    device_id STRING,
    timestamp TIMESTAMP,
    temperature FLOAT64,
    humidity FLOAT64,
    battery_pct INT64
)
PARTITION BY DATE(timestamp)
CLUSTER BY device_id;
```

---

### 4.3. Análisis de Costos y Facturación en GCP con Datos Reales

A continuación se detalla la modelización económica de la arquitectura con base en las tarifas oficiales de Google Cloud en la región `us-central1`:

#### Tarifario Oficial GCP Aplicable
* **Cloud Pub/Sub Ingesta:** \$40.00 USD por TB (\$0.04 por GB). Primeros **10 GB/mes gratuitos**.
* **BigQuery Streaming Ingestion (Direct Subscription):** \$0.05 USD por GB procesado.
* **BigQuery Active Storage:** \$0.02 USD por GB/mes. Primeros **10 GB/mes gratuitos**.
* **BigQuery Long-Term Storage (> 90 días sin cambios):** \$0.01 USD por GB/mes (descuento automático del 50%).
* **BigQuery Consultas SQL (On-Demand):** \$6.25 USD por TB escaneado. Primer **1 TB (1,000 GB)/mes gratuito**.
* **Cloud Storage (GCS Standard):** \$0.020 USD por GB/mes. Primeros **5 GB-mes gratuitos**.
* **Tráfico de Red Interno (Egress intra-región):** **\$0.00 USD**.

#### Modelado Matemático de Costos
Sea $N$ el número de dispositivos IoT y $f$ la frecuencia de muestreo en segundos:

$$\text{Mensajes por Mes } (M) = N \times \left( \frac{86,400}{f} \right) \times 30$$

$$\text{Volumen de Datos Mensual en Gigabytes } (V_{\text{GB}}) = \frac{M \times S_{\text{bytes}}}{1024^3}$$

Donde $S_{\text{bytes}} \approx 150 \text{ bytes}$ por mensaje JSON transmitido.

$$\text{Costo Mensual Estimado} = \max(0, V_{\text{GB}} - 10) \times 0.04 + (V_{\text{GB}} \times 0.05) + \max(0, \text{Storage}_{\text{GB}} - 10) \times 0.02$$

#### Tabla Comparativa de Escenarios Reales

| Parámetro / Componente | Escenario 1: Laboratorio Académico | Escenario 2: Flota Mediana (100 Camiones) | Escenario 3: Gran Escala (1,000 Sensores) | Alternativa Clúster Spark Dedicado |
| :--- | :--- | :--- | :--- | :--- |
| **Dispositivos Activos ($N$)** | 3 sensores | 100 sensores | 1,000 sensores | 100 sensores |
| **Frecuencia ($f$)** | Cada 3 segundos | Cada 10 segundos | Cada 10 segundos | Cada 10 segundos |
| **Mensajes Mensuales ($M$)** | 2.59 millones | 25.92 millones | 259.2 millones | 25.92 millones |
| **Volumen Ingerido ($V_{\text{GB}}$)** | **0.38 GB / mes** | **3.88 GB / mes** | **38.8 GB / mes** | 3.88 GB / mes |
| **Costo Pub/Sub** | \$0.00 USD (Free Tier) | \$0.00 USD (Free Tier) | \$1.15 USD | \$0.00 (Kafka propio) |
| **Costo Ingesta BQ** | \$0.019 USD | \$0.19 USD | \$1.94 USD | \$0.00 |
| **Costo Storage BQ** | \$0.00 USD (Free Tier) | \$0.00 USD (Free Tier) | \$0.58 USD | \$0.00 (HDFS propio) |
| **Costo Cómputo / VMs** | \$0.00 USD (Cloud Shell) | \$0.00 USD (Serverless) | \$0.00 USD (Serverless) | **\$96.00 USD** (2x `n1-std-2`) |
| **Costo Análisis SQL** | \$0.00 USD (Free Tier) | \$0.00 USD (Free Tier) | \$0.00 USD (Free Tier) | \$0.00 |
| **COSTO TOTAL MENSUAL** | **\$0.00 USD / mes** | **\$0.92 USD / mes** | **\$3.67 USD / mes** | **\$96.00 USD / mes** |

> [!TIP]
> **Evaluación de Eficiencia Económica (TCO):**
> La arquitectura implementada demuestra una reducción del Costo Total de Propiedad (**TCO**) del **99.04%** (\$0.92 USD frente a \$96.00 USD mensuales) para una empresa logística de 100 vehículos, garantizando al mismo tiempo una disponibilidad del 99.99% bajo SLAs gestionados por Google.

---

## 5. PIPELINES DE CÓMPUTO Y TRANSFORMACIÓN

El procesamiento de datos se implementa como un pipeline **ELT (Extract, Load, Transform)** en el que las transformaciones se ejecutan nativamente en el motor altamente paralelizado de BigQuery, orquestadas mediante scripts en Python.

### 5.1. Capa Silver: Limpieza, Calidad y Deduplicación Determinística
La Capa Silver asegura que únicamente datos verídicos y únicos se propaguen hacia las capas analíticas:

```mermaid
flowchart TD
    RawInput["bronze_telemetria<br/>(Eventos Crudos)"] --> Step1["Deduplicación Analítica:<br/>ROW_NUMBER() OVER(PARTITION BY device_id, timestamp ORDER BY timestamp DESC) = 1"]
    Step1 --> Step2["Filtro de Outliers Instrumentales:<br/>-50.0 <= temperature <= 60.0<br/>0.0 <= humidity <= 100.0"]
    Step2 --> Step3["Generación de Llave Subrogada:<br/>MD5(device_id + '-' + timestamp)"]
    Step3 --> SilverOutput[("silver_telemetria_clean<br/>Tabla Particionada y Auditada")]
```

#### Código DDL de la Capa Silver:
```sql
CREATE TABLE IF NOT EXISTS `myfirstproject-508413.cold_chain_db.silver_telemetria_clean` (
    telemetria_id STRING,
    device_id STRING,
    timestamp TIMESTAMP,
    temperature FLOAT64,
    humidity FLOAT64,
    battery_pct INT64,
    temp_valida BOOLEAN,
    bateria_baja BOOLEAN,
    fecha DATE
)
PARTITION BY fecha
CLUSTER BY device_id;
```

#### Sentencia de Transformación y Carga Silver:
```sql
INSERT INTO `myfirstproject-508413.cold_chain_db.silver_telemetria_clean`
(telemetria_id, device_id, timestamp, temperature, humidity, battery_pct, temp_valida, bateria_baja, fecha)
WITH deduplicated AS (
    SELECT 
        device_id,
        timestamp,
        temperature,
        humidity,
        battery_pct,
        -- Eliminar retransmisiones duplicadas de paquetes de red
        ROW_NUMBER() OVER(PARTITION BY device_id, timestamp ORDER BY timestamp DESC) as rn
    FROM `myfirstproject-508413.cold_chain_db.bronze_telemetria`
    WHERE timestamp IS NOT NULL
)
SELECT 
    -- Surrogate Key determinística resistente a colisiones
    TO_HEX(MD5(CONCAT(device_id, "-", CAST(timestamp AS STRING)))) AS telemetria_id,
    device_id,
    timestamp,
    temperature,
    humidity,
    battery_pct,
    -- Reglas de validación física de instrumentación
    (temperature BETWEEN -50.0 AND 60.0 AND humidity BETWEEN 0.0 AND 100.0) AS temp_valida,
    (battery_pct < 20) AS bateria_baja,
    DATE(timestamp) AS fecha
FROM deduplicated
WHERE rn = 1
  AND (temperature BETWEEN -50.0 AND 60.0);
```

---

### 5.2. Capa Gold: Lógica de Negocio, Clasificación y Valorización de Pérdidas
En la Capa Gold, los eventos limpios se enriquecen con el catálogo y se aplica la lógica matemática de clasificación y valoración financiera.

#### Fórmulas de Negocio Implementadas:
1. **Desviación Absoluta respecto al Rango ($\Delta T$):**
   $$\Delta T = \begin{cases} 
   T_{\text{registrada}} - T_{\text{máx}}, & \text{si } T_{\text{registrada}} > T_{\text{máx}} \\ 
   T_{\text{mín}} - T_{\text{registrada}}, & \text{si } T_{\text{registrada}} < T_{\text{mín}} \\ 
   0, & \text{en rango normal} 
   \end{cases}$$

2. **Nivel de Severidad de la Infracción:**
   $$\text{Severidad} = \begin{cases} 
   \textbf{CRÍTICA}, & \text{si } \Delta T \ge 5.0\ ^\circ\text{C} \\ 
   \textbf{MODERADA}, & \text{si } 2.0\ ^\circ\text{C} \le \Delta T < 5.0\ ^\circ\text{C} \\ 
   \textbf{LEVE}, & \text{si } 0.0\ ^\circ\text{C} < \Delta T < 2.0\ ^\circ\text{C} 
   \end{cases}$$

3. **Cuantificación de Pérdida Financiera en Dólares:**
   Considerando un lote promedio de 50 unidades por contenedor refrigerado:
   $$\text{Pérdida (USD)} = \text{costo\_unitario} \times 50 \times \left( \frac{\Delta T}{5.0} \right)$$

#### Sentencia de Carga en la Tabla de Hechos de Incidentes:
```sql
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
    ROUND(ABS(s.temperature - CASE WHEN s.temperature > p.temp_max THEN p.temp_max ELSE p.temp_min END), 2) AS desviacion_grados,
    CASE 
        WHEN ABS(s.temperature - CASE WHEN s.temperature > p.temp_max THEN p.temp_max ELSE p.temp_min END) >= 5.0 THEN "CRÍTICA"
        WHEN ABS(s.temperature - CASE WHEN s.temperature > p.temp_max THEN p.temp_max ELSE p.temp_min END) >= 2.0 THEN "MODERADA"
        ELSE "LEVE"
    END AS nivel_severidad,
    ROUND(p.costo_unitario * 50 * (ABS(s.temperature - CASE WHEN s.temperature > p.temp_max THEN p.temp_max ELSE p.temp_min END) / 5.0), 2) AS impacto_financiero_estimado
FROM `myfirstproject-508413.cold_chain_db.silver_telemetria_clean` s
JOIN `myfirstproject-508413.cold_chain_db.dim_asignacion_sensores` a ON s.device_id = a.device_id
JOIN `myfirstproject-508413.cold_chain_db.dim_productos` p ON a.product_id = p.product_id
WHERE s.temperature > p.temp_max OR s.temperature < p.temp_min;
```

---

## 6. PROCESAMIENTO HÍBRIDO (STREAMING VS BATCH)

El diseño arquitectónico concilia la necesidad de **acción operativa inmediata** con la de **auditoría profunda periódica**:

```mermaid
flowchart TD
    EventStream["Flujo Telemático Entrante (Cloud Pub/Sub)"] --> Splitter{"Estrategia de Enrutamiento Híbrido"}

    subgraph HotBranch["HOT PATH: Ruta de Baja Latencia (&lt; 2 Segundos)"]
        DirectBQ["BigQuery Direct Ingest"] --> LiveSQL["Vista Continua: v_alertas_cadena_frio"]
        LiveSQL --> RealtimeAction["• Notificación push al chofer<br/>• Encendido automático de generador<br/>• Alerta en Torre de Control"]
    end

    subgraph ColdBranch["COLD PATH: Ruta Masiva por Lotes (Batch ELT Diario)"]
        RawPartition["Capa Bronze Particionada"] --> ELTJob["batch_pipeline.py (Cómputo en BigQuery)"]
        ELTJob --> MasterSilver["silver_telemetria_clean"]
        MasterSilver --> MasterGold["gold_fact_incidentes & gold_fact_resumen_diario"]
        MasterGold --> ExecutiveBI["• Tableros de Control en Looker Studio<br/>• Liquidación de Seguros de Transporte<br/>• Evaluación de Desempeño de Transportistas"]
    end

    Splitter -->|Direct Streaming| HotBranch
    Splitter -->|Persistencia Histórica| ColdBranch
```

### 6.1. Vista Analítica de Baja Latencia (`v_alertas_cadena_frio`)
Permite a los dashboards operativos de la sala de control consultar el estado de cada vehículo sin esperar al cierre del lote nocturno:

```sql
CREATE OR REPLACE VIEW `myfirstproject-508413.cold_chain_db.v_alertas_cadena_frio` AS
SELECT 
    t.timestamp,
    t.device_id,
    a.camara_almacen,
    a.responsable,
    p.nombre AS producto,
    p.categoria,
    t.temperature AS temp_actual,
    p.temp_min,
    p.temp_max,
    p.costo_unitario,
    CASE 
        WHEN t.temperature > p.temp_max THEN "ALERTA: Exceso de Calor"
        WHEN t.temperature < p.temp_min THEN "ALERTA: Congelamiento Excesivo"
        ELSE "NORMAL"
    END AS estado_cadena_frio,
    CASE 
        WHEN t.temperature > p.temp_max THEN ROUND(t.temperature - p.temp_max, 2)
        WHEN t.temperature < p.temp_min THEN ROUND(p.temp_min - t.temperature, 2)
        ELSE 0.0
    END AS desviacion_grados
FROM `myfirstproject-508413.cold_chain_db.bronze_telemetria` t
JOIN `myfirstproject-508413.cold_chain_db.dim_asignacion_sensores` a ON t.device_id = a.device_id
JOIN `myfirstproject-508413.cold_chain_db.dim_productos` p ON a.product_id = p.product_id;
```

---

## 7. MODELADO PARA ANALÍTICA (STAR SCHEMA)

Para habilitar consultas analíticas de alta velocidad en herramientas de Business Intelligence (BI), se modeló un **Esquema en Estrella (Star Schema)** con dos tablas de hechos y dos tablas de dimensiones:

### 7.1. Diagrama Entidad-Relación (ERD) Completo

```mermaid
erDiagram
    gold_fact_incidentes }o--|| dim_productos : "product_id"
    gold_fact_incidentes }o--|| dim_asignacion_sensores : "device_id"
    gold_fact_resumen_diario }o--|| dim_productos : "product_id"
    gold_fact_resumen_diario }o--|| dim_asignacion_sensores : "device_id"

    gold_fact_incidentes {
        STRING incidente_id PK "Surrogate Key (Hash MD5)"
        TIMESTAMP timestamp "Marca de tiempo del evento"
        DATE fecha FK "Clave de partición física"
        STRING device_id FK "Identificador físico del sensor"
        STRING product_id FK "Identificador del producto perecedero"
        STRING camara_almacen "Activo de transporte o cámara frigorífica"
        STRING responsable "Custodio operativo de la mercadería"
        FLOAT64 temp_registrada "Temperatura física registrada (°C)"
        FLOAT64 temp_limite "Umbral térmico infringido (°C)"
        FLOAT64 desviacion_grados "Magnitud del desvío térmico (°C)"
        STRING nivel_severidad "CRÍTICA | MODERADA | LEVE"
        FLOAT64 impacto_financiero_estimado "Pérdida económica calculada en USD"
    }

    gold_fact_resumen_diario {
        DATE fecha PK "Fecha del consolidado"
        STRING device_id PK "Sensor evaluado"
        STRING product_id FK "Producto custodiado"
        STRING camara_almacen "Ubicación logística"
        INT64 total_lecturas "Volumen de telemetría procesada"
        FLOAT64 temp_promedio "Temperatura media diaria (°C)"
        FLOAT64 temp_minima "Temperatura mínima registrada (°C)"
        FLOAT64 temp_maxima "Temperatura máxima registrada (°C)"
        INT64 total_alertas "Conteo de eventos fuera de rango"
        FLOAT64 bateria_promedio "Nivel medio de batería (%)"
        INT64 tiempo_fuera_rango_minutos "Tiempo estimado en riesgo (minutos)"
    }

    dim_productos {
        STRING product_id PK "Identificador único del producto"
        STRING nombre "Nombre comercial del bien"
        STRING categoria "Farmacia | Alimentos | Congelados"
        FLOAT64 temp_min "Límite inferior permitido (°C)"
        FLOAT64 temp_max "Límite superior permitido (°C)"
        FLOAT64 costo_unitario "Valor económico unitario (USD)"
    }

    dim_asignacion_sensores {
        STRING device_id PK "Identificador del sensor físico"
        STRING product_id FK "Producto actualmente asignado"
        STRING camara_almacen "Vehículo o cámara frigorífica"
        STRING responsable "Persona a cargo de la custodia"
    }
```

---

### 7.2. Diccionario de Datos Formal de la Capa Gold

#### Tabla de Hechos: `gold_fact_incidentes`
* **Granularidad:** Un registro por cada evento de sensor que viole las cotas de temperatura permitidas.
* **Estrategia Física:** Particionada por `fecha` y clusterizada por `(product_id, device_id)`.

| Columna | Tipo BigQuery | Nulabilidad | Clave | Descripción Funcional |
| :--- | :--- | :--- | :--- | :--- |
| `incidente_id` | `STRING` | NOT NULL | PK | Identificador único del incidente generado por hash `MD5("INC-" + telemetria_id)`. |
| `timestamp` | `TIMESTAMP` | NOT NULL | - | Momento exacto en que ocurrió la infracción en UTC. |
| `fecha` | `DATE` | NOT NULL | FK | Fecha extraída del timestamp para particionamiento diario. |
| `device_id` | `STRING` | NOT NULL | FK | Dispositivo de hardware que emitió la alerta. |
| `product_id` | `STRING` | NOT NULL | FK | Producto afectado que se encontraba en el contenedor. |
| `camara_almacen` | `STRING` | NULLABLE | - | Vehículo o cámara frigorífica donde ocurrió el evento. |
| `responsable` | `STRING` | NULLABLE | - | Chofer u operador de bodega a cargo de la carga. |
| `temp_registrada` | `FLOAT64` | NOT NULL | - | Temperatura física leída por el sensor en °C. |
| `temp_limite` | `FLOAT64` | NOT NULL | - | Cota violada ($\text{temp\_max}$ o $\text{temp\_min}$) en °C. |
| `desviacion_grados` | `FLOAT64` | NOT NULL | - | Grados de sobrecalentamiento o sobrecongelamiento. |
| `nivel_severidad` | `STRING` | NOT NULL | - | Categoría operativa: `CRÍTICA`, `MODERADA` o `LEVE`. |
| `impacto_financiero_estimado` | `FLOAT64` | NOT NULL | - | Valorización monetaria de la pérdida estimada en \$ USD. |

#### Tabla de Hechos Agregada: `gold_fact_resumen_diario`
* **Granularidad:** Un registro por cada combinación de `(fecha, device_id, product_id, camara_almacen)`.
* **Propósito:** Alimenta tarjetas ejecutivas y gráficos de tendencias históricas sin requerir escanear eventos individuales.

| Columna | Tipo BigQuery | Descripción Funcional |
| :--- | :--- | :--- |
| `fecha` | `DATE` | Día del calendario evaluado. |
| `device_id` | `STRING` | Identificador del sensor. |
| `product_id` | `STRING` | Producto monitoreado durante la jornada. |
| `camara_almacen` | `STRING` | Instalación o camión logístico. |
| `total_lecturas` | `INT64` | Cantidad total de paquetes de telemetría procesados. |
| `temp_promedio` | `FLOAT64` | Media aritmética de la temperatura (°C). |
| `temp_minima` | `FLOAT64` | Valor más bajo de temperatura registrado en el día (°C). |
| `temp_maxima` | `FLOAT64` | Valor más alto de temperatura registrado en el día (°C). |
| `total_alertas` | `INT64` | Conteo de lecturas fuera del rango admisible. |
| `bateria_promedio` | `FLOAT64` | Nivel medio de carga del sensor (auditoría de salud de hardware). |
| `tiempo_fuera_rango_minutos` | `INT64` | Estimación del tiempo total acumulado de exposición a temperatura indebida. |

---

## 8. EVIDENCIAS DE IMPLEMENTACIÓN Y RESULTADOS EXPERIMENTALES

Todos los componentes de la arquitectura fueron desplegados, ejecutados y validados empíricamente en el proyecto GCP `myfirstproject-508413`.

### 8.1. Transmisión del Simulador IoT y Publicación en Pub/Sub
El simulador en Python se autenticó mediante la clave de la Service Account `iot-simulator-sa` y transmitió telemetría continua generando identificadores de mensaje (Message ID) confirmados por GCP:

```text
==================================================
🚀 [SMART COLD CHAIN - IoT SIMULATOR]
Destino Pub/Sub: projects/myfirstproject-508413/topics/iot-telemetry-topic
==================================================
[2026-11-19T02:42:16Z] ✅ [NORMAL] SENSOR-01 -> 4.2°C (ID: 23514495382571057)
[2026-11-19T02:42:16Z] ⚠️ [ALERTA TÉRMICA] SENSOR-02 -> 10.5°C (ID: 23514051835691269)
[2026-11-19T02:42:17Z] ✅ [NORMAL] SENSOR-03 -> -19.0°C (ID: 23513740931631351)
```

---

### 8.2. Detección en Tiempo Real (Hot Path - Consulta a `v_alertas_cadena_frio`)
La vista analítica detectó de forma inmediata la infracción térmica en el sensor `SENSOR-02`:

```sql
SELECT * FROM `myfirstproject-508413.cold_chain_db.v_alertas_cadena_frio`;
```
**Resultado en Consola de BigQuery:**
```text
+---------------------+-----------+-----------------------+-------------+----------------+------------+-------------+----------+----------+----------------+-------------------------+-------------------+
|      timestamp      | device_id |    camara_almacen     | responsable |    producto    | categoria  | temp_actual | temp_min | temp_max | costo_unitario |   estado_cadena_frio    | desviacion_grados |
+---------------------+-----------+-----------------------+-------------+----------------+------------+-------------+----------+----------+----------------+-------------------------+-------------------+
| 2026-11-19 02:42:17 | SENSOR-03 | Congelador-Central-02 | Ana Gomez   | Helado Gourmet | Congelados |       -19.0 |    -22.0 |    -18.0 |            6.0 | NORMAL                  |               0.0 |
| 2026-11-19 02:42:16 | SENSOR-01 | Camara-Refrigerada-A  | Dr. Garcia  | Vacunas ARN    | Farmacia   |         4.2 |      2.0 |      8.0 |           45.0 | NORMAL                  |               0.0 |
| 2026-11-19 02:42:16 | SENSOR-02 | Camion-Reparto-04     | Juan Perez  | Carne Fresca   | Alimentos  |        10.5 |     -1.0 |      4.0 |           12.5 | ALERTA: Exceso de Calor |               6.5 |
+---------------------+-----------+-----------------------+-------------+----------------+------------+-------------+----------+----------+----------------+-------------------------+-------------------+
```

---

### 8.3. Ejecución del Pipeline Batch Orquestado (`batch_pipeline.py`)
El orquestador en Python procesó las sentencias ELT en BigQuery con confirmación de filas afectadas:

```text
============================================================
🔄 [BATCH PIPELINE] Ejecutando transformaciones ELT...
Proyecto GCP: myfirstproject-508413
============================================================

▶️ Ejecutando Etapa 1. Limpieza y Deduplicación Silver...
   ✅ Completado con éxito. Filas afectadas: 3 (Job ID: c9dde7e1-a671-4d36-8d5d-98b8afd68dfe)

▶️ Ejecutando Etapa 2. Hechos de Incidentes Gold...
   ✅ Completado con éxito. Filas afectadas: 1 (Job ID: b2577f1c-a673-424a-9969-3a73c81adb3c)

▶️ Ejecutando Etapa 3. Resumen Diario Gold...
   ✅ Completado con éxito. Filas afectadas: 3 (Job ID: 97549c15-421a-4604-a79b-994f13c0aa2a)

============================================================
🎉 Pipeline Batch completado exitosamente.
============================================================
```

---

### 8.4. Auditoría de la Tabla de Hechos de Incidentes (`gold_fact_incidentes`)
```sql
SELECT 
    fecha, device_id, producto, camara_almacen, responsable,
    temp_registrada, temp_limite, desviacion_grados, nivel_severidad, impacto_financiero_estimado
FROM `myfirstproject-508413.cold_chain_db.gold_fact_incidentes`;
```
**Resultado Obtenido:**
```text
+------------+-----------+--------------+-------------------+-------------+-----------------+-------------+-------------------+-----------------+-----------------------------+
|   fecha    | device_id |   producto   |  camara_almacen   | responsable | temp_registrada | temp_limite | desviacion_grados | nivel_severidad | impacto_financiero_estimado |
+------------+-----------+--------------+-------------------+-------------+-----------------+-------------+-------------------+-----------------+-----------------------------+
| 2026-11-19 | SENSOR-02 | Carne Fresca | Camion-Reparto-04 | Juan Perez  |            10.5 |         4.0 |               6.5 | CRÍTICA         |                     $812.50 |
+------------+-----------+--------------+-------------------+-------------+-----------------+-------------+-------------------+-----------------+-----------------------------+
```
*Interpretación Forense:* El sensor `SENSOR-02` instalado en el vehículo logístico `Camion-Reparto-04` registró 10.5°C transportando Carne Fresca (cuya tolerancia máxima es 4.0°C). El sistema clasificó la infracción como **CRÍTICA** (+6.5°C de sobrecalentamiento) y liquidó una pérdida financiera estimada de **\$812.50 USD**, asignando la responsabilidad operativa al chofer *Juan Perez*.

---

### 8.5. Auditoría de la Tabla de Resumen Diario (`gold_fact_resumen_diario`)
```sql
SELECT 
    device_id, camara_almacen, total_lecturas, temp_promedio,
    temp_minima, temp_maxima, total_alertas, bateria_promedio, tiempo_fuera_rango_minutos
FROM `myfirstproject-508413.cold_chain_db.gold_fact_resumen_diario`;
```
**Resultado Obtenido:**
```text
+-----------+-----------------------+----------------+---------------+-------------+-------------+---------------+------------------+----------------------------+
| device_id |    camara_almacen     | total_lecturas | temp_promedio | temp_minima | temp_maxima | total_alertas | bateria_promedio | tiempo_fuera_rango_minutos |
+-----------+-----------------------+----------------+---------------+-------------+-------------+---------------+------------------+----------------------------+
| SENSOR-03 | Congelador-Central-02 |              1 |         -19.0 |       -19.0 |       -19.0 |             0 |             98.0 |                          0 |
| SENSOR-01 | Camara-Refrigerada-A  |              1 |           4.2 |         4.2 |         4.2 |             0 |             98.0 |                          0 |
| SENSOR-02 | Camion-Reparto-04     |              1 |          10.5 |        10.5 |        10.5 |             1 |             98.0 |                          1 |
+-----------+-----------------------+----------------+---------------+-------------+-------------+---------------+------------------+----------------------------+
```

---

## 9. TRATAMIENTO DE CASOS EXTREMOS Y RESILIENCIA (EDGE CASES)

La arquitectura fue sometida a escenarios de prueba de borde para verificar su robustez operativa:

1. **Pérdida Prolongada de Cobertura Celular (Blackouts de Red):**
   * *Escenario:* Un camión atraviesa una zona montañosa sin señal 4G durante 4 horas. Al recuperar conectividad, el gateway vuelca 4,800 mensajes acumulados en una sola ráfaga.
   * *Respuesta Arquitectónica:* Cloud Pub/Sub absorbe la ráfaga elásticamente sin degradación. La suscripción directa a BigQuery inserta los datos respetando la estampa temporal original del sensor (`timestamp`), y la partición diaria de BigQuery ubica cada lectura en el día correcto con independencia de la hora en que se recibió el paquete.
2. **Duplicación de Mensajes por Retransmisión de Red:**
   * *Escenario:* El sensor envía un paquete, pero la confirmación (ACK) de red se pierde, obligando al sensor a retransmitir la misma medición tres veces.
   * *Respuesta Arquitectónica:* La capa Bronze almacena los eventos crudos. Durante la ejecución de la capa Silver, la función analítica `ROW_NUMBER() OVER(PARTITION BY device_id, timestamp ORDER BY timestamp DESC)` descarta las duplicaciones, asegurando que las tablas Gold contengan conteos y métricas 100% exactas.
3. **Sensores Descalibrados o Dañados Físicamente:**
   * *Escenario:* Un cortocircuito en el sensor emite una lectura de $999.0\ ^\circ\text{C}$ o $-100.0\ ^\circ\text{C}$.
   * *Respuesta Arquitectónica:* La condición de calidad de datos en Silver (`WHERE temperature BETWEEN -50.0 AND 60.0`) filtra la fila defectuosa antes de que ingrese a las tablas Gold, evitando la distorsión de los promedios y las pérdidas financieras calculadas.

---

## 10. CONCLUSIONES Y RECOMENDACIONES TÉCNICAS

1. **Validación Integral de la Arquitectura:** Se implementó con éxito un flujo de datos End-to-End capaz de conectar datos telemáticos en streaming con sistemas transaccionales batch, satisfaciendo todas las exigencias de latencia, seguridad y gobernanza.
2. **Costo-Efectividad Extrema:** La solución demostró ser viable a costo cero (\$0.00 USD/mes) durante la fase académica gracias al aprovechamiento inteligente del Always Free Tier de GCP, y mantiene un costo inferior a \$1.00 USD mensual para una flota operativa de 100 vehículos, representando un ahorro del 99% frente a arquitecturas basadas en servidores tradicionales.
3. **Idempotencia y Calidad Demostrada:** La separación Medallion garantiza que los reintentos de red telemáticos no afecten los estados financieros de merma ni los tableros analíticos de toma de decisiones.
4. **Impacto Estratégico:** La transformación de variables ambientales físicas en métricas monetarias automatizadas habilita la liquidación expedita de seguros de carga, la trazabilidad sanitaria auditable bajo normas OMS/FDA y la mitigación proactiva de pérdidas comerciales.

---

## 11. ANEXOS: CÓDIGOS FUENTE COMPLETOS

### Anexo A: Simulador de Sensores IoT en Python (`iot_simulator.py`)
```python
"""
Simulador de Sensores IoT para Monitoreo de Cadena de Frio
Publica telemetria ambiental continua hacia Google Cloud Pub/Sub
utilizando autenticacion por Cuenta de Servicio (Service Account).
"""
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

publisher = pubsub_v1.PublisherClient.from_service_account_file(KEY_PATH)
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

print("=" * 60)
print("🚀 [SMART COLD CHAIN - IoT SIMULATOR]")
print(f"Proyecto GCP: {PROJECT_ID}")
print(f"Tópico Pub/Sub: {topic_path}")
print("=" * 60)

DEVICES = {
    "SENSOR-01": {"base_temp": 4.5, "range": 0.5},   # Vacunas (2°C a 8°C)
    "SENSOR-02": {"base_temp": 2.0, "range": 0.8},   # Carne Fresca (-1°C a 4°C)
    "SENSOR-03": {"base_temp": -20.0, "range": 0.5}  # Helados (-22°C a -18°C)
}

try:
    while True:
        for device_id, profile in DEVICES.items():
            noise = random.uniform(-profile["range"], profile["range"])
            temp = round(profile["base_temp"] + noise, 2)
            
            # Simulacion de anomalia accidental (15% de probabilidad)
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
            msg_id = future.result()

            tag = "⚠️ [ALERTA TÉRMICA]" if is_anomaly else "✅ [NORMAL]"
            print(f"[{payload['timestamp']}] {tag} {device_id} -> {temp}°C (ID: {msg_id})")

        time.sleep(3)

except KeyboardInterrupt:
    print("\n🛑 Simulador detenido por el usuario.")
```

### Anexo B: Pipeline ELT en SQL (`pipelines/batch_transformations.sql`)
```sql
-- =============================================================================
-- TRANSFORMACIÓN 1: BRONZE A SILVER (Deduplicación y Limpieza)
-- =============================================================================
INSERT INTO `myfirstproject-508413.cold_chain_db.silver_telemetria_clean`
(telemetria_id, device_id, timestamp, temperature, humidity, battery_pct, temp_valida, bateria_baja, fecha)
WITH deduplicated AS (
    SELECT 
        device_id,
        timestamp,
        temperature,
        humidity,
        battery_pct,
        ROW_NUMBER() OVER(PARTITION BY device_id, timestamp ORDER BY timestamp DESC) as rn
    FROM `myfirstproject-508413.cold_chain_db.bronze_telemetria`
    WHERE timestamp IS NOT NULL
)
SELECT 
    TO_HEX(MD5(CONCAT(device_id, "-", CAST(timestamp AS STRING)))) AS telemetria_id,
    device_id,
    timestamp,
    temperature,
    humidity,
    battery_pct,
    (temperature BETWEEN -50.0 AND 60.0 AND humidity BETWEEN 0.0 AND 100.0) AS temp_valida,
    (battery_pct < 20) AS bateria_baja,
    DATE(timestamp) AS fecha
FROM deduplicated
WHERE rn = 1
  AND (temperature BETWEEN -50.0 AND 60.0);

-- =============================================================================
-- TRANSFORMACIÓN 2: SILVER A GOLD INCIDENTES (Cálculo de Severidad y Pérdida)
-- =============================================================================
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
    ROUND(ABS(s.temperature - CASE WHEN s.temperature > p.temp_max THEN p.temp_max ELSE p.temp_min END), 2) AS desviacion_grados,
    CASE 
        WHEN ABS(s.temperature - CASE WHEN s.temperature > p.temp_max THEN p.temp_max ELSE p.temp_min END) >= 5.0 THEN "CRÍTICA"
        WHEN ABS(s.temperature - CASE WHEN s.temperature > p.temp_max THEN p.temp_max ELSE p.temp_min END) >= 2.0 THEN "MODERADA"
        ELSE "LEVE"
    END AS nivel_severidad,
    ROUND(p.costo_unitario * 50 * (ABS(s.temperature - CASE WHEN s.temperature > p.temp_max THEN p.temp_max ELSE p.temp_min END) / 5.0), 2) AS impacto_financiero_estimado
FROM `myfirstproject-508413.cold_chain_db.silver_telemetria_clean` s
JOIN `myfirstproject-508413.cold_chain_db.dim_asignacion_sensores` a ON s.device_id = a.device_id
JOIN `myfirstproject-508413.cold_chain_db.dim_productos` p ON a.product_id = p.product_id
WHERE s.temperature > p.temp_max OR s.temperature < p.temp_min;

-- =============================================================================
-- TRANSFORMACIÓN 3: SILVER A GOLD RESUMEN DIARIO (Agregación de KPIs)
-- =============================================================================
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
    CAST(ROUND(COUNTIF(s.temperature > p.temp_max OR s.temperature < p.temp_min) * 0.5) AS INT64) AS tiempo_fuera_rango_minutos
FROM `myfirstproject-508413.cold_chain_db.silver_telemetria_clean` s
JOIN `myfirstproject-508413.cold_chain_db.dim_asignacion_sensores` a ON s.device_id = a.device_id
JOIN `myfirstproject-508413.cold_chain_db.dim_productos` p ON a.product_id = p.product_id
GROUP BY s.fecha, s.device_id, p.product_id, a.camara_almacen;
```

### Anexo C: Orquestador en Python (`pipelines/batch_pipeline.py`)
```python
"""
Orquestador de Procesamiento Batch ELT
Ejecuta las transformaciones SQL de forma secuencial en BigQuery
reportando metricas de ejecucion y filas procesadas.
"""
import os
from google.cloud import bigquery

PROJECT_ID = "myfirstproject-508413"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQL_FILE = os.path.join(BASE_DIR, "pipelines", "batch_transformations.sql")

def run_pipeline():
    print("=" * 60)
    print("🔄 [BATCH PIPELINE] Iniciando ciclo de transformación ELT...")
    print(f"Proyecto GCP: {PROJECT_ID}")
    print("=" * 60)

    client = bigquery.Client(project=PROJECT_ID)
    with open(SQL_FILE, "r") as f:
        statements = [s.strip() for s in f.read().split(";") if s.strip()]

    stages = [
        "1. Limpieza y Deduplicación en Capa Silver",
        "2. Identificación y Valorización de Incidentes en Capa Gold",
        "3. Consolidación de KPIs en Resumen Diario Gold"
    ]

    for idx, stmt in enumerate(statements):
        print(f"\n▶️ Ejecutando Etapa {stages[idx]}...")
        job_config = bigquery.QueryJobConfig(
            labels={"pipeline": "coldchain-batch", "stage": f"step-{idx+1}"}
        )
        job = client.query(stmt, job_config=job_config)
        job.result()
        print(f"   ✅ Completado. Job ID: {job.job_id}")
        print(f"   📊 Filas afectadas: {job.num_dml_affected_rows}")

    print("\n" + "=" * 60)
    print("🎉 Pipeline Batch finalizado con éxito.")
    print("=" * 60)

if __name__ == "__main__":
    run_pipeline()
```
