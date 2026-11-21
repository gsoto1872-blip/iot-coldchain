# GUION MAESTRO DE SUSTENTACIÓN ORAL (SPEECH)
## Defensa de Proyecto de Ingeniería: Smart Cold Chain IoT en Google Cloud Platform
### Pitch Deck, Discurso Palabra por Palabra y Manual de Oratoria ante el Jurado

---

### FICHA TÉCNICA DEL DISCURSO Y PARÁMETROS DE EXPOSICIÓN

* **Sustentante:** Guillermo Soto
* **Proyecto GCP Activo:** `myfirstproject-508413` | **Región:** `us-central1` (Iowa, EE. UU.)
* **Repositorio de Código:** [https://github.com/gsoto1872/iot-coldchain](https://github.com/gsoto1872/iot-coldchain)
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

### CRONOGRAMA MINUTO A MINUTO DE LA EXPOSICIÓN

```
====================================================================================================
TIEMPO TOTAL: 18 - 20 MINUTOS
----------------------------------------------------------------------------------------------------
[Min 00:00 - 01:30]  Slide 01: Portada, Presentación Personal y Gancho de Negocio
[Min 01:30 - 03:00]  Slide 02: 1. Resumen Ejecutivo - Alcance de la Implementación
[Min 03:00 - 04:30]  Slide 03: 2. Situación Actual - Diagnóstico As-Is vs To-Be
[Min 04:30 - 06:00]  Slide 04: 3. Criterios de Éxito en Formato KPI (Balanced Scorecard)
[Min 06:00 - 08:00]  Slide 05: 4. Productos Tecnológicos a Usar (Stack & Justificación)
[Min 08:00 - 09:30]  Slide 06: 5. Dependencias, Supuestos y Gestión de Riesgos
[Min 09:30 - 12:00]  Slide 07: 6. Arquitectura Final: Data Lakehouse Medallion
[Min 12:00 - 14:00]  Slide 08: 7. Calculadora de Consumo y TCO (Pricing Real de GCP)
[Min 14:00 - 17:00]  Slide 09: 8. Demostración Práctica End-to-End (Arnés en Vivo)
[Min 17:00 - 18:30]  Slide 10: 9. Conclusiones Técnicas, Operativas y Financieras
[Min 18:30 - 19:30]  Slide 11: 10. Next Steps - Hoja de Ruta Tecnológica 2027
[Min 19:30 - 20:30]  Slide 12: Cierre Protocolar y Apertura de Preguntas (Q&A)
====================================================================================================
```

---

# DISCURSO COMPLETO PALABRA POR PALABRA

---

## DIAPOSITIVA 01: PORTADA EJECUTIVA E IDENTIFICACIÓN DEL PROYECTO
**Tiempo estimado:** 01:30 minutos  
**Diapositiva en pantalla:** Portada con badges de Google Cloud, ID del proyecto y lema.

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
> *A lo largo de los próximos 18 minutos demostraré cómo logramos transformar lecturas de hardware ciego en **decisiones prescriptivas inmediatas con latencia inferior a 2 segundos**, liquidando de forma algorítmica las pérdidas monetarias en dólares y logrando una eficiencia de costos de infraestructura que reduce en más de un 99% el gasto tradicional. Los invito a comenzar revisando el alcance ejecutivo."*

`[Transición: Presionar tecla Flecha Derecha o Espacio para pasar al Slide 2]`

---

## DIAPOSITIVA 02: 1. RESUMEN EJECUTIVO - ALCANCE DE LA IMPLEMENTACIÓN
**Tiempo estimado:** 01:30 minutos  
**Diapositiva en pantalla:** Tarjetas de Reto Global, Alcance Desarrollado y Valor Entregado.

### 🎙️ Discurso Verbal:

> *"Iniciemos dimensionando la escala del problema.*
>
> `[Señalar la tarjeta izquierda: El Problema Global]`  
> *A nivel mundial se registran más de **35 mil millones de dólares anuales en mermas** por fallas en la cadena de frío. Pero el dato verdaderamente revelador es que **el 80% de estas catástrofes ocurren durante el transporte terrestre e intermodal**. Una vez que el camión frigorífico sale del centro de distribución, la mercadería entra en una auténtica 'caja negra' logística.*
>
> `[Pausa de 1 segundo]`
>
> `[Señalar la tarjeta central: Alcance Desarrollado]`  
> *Para erradicar esa caja negra, nuestro alcance contempló el diseño e implementación de un **Data Lakehouse Medallion** que une dos flujos de datos que históricamente vivían en silos aislados:*
> * *Por un lado, el **flujo streaming de IoT**, recibiendo lecturas continuas de temperatura, humedad relativa y nivel de batería cada 10 segundos.*
> * *Por otro lado, el **flujo batch del sistema transaccional ERP**, que contiene los lotes, las tolerancias térmicas del producto, su costo unitario y la asignación del chofer y vehículo.*
>
> `[Señalar la tarjeta derecha: El Valor Entregado]`  
> *Esta convergencia alimenta dos rutas: un **Hot Path** que en menos de 2 segundos detecta cualquier desvío térmico y envía una alarma a la cabina del camión para desviar la carga a una cámara de contingencia antes de que se descomponga; y un **Cold Path** en batch que consolida la información diaria, genera balances contables de la pérdida y expone estos datos a través de una API REST moderna para sistemas corporativos.*
>
> *Veamos a continuación cómo este enfoque revoluciona la situación actual del sector."*

`[Transición: Pasar al Slide 3]`

---

## DIAPOSITIVA 03: 2. SITUACIÓN ACTUAL (DIAGNÓSTICO AS-IS vs TO-BE)
**Tiempo estimado:** 01:30 minutos  
**Diapositiva en pantalla:** Diagrama de flujo comparativo y matriz As-Is vs To-Be.

### 🎙️ Discurso Verbal:

> *"Para entender el salto cuántico que representa este proyecto, debemos comparar la situación actual del mercado con la solución que hemos implementado.*
>
> `[Señalar el diagrama superior: Flujo As-Is]`  
> *Actualmente, más del 70% de las empresas de transporte refrigerado utilizan los llamados **dataloggers pasivos**: pequeños dispositivos USB que se colocan entre las cajas. El transportista conduce 15 o 20 horas a través de la carretera. Al llegar a la bodega de destino, el inspector de calidad abre el camión, retira el dispositivo USB, lo conecta a una laptop y descarga un PDF.*
>
> *¿Qué descubre en ese momento? Que hace 10 horas el compresor de frío falló y la mercadería estuvo a 15 grados centígrados. **Eso no es control de calidad; eso es una autopsia forense**. La carga se va directo a la basura, se pierden miles de dólares y comienzan meses de litigios judiciales entre el dueño de la carga y el transportista.*
>
> `[Pausa de 2 segundos. Modular la voz hacia un tono positivo y resolutivo]`
>
> `[Señalar el diagrama inferior: Flujo To-Be]`  
> *Con nuestro modelo **To-Be**, transformamos esa reacción tardía en un **control activo y proactivo en tiempo real**. Si el compresor falla en el kilómetro 80 de una autopista, en menos de **2 segundos** el chofer y la torre de control reciben la notificación del exceso térmico. El conductor se desvía de inmediato a un almacén frigorífico en el kilómetro 90, se trasvasa la mercadería y **se salva el 100% del cargamento**.*
>
> *Además, sustituimos los servidores dedicados por una arquitectura 100% Serverless, logrando un ahorro de costos de TI superior al 99%.*
>
> *Para comprobar que esto funciona con rigor de ingeniería, definimos un cuadro de mando integral con métricas concretas."*

`[Transición: Pasar al Slide 4]`

---

## DIAPOSITIVA 04: 3. CRITERIOS DE ÉXITO EN FORMATO KPI
**Tiempo estimado:** 01:30 minutos  
**Diapositiva en pantalla:** Tarjetas numéricas de KPIs (1.8s, 99.99%, 100%, 100%, 600ms, $0.00).

### 🎙️ Discurso Verbal:

> *"Para evaluar el desempeño del sistema de manera objetiva y cuantificable, establecimos seis Indicadores Clave de Rendimiento organizados bajo un Balanced Scorecard de datos.*
>
> `[Señalar la primera tarjeta: Latencia Hot Path]`  
> *El primer KPI, de naturaleza operacional, fue la **Latencia de Detección en el Hot Path**. Nos propusimos alertar en 3 segundos o menos. En los ensayos reales sobre Google Cloud obtuvimos una marca de **1.8 segundos** cronometrados desde la emisión física del sensor hasta la actualización de la vista analítica. KPI superado con creces.*
>
> `[Señalar la segunda tarjeta: Disponibilidad]`  
> *El segundo KPI, de resiliencia, exigía una disponibilidad mínima del 99.90% para la ingesta. Al sustentarnos sobre la infraestructura multi-zona de **Google Cloud Pub/Sub**, alcanzamos un **99.99%** respaldado contractualmente por el SLA de Google.*
>
> `[Señalar la tercera tarjeta: Deduplicación Silver]`  
> *El tercer KPI es crítico para la gobernanza: **100% de Deduplicación en la Capa Silver**. Los sensores móviles en carretera sufren cortes de señal celular y reenvían paquetes repetidos. Si procesáramos esos datos en crudo, duplicaríamos las multas contables. Mediante funciones analíticas de ventana con `ROW_NUMBER()`, garantizamos que no exista un solo registro duplicado en la capa limpia.*
>
> `[Señalar las tarjetas inferiores: Velocidad y Costos]`  
> *Finalmente, en rendimiento y finanzas: optimizamos el almacenamiento en BigQuery mediante **particionamiento diario y clustering por dispositivo**, logrando que las consultas analíticas respondan en apenas **600 milisegundos**, operando en nuestro laboratorio a un costo de **$0.00 dólares** gracias a la capa Always Free de GCP.*
>
> *Veamos a continuación el stack tecnológico que hizo posibles estos resultados."*

`[Transición: Pasar al Slide 5]`

---

## DIAPOSITIVA 05: 4. PRODUCTOS TECNOLÓGICOS A USAR (STACK & JUSTIFICACIÓN)
**Tiempo estimado:** 02:00 minutos  
**Diapositiva en pantalla:** Diagrama Mermaid de componentes y tabla de alternativas descartadas.

### 🎙️ Discurso Verbal:

> *"La elección de tecnologías en este proyecto obedeció a un principio estricto de ingeniería: **máxima resiliencia con el menor costo operativo y de mantenimiento posible**.*
>
> `[Señalar la capa de Ingesta: Cloud Pub/Sub]`  
> *Para la ingesta elegimos **Google Cloud Pub/Sub**. ¿Por qué descartamos Apache Kafka? Porque montar un clúster de Kafka con Zookeeper o KRaft exige pagar instancias virtuales encendidas las 24 horas del día, lo que generaría un costo fijo de más de 150 dólares al mes en servidores ociosos. Pub/Sub escala de 0 a millones de eventos de forma transparente y nos ofrece 10 GB mensuales gratuitos.*
>
> `[Señalar BigQuery Direct Ingestion]`  
> *Pero la innovación clave en la ingesta radica en **BigQuery Direct Ingestion**. Tradicionalmente, se solía colocar un pipeline de Cloud Dataflow entre Pub/Sub y BigQuery. Sin embargo, para ingesta directa de telemetría a la Capa Bronze, Dataflow requería pagar workers de cómputo continuos. Con Direct Ingestion, Pub/Sub escribe de forma atómica y directa en BigQuery en 2 segundos, sin una sola línea de código middleware y a solo 5 centavos por gigabyte.*
>
> `[Señalar BigQuery]`  
> *Para el almacenamiento elegimos **Google BigQuery** frente a Cloud SQL. Las bases de datos relacionales tradicionales sufren bloqueos de registros cuando miles de sensores escriben concurrentemente. BigQuery utiliza el formato columnar Capacitor, permitiendo ingestas masivas y análisis forense sobre petabytes con cero contención de bloqueos.*
>
> `[Señalar Cloud IAM y FastAPI]`  
> *En seguridad aplicamos el **Principio de Menor Privilegio** a través de Cloud IAM: la Service Account del sensor solo tiene el rol de publicador en Pub/Sub, impidiendo cualquier acceso a la base de datos. Y para exponer los servicios implementamos un microservicio con **FastAPI en Python 3.12**, que aprovecha el tipado estricto de Pydantic y soporte asíncrono nativo.*
>
> *Examinemos ahora cómo delimitamos las fronteras del proyecto y gestionamos los riesgos."*

`[Transición: Pasar al Slide 6]`

---

## DIAPOSITIVA 06: 5. DEPENDENCIAS, SUPUESTOS Y GESTIÓN DE RIESGOS
**Tiempo estimado:** 01:30 minutos  
**Diapositiva en pantalla:** Matriz de dependencias, supuestos y elementos fuera de scope.

### 🎙️ Discurso Verbal:

> *"Ningún proyecto de ingeniería está completo si no define con rigor sus dependencias y cómo mitiga los riesgos inherentes del entorno real.*
>
> `[Señalar la primera fila: Conectividad Móvil]`  
> *El principal riesgo en aplicaciones telemáticas es la **pérdida de cobertura celular en carretera**. Si el camión entra en un túnel o en una zona montañosa durante dos horas, ¿qué ocurre? Diseñamos la solución para ser completamente tolerante a caídas de red: el gateway del sensor cuenta con un buffer FIFO en memoria local. Cuando el vehículo recupera cobertura, envía una ráfaga acumulada de 2,000 lecturas. Pub/Sub absorbe el pico elásticamente y nuestro pipeline SQL en Silver se encarga de reordenar cronológicamente los datos sin pérdida de eventos.*
>
> `[Señalar la segunda fila: Colocalización]`  
> *Otra dependencia crítica es la latencia y los costos de transferencia de red. Mitigamos esto mediante la **colocalización estricta**: todos los recursos (Pub/Sub, BigQuery y Cloud Storage) residen en la misma región: `us-central1` (Iowa). Gracias a esto, el costo por transferencia interna de datos es exactamente **$0.00 USD**.*
>
> `[Señalar los Supuestos y Fuera de Scope]`  
> *En los supuestos, establecimos un **Data Contract JSON estricto**: si un sensor defectuoso envía lecturas físicamente imposibles, como 500 grados centígrados, la Capa Silver las aísla en una tabla de cuarentena. Asimismo, congelamos el costo unitario del producto al momento del despacho para evitar que variaciones de mercado distorsionen las pérdidas contables.*
>
> *Y dejamos conscientemente fuera de alcance la soldadura y calibración física del hardware del sensor para enfocar el 100% de nuestro esfuerzo en la arquitectura analítica en la nube.*
>
> *Pasemos ahora a revisar el corazón del sistema: la Arquitectura Final Medallion."*

`[Transición: Pasar al Slide 7]`

---

## DIAPOSITIVA 07: 6. ARQUITECTURA FINAL: DATA LAKEHOUSE MEDALLION
**Tiempo estimado:** 02:30 minutos  
**Diapositiva en pantalla:** Diagrama completo de las 4 etapas del Lakehouse y capas Bronze, Silver y Gold.

### 🎙️ Discurso Verbal:

> *"Esta lámina representa el núcleo técnico de nuestra sustentación: la arquitectura definitiva basada en el patrón **Data Lakehouse Medallion**.*
>
> `[Señalar Etapa 1 y 2: Fuentes e Ingesta]`  
> *El viaje del dato comienza a la izquierda con los 100 sensores transmitiendo cada 10 segundos hacia el topic de Pub/Sub `iot-telemetry-topic`, mientras los catálogos maestros del ERP residen en Cloud Storage. A través de la suscripción `iot-telemetry-bq-sub`, los eventos entran directamente a BigQuery sin intermediarios.*
>
> `[Señalar Etapa 3: Capa Bronze]`  
> *Los datos ingresan primero a la **Capa Bronze**, en la tabla `bronze_telemetria`. Esta capa representa la verdad histórica pura, cruda e inalterable. Para maximizar el rendimiento analítico y reducir costos, la tabla está **particionada por fecha (`DATE(timestamp)`) y clusterizada por el identificador del sensor (`device_id`)**.*
>
> `[Pausa de 1 segundo]`
>
> `[Señalar Capa Silver]`  
> *A continuación, el pipeline batch orquestado en Python ejecuta la transformación hacia la **Capa Silver**, en la tabla `silver_telemetria_clean`. En este punto realizamos tres operaciones críticas de calidad de datos:*
> 1. *Descartamos cualquier lectura con ruido electromagnético fuera del rango de -50°C a +60°C.*
> 2. *Aplicamos la función de ventana `ROW_NUMBER()` para eliminar registros duplicados producto de retransmisiones celulares.*
> 3. *Generamos una **clave primaria subrogada determinística** utilizando un hash MD5 a partir del sensor y la marca de tiempo, garantizando la idempotencia del proceso.*
>
> `[Señalar Capa Gold]`  
> *Finalmente, en la **Capa Gold**, modelamos la información en un **esquema en estrella (Star Schema)**. Aquí cruzamos la telemetría limpia con las dimensiones del ERP (`dim_productos` y `dim_asignacion_sensores`). Esto produce dos tablas de hechos:*
> * *La tabla `gold_fact_incidentes`, donde cada sobrecalentamiento se clasifica como Moderado, Alto o Crítico, calculando de manera algorítmica la **pérdida financiera en dólares** multiplicando el volumen del lote por el costo unitario y el castigo térmico.*
> * *Y la tabla agregada `gold_fact_resumen_diario`, que consolida métricas diarias de temperatura y monitorea el desgaste de la batería de cada dispositivo.*
>
> `[Señalar Hot Path y API]`  
> *En paralelo, el **Hot Path** consulta la vista `v_alertas_cadena_frio` en menos de 2 segundos, alimentando a la REST API en FastAPI para notificaciones operativas inmediatas.*
>
> *Veamos ahora el impacto financiero de esta arquitectura en la Calculadora de Consumo."*

`[Transición: Pasar al Slide 8]`

---

## DIAPOSITIVA 08: 7. CALCULADORA DE CONSUMO Y TCO (PRICING REAL DE GCP)
**Tiempo estimado:** 02:00 minutos  
**Diapositiva en pantalla:** Ecuaciones de dimensionamiento, tabla de desglose por SKU y comparativa de TCO.

### 🎙️ Discurso Verbal:

> *"Uno de los mayores diferenciadores de nuestra propuesta radica en la solvencia económica del diseño. Realizamos un dimensionamiento riguroso basado en las tarifas públicas oficiales de Google Cloud para la región `us-central1`.*
>
> `[Señalar las fórmulas en la parte superior]`  
> *Si consideramos una flota mediana de **100 camiones refrigerados** emitiendo una lectura cada 10 segundos durante las 24 horas del día por 30 días, tenemos exactamente:*  
> *100 camiones por 8,640 lecturas al día por 30 días = **25 millones 920 mil mensajes mensuales**.*  
> *A un peso de 150 bytes por payload JSON, esto equivale a **3.88 Gigabytes al mes**.*
>
> `[Señalar la tabla de costos por servicio]`  
> *Analicemos el desglose línea por línea:*
> * *En **Cloud Pub/Sub**: como transferimos 3.88 GB y Google otorga **10 GB gratis al mes**, el costo es **$0.00 USD**.*
> * *En **BigQuery Direct Ingestion**: la tarifa es de 5 centavos por gigabyte. Por 3.88 GB pagamos apenas **$0.19 USD al mes**.*
> * *En **Almacenamiento de BigQuery**: tras un año completo acumulamos 46.5 GB. Con los primeros 10 GB gratuitos, el promedio mensual a $0.02/GB es de **$0.73 USD**.*
> * *En **Consultas SQL de BigQuery**: gracias al particionado diario, escaneamos unos 120 GB al mes. Como Google otorga **1 Terabyte gratuito mensual**, el costo es **$0.00 USD**.*
> * *Y en **Cloud Storage y Red Interna**: el costo es **$0.00 USD** por Free Tier y tráfico colocalizado.*
>
> `[Pausa de 2 segundos. Enfatizar con la voz]`
>
> `[Señalar el Total Anual y la Comparativa TCO]`  
> *Sumando todo, la facturación mensual proyectada es de tan solo **$0.92 dólares al mes**, lo que equivale a **$11.04 dólares al año**.*
>
> *Comparemos esto con la industria tradicional: si hubiésemos contratado un clúster Dataproc de Spark con dos máquinas `n1-standard-2` encendidas 24/7, la empresa pagaría **$1,152 dólares al año**. Nuestra arquitectura Serverless genera un ahorro neto de **$1,140 dólares anuales**, lo que representa una **reducción del 99.04% en el Costo Total de Propiedad (TCO)**.*
>
> *A continuación, demostraremos esto en vivo en nuestra prueba de extremo a extremo."*

`[Transición: Pasar al Slide 9]`

---

## DIAPOSITIVA 09: 8. DEMO END-TO-END DE IMPLEMENTACIÓN (CASO REAL EN VIVO)
**Tiempo estimado:** 03:00 minutos  
**Diapositiva en pantalla:** Diagrama de secuencia y trace de terminal de la prueba real.  
*(Opcional: Si el jurado solicita la terminal interactiva, pasar a la ventana de Cloud Shell y ejecutar `python demo/demo_e2e.py`)*

### 🎙️ Discurso Verbal:

> *"Para demostrar la factibilidad técnica y la robustez del código, desarrollamos un arnés automatizado de validación end-to-end en el script `demo/demo_e2e.py`.*
>
> `[Señalar el diagrama de secuencia en pantalla]`  
> *El caso de uso real que emulamos representa una contingencia logística en plena carretera:*
>
> * **Paso 1:** El dispositivo `SENSOR-02` instalado en el vehículo `Camion-Reparto-04`, conducido por Juan Perez, transporta un lote de **Carne Fresca** (500 kg valorizados a $5.00/kg). El límite térmico máximo tolerado es de **4.0°C**. El compresor sufre una falla mecánica y el sensor registra **13.5°C**.
> * **Paso 2:** El evento se empaqueta en JSON, se firma con la Service Account y se publica en Cloud Pub/Sub, recibiendo el identificador de confirmación `Message ID: 23550907518145894` en 120 milisegundos.
> * **Paso 3:** La suscripción BigQuery Direct Ingestion persiste el dato crudo en la tabla `bronze_telemetria` en **2.1 segundos**, sin servidores intermediarios.
> * **Paso 4:** En el Hot Path, la vista SQL `v_alertas_cadena_frio` detecta de inmediato el **exceso térmico de +9.5°C** y levanta la bandera roja en la torre de control.
> * **Paso 5:** Se dispara el pipeline batch `batch_pipeline.py`. El proceso aplica deduplicación en la Capa Silver y cruza el incidente en la Capa Gold. Al detectar una desviación superior a 5°C, clasifica la severidad como **CRÍTICA** y calcula la merma contable: 500 kg con castigo del 47.5% arroja una **pérdida financiera de $1,187.50 USD**.
> * **Paso 6:** Invocamos el endpoint `/api/v1/incidents?severity=CRÍTICA` de nuestra API REST en FastAPI, la cual responde `HTTP 200 OK` entregando el contrato JSON auditado.
> * **Paso 7:** El sistema emite la decisión prescriptiva: ordena el desvío inmediato del conductor a la cámara de frío más cercana y coloca el lote en cuarentena automática en el sistema WMS para evitar que llegue a la mesa del consumidor.
>
> `[Pausa de 2 segundos]`
> *El flujo funcionó de extremo a extremo, cerrando el ciclo entre el sensor de campo y el balance financiero corporativo.*
>
> *Sinteticemos ahora las conclusiones principales del proyecto."*

`[Transición: Pasar al Slide 10]`

---

## DIAPOSITIVA 10: 9. CONCLUSIONES DE LA IMPLEMENTACIÓN
**Tiempo estimado:** 01:30 minutos  
**Diapositiva en pantalla:** Cuatro pilares de conclusiones (Factibilidad, Gobernanza, Finanzas, Negocio).

### 🎙️ Discurso Verbal:

> *"Como balance general de este trabajo de ingeniería, podemos resumir nuestras conclusiones en cuatro dimensiones estratégicas:*
>
> `[Señalar punto 1: Factibilidad Técnica]`  
> *Primero, **Factibilidad Técnica Comprobada**: demostramos que una arquitectura moderna de datos no requiere la complejidad ni el costo de gestionar clústeres dedicados. La unión nativa de Pub/Sub Direct Ingestion y BigQuery ofrece escalabilidad masiva con cero fricción de mantenimiento.*
>
> `[Señalar punto 2: Gobernanza ALCOA+]`  
> *Segundo, **Gobernanza y Confiabilidad Matemática**: la inmutabilidad de la Capa Bronze combinada con la deduplicación analítica en la Capa Silver asegura que ninguna fluctuación de red celular altere los registros contables, cumpliendo con los estándares de integridad de datos exigidos por la FDA y la industria farmacéutica.*
>
> `[Señalar punto 3: Disrupción en TCO]`  
> *Tercero, **Eficiencia Económica Radical**: reducir el costo anual de infraestructura de **$1,152 dólares a tan solo $11 dólares** mediante arquitectura Serverless es un resultado contundente que demuestra que la excelencia en ingeniería se traduce en rentabilidad para la empresa.*
>
> `[Señalar punto 4: Valor de Negocio]`  
> *Y cuarto, **De Datos a Valor**: logramos que la telemetría hable el lenguaje de la alta dirección. El sistema no solo emite advertencias técnicas: emite asientos de liquidación contable en dólares que habilitan el cobro automático de pólizas de seguro y previenen daños a la salud pública.*
>
> *Veamos finalmente la hoja de ruta que proyectamos para este sistema."*

`[Transición: Pasar al Slide 11]`

---

## DIAPOSITIVA 11: 10. NEXT STEPS (HOJA DE RUTA ESTRATÉGICA 2027)
**Tiempo estimado:** 01:00 minuto  
**Diapositiva en pantalla:** Línea de tiempo de Fases 1, 2 y 3 (Machine Learning, Cloud Run, Blockchain).

### 🎙️ Discurso Verbal:

> *"Nuestra visión de este proyecto va más allá de esta entrega académica; hemos trazado una hoja de ruta tecnológica clara y escalable.*
>
> `[Señalar Fase 2: Q1 2027]`  
> *En la **Fase 2**, programada para el primer trimestre de 2027, implementaremos inteligencia predictiva utilizando **BigQuery ML**. Mediante modelos de series temporales con el algoritmo `ARIMA_PLUS`, el sistema ya no esperará a que la temperatura rompa el límite de 4°C: analizará la velocidad de incremento térmico y **predecirá la anomalía con 30 minutos de anticipación** mientras el vehículo aún se encuentra en ruta.*
> *Asimismo, desplegaremos la API REST en contenedores sobre **Google Cloud Run** para contar con autoescalado serverless de 0 a 1,000 instancias concurrentes e implementaremos CI/CD automatizado con GitHub Actions.*
>
> `[Señalar Fase 3: Q2 2027]`  
> *En la **Fase 3**, para el segundo trimestre de 2027, integraremos los incidentes de la Capa Gold con **contratos inteligentes en Blockchain**, permitiendo que las indemnizaciones de aseguradoras o las penalidades a transportistas infractores se debiten de forma automática e irrevocable. Y dotaremos a los conductores de una aplicación móvil PWA con alarmas acústicas en cabina.*
>
> *Pasemos ahora al cierre de la presentación."*

`[Transición: Pasar al Slide 12]`

---

## DIAPOSITIVA 12: DEFENSA TÉCNICA Y CIERRE PROTOCOLAR
**Tiempo estimado:** 01:00 minuto  
**Diapositiva en pantalla:** Agradecimiento, metadatos del proyecto y banco de preguntas preparadas.

### 🎙️ Discurso Verbal de Cierre:

> *"Estimados miembros del jurado evaluador, profesor y colegas:*
>
> *Con esto concluyo formalmente la sustentación de la arquitectura **Smart Cold Chain IoT** en Google Cloud Platform.*
>
> *Hemos comprobado que la ingeniería de datos en la nube permite salvar cargamentos millonarios, proteger la salud de las personas y optimizar radicalmente los presupuestos de tecnología.*
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

# GUÍA MAESTRA DE RESPUESTAS ANTE PREGUNTAS DEL JURADO (Q&A)

### Técnica de Comunicación Recomendada:
Cuando un profesor o jurado te haga una pregunta:
1. **Escucha activamente** sin interrumpir hasta que termine de hablar.
2. **Agradece y valida la pregunta:** *"Muchas gracias por la pregunta, profesor [Nombre]..."* o *"Es una pregunta fundamental para la gobernanza del sistema..."*.
3. **Responde primero con la conclusión técnica directa (10 segundos)** y luego sustenta con la evidencia real de tu implementación en GCP.

---

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

---

### RESUMEN DE CONSEJOS ANTE IMPREVISTOS DURANTE LA SUSTENTACIÓN

* **Si la conexión a Internet falla durante la Demo:**  
  *Mantén la calma y di con aplomo:*  
  *"Como medida preventiva de contingencia de ingeniería, hemos documentado la traza completa de ejecución con sus identificadores de mensaje de Pub/Sub y respuestas HTTP en la diapositiva 9 y en nuestro informe técnico. Podemos observar aquí los mismos pasos que corre el script en vivo."*
* **Si el jurado te interrumpe a mitad de una lámina:**  
  *Detén tu discurso, escucha con atención, asiente con la cabeza y responde puntualmente lo que preguntan. Luego retoma fluidamente:*  
  *"Retomando el flujo de la arquitectura..."*
* **Si te preguntan algo que no contemplaste:**  
  *No inventes. Di con madurez profesional:*  
  *"Ese es un punto muy valioso que no formó parte del alcance inicial de esta entrega, pero representa una excelente oportunidad de mejora que incorporaremos en la Fase 2 de nuestra hoja de ruta tecnológica."*
