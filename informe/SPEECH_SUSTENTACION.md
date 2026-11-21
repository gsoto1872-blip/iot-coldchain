# GUION MAESTRO DE SUSTENTACIÓN ORAL (SPEECH)
## Defensa de Proyecto de Ingeniería: Smart Cold Chain IoT en Google Cloud Platform
### Pitch Deck, Discurso Palabra por Palabra y Manual de Oratoria ante el Jurado

---

### FICHA TÉCNICA DEL DISCURSO Y PARÁMETROS DE EXPOSICIÓN

* **Sustentante:** Guillermo Soto
* **Proyecto GCP Activo:** `myfirstproject-508413` | **Región:** `us-central1` (Iowa, EE. UU.)
* **Repositorio de Código:** [https://github.com/gsoto1872-blip/iot-coldchain](https://github.com/gsoto1872-blip/iot-coldchain)
* **Tiempo Total Estimado:** 18 a 20 minutos de exposición + 10 minutos de ronda de preguntas (Q&A).
* **Herramientas de Apoyo:**
  - Diapositivas Interactivas: [SLIDES_SUSTENTACION.html](file:///home/gsoto1872/iot-coldchain/informe/SLIDES_SUSTENTACION.html)
  - Documento de Diapositivas Extendido: [SLIDES_SUSTENTACION.md](file:///home/gsoto1872/iot-coldchain/informe/SLIDES_SUSTENTACION.md)
  - Terminal en Vivo para Demostración: `python demo/demo_e2e.py`

---

### CONSEJOS DE ORATORIA, MODULACIÓN Y LENGUAJE CORPORAL

1. **Ritmo y Pausas:** Habla a una velocidad moderada (~120 a 140 palabras por minuto). En el guión encontrarás marcas como `[Pausa de 2 segundos]` para recordarte respirar y permitir que el jurado asimile los conceptos más potentes.
2. **Énfasis de Voz:** Las palabras y frases marcadas en **negrita** deben pronunciarse con mayor firmeza y volumen para proyectar seguridad técnica.
3. **Lenguaje Corporal:**
   - Mantén contacto visual equitativo con todos los miembros del jurado (mira 5 segundos a cada evaluador).
   - Utiliza las manos abiertas para enfatizar la escalabilidad y las transiciones del sistema.
   - Cuando menciones un dato en pantalla, gira el torso hacia la diapositiva y señálalo con la mano abierta: `[Señalar en pantalla]`.
4. **Manejo de la Seguridad:** Recuerda que **tú eres quien construyó el sistema y conoce cada línea de código**. No estás defendiendo una teoría: estás exponiendo una infraestructura que ya corrió, procesó datos y fue validada en Google Cloud.

---

### CRONOGRAMA MINUTO A MINUTO DE LA EXPOSICIÓN (PUNTOS OFICIALES)

```
====================================================================================================
TIEMPO TOTAL: 18 - 20 MINUTOS
----------------------------------------------------------------------------------------------------
[Min 00:00 - 01:30]  Slide 01: Portada, Presentación Personal y Ficha del Proyecto
[Min 01:30 - 03:00]  Slide 02: 1. Resumen ejecutivo - Alcance de la Migración/Implementación
[Min 03:00 - 04:30]  Slide 03: 2. Situación actual
[Min 04:30 - 06:00]  Slide 04: 3. Criterios de éxito, performance, en formato KPI
[Min 06:00 - 08:00]  Slide 05: 4. Productos tecnológicos a usar
[Min 08:00 - 09:30]  Slide 06: 5. Dependencias/supuestos o fuera de scope
[Min 09:30 - 12:00]  Slide 07: 6. Arquitectura final: (la arquitectura que generará la estimación de consumo del primer año)
[Min 12:00 - 14:00]  Slide 08: 7. Calculadora de consumo
[Min 14:00 - 17:00]  Slide 09: 8. Demo end to end de implementación
[Min 17:00 - 18:30]  Slide 10: 9. Conclusiones
[Min 18:30 - 19:30]  Slide 11: 10. Next Steps
[Min 19:30 - 20:30]  Slide 12: Defensa Técnica y Preguntas del Jurado (Q&A)
====================================================================================================
```

---

# DISCURSO COMPLETO PALABRA POR PALABRA

---

## DIAPOSITIVA 01: PORTADA EJECUTIVA E IDENTIFICACIÓN DEL PROYECTO
**Tiempo estimado:** 01:30 minutos  
**Diapositiva en pantalla:** Portada con badges de Google Cloud, ID del proyecto `myfirstproject-508413` y lema.

### 🎙️ Discurso Verbal:

> *"Buenos días señores miembros del jurado evaluador, profesor y compañeros presentes.*
>
> *Mi nombre es **Guillermo Soto** y el día de hoy tengo el honor de presentar la sustentación final de nuestro proyecto de ingeniería de datos titulado:*  
> ***'Smart Cold Chain IoT: Arquitectura End-to-End y Procesamiento Híbrido en Google Cloud Platform'**.*
>
> `[Pausa de 2 segundos. Mirar al jurado con seguridad]`
>
> *Este proyecto aborda una de las problemáticas logísticas más costosas e invisibles del comercio global: la ruptura de la cadena de frío en el transporte de vacunas biológicas, medicamentos de alta sensibilidad y alimentos perecederos.*
>
> `[Señalar badges en la diapositiva]`  
> *Quiero destacar desde el primer segundo que lo que verán hoy no es un boceto conceptual ni una simulación académica en un entorno local. Es una **arquitectura Serverless viva y operativa**, desplegada bajo el ID de proyecto `myfirstproject-508413` en la región `us-central1` de Google Cloud.*
>
> *A lo largo de los próximos 18 minutos demostraremos cómo cubrimos de forma exhaustiva los diez puntos fundamentales requeridos: desde el alcance de migración e implementación, pasando por los criterios de éxito en formato KPI, la arquitectura final que genera la estimación de consumo, la calculadora de costos del primer año, hasta la demostración práctica en vivo y las conclusiones.*
>
> *Los invito a comenzar con el primer punto: el Resumen Ejecutivo y Alcance de la Migración e Implementación."*

`[Transición: Presionar tecla Flecha Derecha o Espacio para pasar al Slide 2]`

---

## DIAPOSITIVA 02: 1. RESUMEN EJECUTIVO - ALCANCE DE LA MIGRACIÓN/IMPLEMENTACIÓN
**Tiempo estimado:** 01:30 minutos  
**Diapositiva en pantalla:** Tarjetas de Alcance de la Migración, Alcance de la Implementación y Procesamiento Híbrido.

### 🎙️ Discurso Verbal:

> *"Iniciemos con el **Punto 1: Resumen ejecutivo - Alcance de la Migración e Implementación**.*
>
> `[Señalar la tarjeta izquierda: Alcance de la Migración]`  
> *En primer lugar, el **alcance de la migración** aborda la modernización de la infraestructura tecnológica. La empresa operaba bajo un modelo heredado (*legacy*) caracterizado por dataloggers USB manuales, hojas de cálculo aisladas y bases de datos relacionales en servidores locales que sufrían graves problemas de concurrencia y contención de bloqueos. En lugar de hacer una migración básica de tipo 'Lift-and-Shift' —que habría significado trasladar máquinas virtuales caras a la nube—, ejecutamos un **Re-platforming hacia Cloud-Native Serverless** en Google Cloud Platform, desacoplando completamente el almacenamiento del cómputo.*
>
> `[Pausa de 1 segundo]`
>
> `[Señalar la tarjeta central: Alcance de la Implementación]`  
> *En segundo lugar, el **alcance de la implementación** construyó una plataforma integral de datos que unifica dos flujos:*
> * *El **flujo streaming de IoT**, que ingesta telemetría continua de temperatura, humedad y batería desde 100 sensores cada 10 segundos vía Cloud Pub/Sub.*
> * *Y el **flujo batch del ERP**, que aporta los catálogos maestros con tolerancias térmicas, costo unitario por kilogramo o dosis, chofer y vehículo asignado.*
>
> `[Señalar la tarjeta derecha: Procesamiento Híbrido]`  
> *Esta integración alimenta nuestro **procesamiento híbrido**: un **Hot Path** que en menos de 2 segundos alerta a la cabina del camión para desviar la carga a una cámara fría y evitar la pérdida física; y un **Cold Path** en batch que consolida la información diaria, deduplica registros y calcula la pérdida financiera en dólares para aseguradoras, exponiendo todo mediante una REST API en FastAPI.*
>
> *Veamos a continuación el Punto 2: la Situación Actual."*

`[Transición: Pasar al Slide 3]`

---

## DIAPOSITIVA 03: 2. SITUACIÓN ACTUAL
**Tiempo estimado:** 01:30 minutos  
**Diapositiva en pantalla:** Diagrama de flujo comparativo y matriz As-Is vs To-Be.

### 🎙️ Discurso Verbal:

> *"Pasamos al **Punto 2: Situación actual**.*
>
> `[Señalar el diagrama superior: Flujo As-Is]`  
> *Para justificar esta solución debemos entender la precariedad de la situación actual en el transporte de carga refrigerada. Más del 70% de las empresas utilizan **dataloggers pasivos USB**. El transportista coloca un dispositivo USB entre las cajas y conduce durante 15 o 20 horas a través de la carretera.*
>
> *Al llegar a destino, el inspector de calidad descarga el archivo en su laptop y descubre que hace 10 horas el compresor falló y la mercadería se calentó a 15 grados. **Esto no es control de calidad; es una autopsia forense**. El 100% de la carga se destruye, se pierden miles de dólares y comienzan meses de disputas legales entre el dueño de la carga y el transportista.*
>
> `[Pausa de 2 segundos. Modular la voz hacia un tono positivo y resolutivo]`
>
> `[Señalar el diagrama inferior: Flujo To-Be]`  
> *Con nuestra situación implementada **To-Be**, transformamos esa reacción tardía en un **control activo y proactivo en tiempo real**. Si el compresor falla en la carretera, en menos de **2 segundos** el chofer y la torre de control reciben la notificación del exceso térmico. El conductor se desvía de inmediato a un almacén frigorífico cercano, se trasvasa la mercadería y **se salva el 100% del cargamento**.*
>
> *Y en costos de TI, reemplazamos servidores dedicados costosos por arquitectura Serverless, reduciendo el TCO en un 99.04%.*
>
> *Revisemos ahora el Punto 3: los Criterios de Éxito en formato KPI."*

`[Transición: Pasar al Slide 4]`

---

## DIAPOSITIVA 04: 3. CRITERIOS DE ÉXITO, PERFORMANCE, EN FORMATO KPI
**Tiempo estimado:** 01:30 minutos  
**Diapositiva en pantalla:** Tarjetas numéricas de KPIs (1.8s, 99.99%, 100%, 100%, 600ms, $0.00).

### 🎙️ Discurso Verbal:

> *"Continuamos con el **Punto 3: Criterios de éxito, performance, en formato KPI**.*
>
> *Para medir el éxito de la plataforma establecimos un Balanced Scorecard de datos con seis métricas cuantitativas estrictas:*
>
> `[Señalar la primera tarjeta: Latencia Hot Path]`  
> *1. **Latencia del Hot Path**: la meta de diseño era alertar en $\le 3.0$ segundos. En los ensayos reales sobre Google Cloud obtuvimos **1.8 segundos**, superando holgadamente el objetivo.*
>
> `[Señalar la segunda tarjeta: Disponibilidad]`  
> *2. **Disponibilidad de Ingesta**: meta de $\ge 99.90\%$. Alcanzamos un **99.99%** respaldado por el SLA multi-zona de Cloud Pub/Sub.*
>
> `[Señalar la tercera tarjeta: Deduplicación Silver]`  
> *3. **Deduplicación en Capa Silver**: meta del 100%. Los reintentos celulares por pérdida de cobertura en carretera se eliminaron al **100%** mediante funciones de ventana analítica con `ROW_NUMBER()`, garantizando idempotencia matemática.*
>
> `[Señalar la cuarta tarjeta: Precisión Contable]`  
> *4. **Valoración Contable**: logramos el **100% de incidentes valorizados en USD** en la Capa Gold, sin valores nulos.*
>
> `[Señalar las tarjetas inferiores: Velocidad y Costos]`  
> *5. **Performance de Consultas**: gracias al particionado diario por fecha y clustering por dispositivo en BigQuery, las consultas complejas de auditoría responden en apenas **600 milisegundos**.*
> *6. **Eficiencia de Costos TI**: la meta era gastar $\le \$20$ USD mensuales. El resultado real en laboratorio fue de **$0.00 USD al mes** gracias al Always Free Tier de GCP.*
>
> *Veamos a continuación el Punto 4: los Productos Tecnológicos a usar."*

`[Transición: Pasar al Slide 5]`

---

## DIAPOSITIVA 05: 4. PRODUCTOS TECNOLÓGICOS A USAR
**Tiempo estimado:** 02:00 minutos  
**Diapositiva en pantalla:** Diagrama Mermaid de componentes y tabla de alternativas descartadas.

### 🎙️ Discurso Verbal:

> *"Entramos al **Punto 4: Productos tecnológicos a usar**.*
>
> `[Señalar el diagrama de flujo tecnológico]`  
> *La selección de componentes no respondió a modas, sino a un análisis estricto de trade-offs técnicos y económicos:*
>
> `[Señalar Cloud Pub/Sub]`  
> * *Para la ingesta elegimos **Google Cloud Pub/Sub**. Descartamos Apache Kafka porque exige mantener servidores dedicados con Zookeeper o KRaft encendidos las 24 horas del día, lo que generaría un costo fijo de más de 150 dólares mensuales en máquinas ociosas. Pub/Sub autoescala de 0 a millones de eventos y nos ofrece 10 GB gratuitos cada mes.*
>
> `[Señalar BigQuery Direct Ingestion]`  
> * *La pieza clave de la ingesta es **BigQuery Direct Ingestion**. Tradicionalmente se usaba Cloud Dataflow entre Pub/Sub y BigQuery. Sin embargo, para ingestar datos crudos a la Capa Bronze, Dataflow requería pagar workers de cómputo continuos. Con Direct Ingestion, Pub/Sub escribe de forma directa en BigQuery en 2 segundos, a solo 5 centavos por gigabyte y con cero líneas de código middleware.*
>
> `[Señalar BigQuery]`  
> * *Para el almacenamiento elegimos **Google BigQuery** frente a Cloud SQL. Las bases relacionales colapsan ante miles de escrituras concurrentes de sensores IoT por contención de bloqueos transaccionales. BigQuery almacena petabytes en formato columnar sin bloqueos.*
>
> `[Señalar Cloud IAM y FastAPI]`  
> * *En seguridad aplicamos el Principio de Menor Privilegio mediante una Service Account con rol estricto de publicación en Cloud IAM. Y para la exposición de servicios construimos una API REST en **FastAPI (Python 3.12)** con validación de contratos en Pydantic y documentación OpenAPI Swagger nativa.*
>
> *Revisemos ahora el Punto 5: Dependencias, Supuestos y Fuera de Scope."*

`[Transición: Pasar al Slide 6]`

---

## DIAPOSITIVA 06: 5. DEPENDENCIAS/SUPUESTOS O FUERA DE SCOPE
**Tiempo estimado:** 01:30 minutos  
**Diapositiva en pantalla:** Matriz de dependencias, supuestos y elementos fuera de scope.

### 🎙️ Discurso Verbal:

> *"Pasamos al **Punto 5: Dependencias/supuestos o fuera de scope**.*
>
> `[Señalar la primera fila: Conectividad Móvil]`  
> *Todo proyecto robusto debe explicitar sus dependencias y cómo mitiga los riesgos del entorno real:*
> * *La **dependencia crítica de conectividad celular 4G** se mitiga en el gateway IoT mediante un buffer local FIFO. Si el camión entra en un túnel sin señal durante dos horas, almacena las lecturas en memoria y las envía en ráfaga al salir. Pub/Sub absorbe el pico elásticamente y la Capa Silver reordena y deduplica.*
> * *La **dependencia regional en `us-central1`** se mitiga con la colocalización total de recursos en Iowa, garantizando que el tráfico de red interno tenga un costo de **$0.00 USD**.*
>
> `[Señalar los Supuestos y Fuera de Scope]`  
> *Entre los **supuestos**, establecimos un **Data Contract JSON estricto**: si un sensor defectuoso envía lecturas físicamente imposibles como 500°C, la Capa Silver las aísla en una tabla de cuarentena mediante un filtro físico de -50°C a +60°C. Asimismo, asumimos la constancia del costo unitario del lote durante el viaje congelándolo en la tabla `dim_productos`.*
>
> *Y dejamos formalmente **fuera de scope** la fabricación de circuitos físicos de hardware para concentrarnos en la arquitectura analítica en la nube, emulando la física telemática con Python.*
>
> *Llegamos ahora al Punto 6: la Arquitectura Final que generará la estimación de consumo del primer año."*

`[Transición: Pasar al Slide 7]`

---

## DIAPOSITIVA 07: 6. ARQUITECTURA FINAL: (LA ARQUITECTURA QUE GENERARÁ LA ESTIMACIÓN DE CONSUMO DEL PRIMER AÑO)
**Tiempo estimado:** 02:30 minutos  
**Diapositiva en pantalla:** Diagrama completo de las 4 etapas del Lakehouse Medallion y desglose de consumo por capa.

### 🎙️ Discurso Verbal:

> *"Llegamos al **Punto 6: Arquitectura final: (la arquitectura que generará la estimación de consumo del primer año)**.*
>
> `[Señalar el diagrama de arquitectura central]`  
> *Esta diapositiva representa el núcleo de ingeniería del proyecto. Es fundamental porque cada uno de los bloques que ven aquí define de manera matemática las métricas que alimentan nuestra calculadora de consumo del primer año:*
>
> `[Señalar Etapa 1 y 2: Ingesta]`  
> *1. **Ingesta Streaming (Pub/Sub):** Los 100 sensores emiten una lectura cada 10 segundos, generando **25.92 millones de mensajes al mes** ($\approx 3.88\text{ GB/mes}$) que entran al topic `iot-telemetry-topic`. Esto define el primer consumo.*
> *2. **Direct Ingestion:** Transfiere esos 3.88 GB mensuales directamente a BigQuery sin workers de cómputo.*
>
> `[Señalar Capa Bronze]`  
> *3. **Capa Bronze (`bronze_telemetria`):** Almacena el histórico crudo inmutable. Está particionada diariamente por `DATE(timestamp)` y clusterizada por `device_id`. Al cabo de 12 meses, acumula un volumen neto de **46.5 Gigabytes**, lo que define el consumo de almacenamiento.*
>
> `[Señalar Capa Silver]`  
> *4. **Capa Silver (`silver_telemetria_clean`):** El pipeline batch deduplica registros con `ROW_NUMBER()` y genera claves subrogadas MD5. Al ejecutarse dentro de BigQuery mediante SQL analítico, no genera costos de transferencia externa.*
>
> `[Señalar Capa Gold]`  
> *5. **Capa Gold (`gold_fact_incidentes` y `gold_fact_resumen_diario`):** Modela los hechos en un esquema en estrella cruzando con las tablas del ERP (`dim_productos`). Gracias al particionado y clustering, las consultas de auditoría solo escanean **~120 GB al mes**, definiendo el consumo de queries SQL.*
>
> `[Señalar Cloud Storage y Egress]`  
> *6. **Almacenamiento de Maestros y Red:** Cloud Storage almacena los CSVs del ERP (<100 MB), y como todos los servicios residen en `us-central1`, el tráfico de red interno es de cero dólares.*
>
> *Veamos de inmediato cómo esta arquitectura se traduce en números concretos en el Punto 7: la Calculadora de Consumo."*

`[Transición: Pasar al Slide 8]`

---

## DIAPOSITIVA 08: 7. CALCULADORA DE CONSUMO
**Tiempo estimado:** 02:00 minutos  
**Diapositiva en pantalla:** Ecuaciones de dimensionamiento, tabla de desglose por SKU y comparativa de TCO.

### 🎙️ Discurso Verbal:

> *"Pasamos al **Punto 7: Calculadora de consumo**.*
>
> `[Señalar las fórmulas de dimensionamiento]`  
> *A partir de la arquitectura que acabamos de revisar, realizamos el cálculo para una flota de 100 camiones transmitiendo continuamente:*  
> *100 vehículos $\times$ 8,640 lecturas al día $\times$ 30 días = **25,920,000 eventos mensuales**, lo que representa **3.88 Gigabytes al mes**.*
>
> `[Señalar la tabla de costos oficiales de GCP]`  
> *Aplicando las tarifas públicas oficiales de Google Cloud para `us-central1`:*
> * *En **Cloud Pub/Sub**: los 3.88 GB quedan 100% cubiertos por los **10 GB gratuitos mensuales** $\implies$ **$0.00 USD**.*
> * *En **BigQuery Ingesta Directa**: a $0.05 por GB procesado, pagamos apenas **$0.19 USD al mes** ($2.28 USD al año).*
> * *En **Almacenamiento de BigQuery**: tras 12 meses acumulamos 46.5 GB. Descontando los 10 GB gratuitos, el promedio mensual a $0.02/GB es de **$0.73 USD al mes** ($8.76 USD al año).*
> * *En **Consultas SQL de BigQuery**: escaneamos ~120 GB mensuales, totalmente cubiertos por el **1 Terabyte gratuito mensual** $\implies$ **$0.00 USD**.*
> * *En **Cloud Storage y Red Interna**: cubiertos por el Free Tier y tráfico colocalizado $\implies$ **$0.00 USD**.*
>
> `[Pausa de 2 segundos. Modular la voz con firmeza]`
>
> `[Señalar la fila de Total Facturación y Comparativa TCO]`  
> *El costo total del primer año es de apenas **$0.92 dólares al mes**, lo que equivale a **$11.04 dólares al año**.*
>
> *Si comparamos esto con la arquitectura tradicional de un clúster Dataproc de Spark con dos máquinas `n1-standard-2` encendidas 24/7, que cuesta **$1,152 dólares al año**, nuestra arquitectura Serverless genera un ahorro neto de **$1,140 dólares anuales**, lo que representa una **reducción del 99.04% en el Costo Total de Propiedad**.*
>
> *Veamos ahora el Punto 8: la Demostración Práctica End-to-End."*

`[Transición: Pasar al Slide 9]`

---

## DIAPOSITIVA 09: 8. DEMO END TO END DE IMPLEMENTACIÓN
**Tiempo estimado:** 03:00 minutos  
**Diapositiva en pantalla:** Diagrama de secuencia y trace de terminal de la prueba real.  
*(Opcional: Si el jurado solicita la terminal interactiva, pasar a la ventana de Cloud Shell y ejecutar `python demo/demo_e2e.py`)*

### 🎙️ Discurso Verbal:

> *"Llegamos al **Punto 8: Demo end to end de implementación**.*
>
> `[Señalar el diagrama de secuencia en pantalla]`  
> *Para comprobar el funcionamiento del pipeline corriendo de extremo a extremo, construimos un arnés de validación automatizado en el script `demo/demo_e2e.py` que recorre el ciclo de vida completo de un incidente:*
>
> * **Paso 1 (Inyección):** El sensor `SENSOR-02` instalado en el vehículo `Camion-Reparto-04`, conducido por Juan Perez, transporta un lote de **Carne Fresca** (500 kg valorizados a $5.00/kg). El límite térmico máximo tolerado es de **4.0°C**. El compresor sufre una avería y el sensor reporta **13.5°C**.
> * **Paso 2 (Pub/Sub):** El evento se empaqueta en JSON, se firma con la Service Account y se publica en Cloud Pub/Sub, recibiendo el identificador de confirmación `Message ID: 23550907518145894` en 120 milisegundos.
> * **Paso 3 (Bronze Streaming):** BigQuery Direct Ingestion persiste el dato en la tabla `bronze_telemetria` en **2.1 segundos**, sin servidores intermediarios.
> * **Paso 4 (Hot Path):** La vista SQL `v_alertas_cadena_frio` detecta de inmediato el **exceso térmico de +9.5°C** y activa la alerta roja en la torre de despacho.
> * **Paso 5 (Batch Pipeline):** El pipeline batch `batch_pipeline.py` deduplica en la Capa Silver y liquida en la Capa Gold: al superar los 5°C de desviación, clasifica la severidad como **CRÍTICA** y calcula la merma contable: 500 kg con castigo del 47.5% arroja una **pérdida financiera de $1,187.50 USD**.
> * **Paso 6 (REST API):** El endpoint `/api/v1/incidents?severity=CRÍTICA` de nuestra API REST en FastAPI responde `HTTP 200 OK` entregando el JSON auditado.
> * **Paso 7 (Decisión Prescriptiva):** El sistema emite la orden de desvío inmediato al chofer Juan Perez hacia una cámara frigorífica de contingencia y bloquea el lote en el sistema WMS para que no llegue al consumidor.
>
> `[Pausa de 2 segundos]`
> *El pipeline funcionó de extremo a extremo, cerrando el ciclo entre el sensor de campo y el balance financiero corporativo.*
>
> *Pasemos ahora al Punto 9: las Conclusiones."*

`[Transición: Pasar al Slide 10]`

---

## DIAPOSITIVA 10: 9. CONCLUSIONES
**Tiempo estimado:** 01:30 minutos  
**Diapositiva en pantalla:** Cuatro pilares de conclusiones (Factibilidad, Gobernanza, Finanzas, Negocio).

### 🎙️ Discurso Verbal:

> *"Entramos al **Punto 9: Conclusiones**.*
>
> `[Señalar punto 1: Factibilidad Técnica]`  
> *Primero, **Factibilidad Técnica Serverless Comprobada**: demostramos que no se requieren clústeres complejos ni servidores dedicados para procesar IoT a gran escala. La integración nativa de Cloud Pub/Sub Direct Ingestion y BigQuery ofrece escalabilidad masiva con cero mantenimiento de infraestructura.*
>
> `[Señalar punto 2: Gobernanza ALCOA+]`  
> *Segundo, **Gobernanza y Calidad Matemática**: la inmutabilidad de la Capa Bronze unida a la deduplicación analítica en la Capa Silver con `ROW_NUMBER()` garantiza que las fluctuaciones de red móvil no dupliquen incidentes ni distorsionen los libros contables, cumpliendo con los estándares de integridad de datos exigidos por la FDA.*
>
> `[Señalar punto 3: Disrupción en TCO]`  
> *Tercero, **Eficiencia Económica Radical**: reducir el costo anual de infraestructura de **$1,152 dólares a tan solo $11 dólares** mediante arquitectura Serverless representa un ahorro del 99.04%, demostrando que la solución es financieramente imbatible.*
>
> `[Señalar punto 4: Valor de Negocio]`  
> *Y cuarto, **De Datos a Valor**: logramos que la telemetría hable el idioma del negocio. El sistema no solo emite alertas técnicas: emite asientos de liquidación contable en dólares que habilitan el cobro automático de pólizas de seguro y protegen la salud de los consumidores.*
>
> *Revisemos finalmente el Punto 10: Next Steps."*

`[Transición: Pasar al Slide 11]`

---

## DIAPOSITIVA 11: 10. NEXT STEPS
**Tiempo estimado:** 01:00 minuto  
**Diapositiva en pantalla:** Línea de tiempo de Fases 1, 2 y 3 (Machine Learning, Cloud Run, Blockchain).

### 🎙️ Discurso Verbal:

> *"Culminamos los puntos oficiales con el **Punto 10: Next Steps**.*
>
> `[Señalar Fase 2: Q1 2027]`  
> *Nuestra visión estratégica proyecta una evolución en dos fases futuras:*
> * *En la **Fase 2 (Q1 2027)**, incorporaremos inteligencia predictiva utilizando **BigQuery ML**. Mediante modelos de series temporales con el algoritmo `ARIMA_PLUS`, el sistema ya no esperará a que la temperatura rompa el límite de 4°C: analizará la pendiente de subida térmica y **predecirá la rotura con 30 minutos de anticipación** en plena carretera. Asimismo, empaquetaremos la API en contenedores sobre **Google Cloud Run** e implementaremos CI/CD automatizado con GitHub Actions.*
>
> `[Señalar Fase 3: Q2 2027]`  
> * *En la **Fase 3 (Q2 2027)**, integraremos la Capa Gold con **contratos inteligentes en Blockchain**, permitiendo que las indemnizaciones de seguros o penalidades a transportistas infractores se debiten de forma automática e irrevocable ante una rotura térmica certificada. Y dotaremos a los choferes de una aplicación móvil PWA con alarmas acústicas en cabina.*
>
> *Pasemos ahora al cierre de la presentación."*

`[Transición: Pasar al Slide 12]`

---

## DIAPOSITIVA 12: DEFENSA TÉCNICA Y PREGUNTAS DEL JURADO (Q&A)
**Tiempo estimado:** 01:00 minuto  
**Diapositiva en pantalla:** Agradecimiento, metadatos del proyecto y banco de preguntas preparadas.

### 🎙️ Discurso Verbal de Cierre:

> *"Estimados miembros del jurado evaluador, profesor y colegas:*
>
> *Con esto concluyo formalmente la sustentación de los diez puntos requeridos para el proyecto **'Smart Cold Chain IoT'** en Google Cloud Platform.*
>
> *Hemos comprobado que la ingeniería de datos en la nube permite salvar cargamentos millonarios, proteger la salud pública y optimizar radicalmente los presupuestos de tecnología.*
>
> *El código fuente completo, los scripts de prueba, la documentación técnica y los modelos SQL se encuentran disponibles y versionados en nuestro repositorio abierto de GitHub.*
>
> `[Pausa de 2 segundos. Mirar a los ojos al presidente del jurado]`
>
> *Agradezco profundamente su tiempo, su atención y la rigurosidad de su evaluación, y quedo a su entera disposición para responder cualquier consulta técnica, arquitectural o financiera sobre el proyecto.*
>
> ***Muchas gracias.***"*

`[Fin del Discurso. Mantener postura erguida, manos juntas y esperar la primera pregunta del jurado]`

---

# BANCO MAESTRO DE RESPUESTAS ANTE PREGUNTAS DEL JURADO (Q&A)

### PREGUNTA 1: ¿Por qué usaron BigQuery Direct Ingestion en lugar de Cloud Dataflow (Apache Beam)?
* **Respuesta Maestra:**
  > *"Excelente pregunta, profesor. Descartamos Cloud Dataflow para la ingesta cruda a Bronze por dos razones: **costo operativo y simplicidad de mantenimiento**.*
  > *Dataflow es una herramienta extraordinaria cuando se requieren transformaciones complejas en vuelo antes de persistir, como ventanas de sesión deslizantes o joins de dos streams en memoria. Sin embargo, para ingestar telemetría tal como llega a una Capa Bronze, Dataflow exige aprovisionar trabajadores de Compute Engine activos 24/7, lo que genera un costo base de $60 a $120 dólares al mes.*
  > *BigQuery Direct Ingestion en Pub/Sub es una característica nativa, 100% Serverless, que escribe de forma atómica en BigQuery con latencia de 2.1 segundos a solo 5 centavos por gigabyte, sin requerir una sola línea de código middleware que mantener ni parches de infraestructura."*

---

### PREGUNTA 2: Si Cloud Pub/Sub ofrece entrega 'at-least-once' (al menos una vez), ¿cómo garantizan que no existan duplicados en los balances contables?
* **Respuesta Maestra:**
  > *"Esa es precisamente la razón por la cual implementamos el patrón Lakehouse Medallion y no conectamos la analítica directamente a la Capa Bronze.*
  > *Pub/Sub garantiza que ningún mensaje se pierda, pero ante una reconexión de red puede entregar un mensaje dos veces. Si calculáramos las pérdidas en Bronze, cobraríamos penalidades duplicadas. Por ello, la **Capa Silver** implementa idempotencia analítica mediante la función de ventana:*
  > ```sql
  > ROW_NUMBER() OVER(PARTITION BY device_id, timestamp ORDER BY timestamp DESC) = 1
  > ```
  > *Al filtrar únicamente la primera ocurrencia en Silver y generar una clave subrogada determinística con `TO_HEX(MD5(CONCAT(device_id, '-', timestamp)))`, garantizamos con rigor matemático que a la Capa Gold solo ingresen registros únicos, asegurando balances contables 100% auditables."*

---

### PREGUNTA 3: ¿Qué ocurriría con los costos y el rendimiento si la flota escala a 10,000 camiones?
* **Respuesta Maestra:**
  > *"La arquitectura fue diseñada específicamente para esa escala horizontal sin requerir reingeniería.*
  > *Con 10,000 camiones emitiendo cada 10 segundos, el volumen mensual alcanzaría 388 Gigabytes. En Pub/Sub, superada la cuota gratuita, pagaríamos aproximadamente $15.12 USD al mes; la ingesta directa en BigQuery costaría $19.40 USD; y el almacenamiento acumulado de 4.6 TB al año costaría unos $92 USD al mes. En total, **operaríamos 10,000 camiones por menos de $130 dólares mensuales en GCP**, mientras que mantener un clúster de Spark para ese volumen superaría fácilmente los $1,500 dólares.*
  > *En cuanto a rendimiento, gracias a que BigQuery particiona físicamente por fecha y clusteriza por dispositivo, una consulta que busque un camión específico tardará los mismos 600 milisegundos que tarda hoy, porque el motor solo lee el bloque del clúster correspondiente."*

---

### PREGUNTA 4: ¿Cómo se protege la nube si un atacante roba físicamente uno de los sensores del camión?
* **Respuesta Maestra:**
  > *"Implementamos de forma rigurosa el **Principio de Menor Privilegio (PoLP)** en Cloud IAM.*
  > *La Service Account que reside en el sensor (`iot-simulator-sa`) posee exclusivamente el rol `roles/pubsub.publisher` restringido al topic `iot-telemetry-topic`. Si un atacante extrae la clave criptográfica del microcontrolador, no puede leer telemetría de otros camiones, no puede listar tópicos, no tiene ningún permiso de lectura ni escritura en BigQuery y no puede modificar ningún recurso del proyecto.*
  > *Para producción comercial a gran escala, recomendamos además asociar cada dispositivo con certificados mTLS únicos o utilizar autenticación de carga de trabajo federada (Workload Identity Federation), permitiendo revocar un sensor individual en milisegundos desde la consola central."*

---

### PREGUNTA 5: ¿Por qué eligieron BigQuery y no Cloud Bigtable para almacenar la telemetría IoT?
* **Respuesta Maestra:**
  > *"Consideramos Cloud Bigtable porque es el estándar para escrituras clave-valor masivas con latencias sub-10ms. Sin embargo, para nuestro problema de negocio presentaba dos limitaciones insalvables:*
  > 1. *Bigtable no soporta SQL estándar ni joins relacionales nativos, lo que habría obligado a transferir los datos a otro motor para cruzarlos con las tablas de productos y choferes del ERP.*
  > 2. *Bigtable exige un costo mínimo aprovisionado de aproximadamente $450 USD mensuales por clúster de 1 nodo.*
  > *BigQuery nos proporcionó almacenamiento columnar serverless de costo marginal cero en pruebas, consultas SQL analíticas complejas, cruces dimensionales instantáneos y la capacidad nativa de aplicar Machine Learning con BigQuery ML sin mover los datos de sitio."*

---

### PREGUNTA 6: ¿Cómo se integraría esta arquitectura con herramientas de Business Intelligence como Looker Studio o Power BI?
* **Respuesta Maestra:**
  > *"La integración es totalmente directa gracias al modelado en estrella de la Capa Gold. Las herramientas como Looker Studio, Power BI o Tableau cuentan con conectores nativos de alta velocidad hacia BigQuery.*
  > *Al conectar el tablero con la tabla `gold_fact_incidentes` y sus dimensiones maestras, la herramienta ejecuta consultas SQL directas o aprovecha BigQuery BI Engine para cachear en memoria las consultas más frecuentes, entregando visualizaciones interactivas de mapas de calor térmico, mermas por transportista y cumplimiento de SLA con latencias inferiores a un segundo."*
