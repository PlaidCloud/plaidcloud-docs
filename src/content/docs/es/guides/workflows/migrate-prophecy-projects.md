---
title: Migrar proyectos de Prophecy
description: Convierta la exportación de un proyecto de Prophecy en flujos de trabajo de PlaidCloud desde la aplicación Analyze, la API REST o un agente de IA conectado por MCP, vincule sus conjuntos de datos y conexiones, y lea el informe de conversión.
sidebar:
  order: 31.5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-prophecy-projects.md
---

PlaidCloud es un reemplazo directo de Prophecy. Cada gem de Prophecy se convierte en pasos nativos de flujo de trabajo de PlaidCloud que realizan el trabajo del gem: el convertidor crea un flujo de trabajo por cada pipeline de Spark y uno para el proyecto SQL, asigna cada gem a un paso de flujo de trabajo, una variable de proyecto o un objeto del lienzo, conserva el grafo original y devuelve un informe de conversión. Los pocos comportamientos que un flujo de trabajo convertido no reproduce por sí solo se enumeran en [Casos límite](#casos-límite).

La conversión solo lee la exportación que usted indique. Nunca se conecta al sistema del que lee o en el que escribe un conjunto de datos de Prophecy, y nunca ejecuta el código del proyecto.

La conversión es un paso único. Si convierte el mismo proyecto de nuevo, se crean nuevos flujos de trabajo y tablas, y las ediciones que haya hecho en PlaidCloud nunca se combinan con una exportación posterior.

## Qué crea PlaidCloud

- Cada gem de Prophecy se convierte en el paso de flujo de trabajo equivalente, conservando las relaciones ascendentes y descendentes.
- Los parámetros de Prophecy se convierten en variables de proyecto, y las referencias a ellos dentro de la configuración de los gems se reescriben con la sintaxis de variables de PlaidCloud. Puede reemplazar los valores de los parámetros en la conversión.
- Cada conjunto de datos que lee un gem se convierte en un paso de importación, o lee una tabla o un documento existente, según cómo lo vincule.
- Cada trabajo de Prophecy o programación de pipeline SQL se convierte en un [evento programado](/es/administration/scheduled-events/) en el flujo de trabajo convertido, habilitado cuando lo está en Prophecy. Consulte [Programaciones](#servicios-y-control).
- Los scripts, las instrucciones SQL, las macros y demás código del proyecto llegan dentro de pasos que contienen el código. Consulte [Código del proyecto en los pasos](#código-del-proyecto-en-los-pasos).
- Un gem personalizado, incluido un gem de Gem Builder, ejecuta en un paso de Python el código que la exportación contiene para él. Consulte [Código del proyecto en los pasos](#código-del-proyecto-en-los-pasos).
- Un gem Pivot con una condición HAVING o una columna de todos los valores se convierte, igual que los tipos de ordenación y de Deduplicate que ofrece Prophecy.
- Las expresiones se convierten suponiendo el comportamiento de Spark SQL para el tratamiento de valores nulos, la división entera y las conversiones de tipo implícitas. Compruebe los resultados donde esos comportamientos difieran en su motor de PlaidCloud.

## Antes de empezar

1. Exporte el proyecto desde Prophecy como un archivo `.zip`, o exporte un único pipeline, modelo o subgrafo como un archivo `.json`.
2. Cargue el archivo en una [cuenta de documentos](/es/guides/documents/adding-accounts/) que usted pueda leer.
3. Elija el proyecto de PlaidCloud que debe recibir los flujos de trabajo. Necesita acceso de escritura a él.
4. Decida desde dónde se leen los archivos de los conjuntos de datos sin vincular. Elija una cuenta de documentos y una carpeta base.

## Convertir el proyecto

Convierta desde la aplicación Analyze, la API REST o el catálogo de herramientas de MCP. Las tres opciones usan los mismos campos.

### Aplicación Analyze

1. Abra **Analyze** y elija **Tools → Importar proyecto de Prophecy**.
2. Elija el **Proyecto de destino**, el **Proyecto de Prophecy (.zip o .json)** que cargó en una cuenta de documentos y la **Ubicación de los archivos de origen**, es decir, la cuenta de documentos y la carpeta base desde las que se leen los archivos de los conjuntos de datos sin vincular.
3. En **Nombres de objetos y opciones**, si lo desea, defina prefijos para flujos de trabajo, pasos y tablas, elija el **Tipo de flujo de trabajo** y decida si desea **Importar los componentes sin convertir como marcadores de posición de paso directo**.
4. En **Vinculaciones de orígenes y parámetros**, si lo desea, vincule un conjunto de datos a una tabla existente introduciendo el nombre del conjunto de datos y el ID de la tabla, y reemplace los parámetros de Prophecy por nombre. Para vincular conexiones, use la API REST o la herramienta de MCP. Consulte [Vincular conexiones](#vincular-conexiones).
5. Seleccione **Importar**.

La ventana muestra el progreso mientras lee el proyecto, analiza los pipelines, los asigna a operaciones de PlaidCloud y crea los flujos de trabajo, las tablas y los pasos. Al terminar, la ventana muestra el informe de conversión: recuento de pasos por nivel de confianza, advertencias, **Conversiones parciales**, **Marcadores de posición sin convertir**, **Componentes omitidos** y los **Archivos de origen que se deben cargar**.

### Campos

La API REST y la herramienta de MCP usan estos campos.

| Campo | Obligatorio | Qué hace |
| --- | --- | --- |
| `source_account_id` | Sí | Cuenta de documentos que contiene la exportación de Prophecy. |
| `source_file_path` | Sí | Ruta, dentro de esa cuenta, del `.zip` del proyecto o de un archivo `.json` de un pipeline, modelo o subgrafo. |
| `project_id` | Sí | Proyecto en el que se crean los flujos de trabajo. |
| `document_account_id` | Sí | Cuenta de documentos de la que leen los conjuntos de datos sin vincular. |
| `document_account_path` | Sí | Carpeta base de esa cuenta para los conjuntos de datos sin vincular. Un valor vacío o `/` es la raíz de la cuenta, y se omite una `/` inicial. Se rechazan las rutas con `..` o segmentos que empiezan por punto, llaves, letra de unidad o esquema de URL, o caracteres de control. |
| `workflow_prefix` | No | Prefijo que se agrega a los nombres de los flujos de trabajo. |
| `step_prefix` | No | Prefijo que se agrega a los nombres de los pasos. |
| `table_prefix` | No | Prefijo que se agrega a los nombres de las tablas. De forma predeterminada es el nombre del propio flujo de trabajo. Un prefijo que reutilizaría el nombre de una tabla existente se rechaza antes de crear nada. El prefijo utilizado se devuelve en el informe de conversión. |
| `workflow_type` | No | `advanced` (predeterminado) coloca el grafo en el lienzo DAG. `standard` genera una lista de pasos en serie. |
| `source_bindings` | No | Vincula conjuntos de datos y operaciones a datos existentes. Consulte [Vincular orígenes](#vincular-orígenes). |
| `connection_bindings` | No | Vincula las bases de datos, los almacenes de archivos, las API REST y el correo electrónico a los que accede un proyecto con conexiones de PlaidCloud y cuentas de documentos. Consulte [Vincular conexiones](#vincular-conexiones). |
| `parameters` | No | Reemplaza los parámetros de Prophecy. Consulte [Parámetros](#parámetros). |
| `allow_unconverted_placeholders` | No | Controla lo que hace un marcador de posición en el momento de la ejecución. Consulte [Marcadores de posición para gems sin convertir](#marcadores-de-posición-para-gems-sin-convertir). |

### REST

Envíe los campos como cuerpo JSON a:

```text
POST /rest/v1/analyze/prophecy/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/prophecy/customer-360.zip",
  "project_id": "<project id>",
  "document_account_id": "<document account id>",
  "document_account_path": "/prophecy-inputs"
}
```

Necesita el rol `analyze.workflow.write`.

### MCP

Un agente de IA conectado por MCP llama a la herramienta `prophecy_convert` con los mismos campos. Consulte [Agentes de IA (MCP)](/es/integrations/ai-coding-agents/) para conectar un agente. La herramienta modifica su proyecto, así que revise la llamada antes de aprobarla.

## Vincular orígenes

Una exportación de Prophecy describe de dónde proceden sus datos, pero no contiene datos ni credenciales. Use `source_bindings` para conectar cada conjunto de datos con datos que ya tenga en PlaidCloud. La clave es el nombre del conjunto de datos tal como aparece en el informe de conversión. El valor es uno de estos:

- Un ID `analyzetable_` de una tabla del proyecto de destino. El flujo de trabajo convertido lee esa tabla directamente.
- Un objeto con `account`, `path` y, opcionalmente, `sheet`, para leer un archivo de una cuenta de documentos.

```json
"source_bindings": {
  "customers": "analyzetable_1234",
  "budget": { "account": "<document account id>", "path": "/finance/budget.xlsx", "sheet": "FY27" }
}
```

Se rechaza una vinculación que usted no pueda leer. Una clave que no coincide con ningún conjunto de datos se notifica como advertencia. La ventana de Analyze vincula conjuntos de datos con tablas; use la API REST o la herramienta de MCP para vincular un conjunto de datos con un archivo de documento.

### Conjuntos de datos sin vincular

Un conjunto de datos sin vinculación se convierte en un paso de importación que aún no tiene datos, y el informe de conversión incluye una advertencia para él. El paso lee desde:

```text
<document_account_path>/prophecy/<workflow id>/<dataset name>.csv
```

Cargue el archivo en esa ruta y ejecute el flujo de trabajo. Hasta que el archivo esté allí, el paso de importación termina con una advertencia y crea una tabla vacía, y el flujo de trabajo continúa. El informe enumera cada ruta en **Archivos de origen que se deben cargar**.

### Vincular operaciones de tablas y archivos

Los gems que modifican tablas o archivos, como Table Operations (update, delete, drop) y File Operation (copy), actúan solo sobre los datos que creó la conversión. Para que uno trabaje con datos que ya existen, vincúlelo con una clave con el formato `operation:<pipeline>/<id>`, donde `<pipeline>` es el nombre del pipeline y `<id>` es el ID del gem. El informe de conversión indica la clave de cada uno de esos gems.

```json
"source_bindings": {
  "operation:daily_load/Operation_1": "analyzetable_5678"
}
```

Una operación destructiva sobre tablas o archivos se ejecuta solo cuando usted la vincula. Sin vinculación, un gem Table Operations trabaja con una tabla escrita por otro gem del mismo proyecto y, en caso contrario, se convierte en un marcador de posición que indica su clave. Un gem File Operation copia desde su propia carpeta de almacenamiento temporal. No se modifica nada fuera de las tablas y carpetas propias de la conversión a menos que usted lo vincule.

## Vincular conexiones

Un proyecto de Prophecy accede a bases de datos, almacenes de archivos, API REST y servidores de correo mediante conexiones. La exportación contiene los nombres de las conexiones pero no las credenciales, así que use `connection_bindings` para apuntar cada una a una conexión de PlaidCloud o a una cuenta de documentos que ya tenga. El informe de conversión enumera cada clave en sus vinculaciones.

```json
"connection_bindings": {
  "connection:warehouse_pg": "<connection id>",
  "connection:landing_s3": "<document account id>",
  "operation:daily_load/Email_1": "<connection id>"
}
```

Una clave es una de estas:

| Clave | Vincula | Valor |
| --- | --- | --- |
| `connection:<name>` | La conexión de Prophecy que nombra un gem o un conjunto de datos de base de datos. Una vinculación sirve para todos los gems de esa conexión. Un gem que no nombra ninguna conexión usa `connection:<pipeline>/<gem id>`, y un conjunto de datos de base de datos usa `connection:<dataset name>`. | Un ID de conexión de PlaidCloud: una conexión de base de datos (incluidas BigQuery y SAP HANA), una conexión de MongoDB o Apache Kafka, una conexión de Salesforce para lecturas y escrituras de Salesforce, una conexión de Tableau para un gem de Tableau, una conexión REST para Azure Cosmos DB, Pinecone, Power BI y las escrituras de Smartsheet y Slack, o una conexión basada en Singer para las lecturas de Smartsheet, Slack e Iceberg. Un ID de cuenta de documentos para un gem File Storage o Directory. |
| `operation:<pipeline>/<gem id>` | Un gem REST que envía algo distinto de GET, HEAD u OPTIONS, y todos los gems Email. | Un ID de conexión. Para REST, una conexión REST que contenga la credencial. |

La vinculación es su consentimiento para los gems que modifican elementos fuera de la conversión:

- Una solicitud REST que puede cambiar lo que contiene la API, y un correo electrónico que llega a personas reales, se convierten en pasos operativos solo cuando usted vincula su clave `operation:`. Sin vincular, el gem es un marcador de posición que indica la clave.
- Una cuenta de documentos vinculada a un gem File Storage o Directory permite que los pasos de ese gem escriban, eliminen o muevan archivos de esa cuenta.
- Una solicitud GET, HEAD u OPTIONS se envía tal como la envía el gem. Sin vincular, no tiene credencial hasta que usted seleccione una conexión REST en el paso convertido.

Un conjunto de datos de base de datos o un gem External Table sin vinculación se convierte en un paso que indica su clave y espera a que usted seleccione una conexión, y el informe incluye una advertencia. Vuelva a convertir con la clave vinculada, o seleccione la conexión en el paso. Se rechaza una vinculación cuyo ID sea del tipo de almacén incorrecto para sus gems, o que usted no pueda usar. Una clave que no coincide con nada se notifica como advertencia.

## Parámetros

`parameters` reemplaza los parámetros de Prophecy en la conversión:

```json
"parameters": {
  "instance": "prod",
  "values": { "run_date": "2026-10-01", "region": "EMEA" },
  "pipelines": {
    "daily_load": { "instance": "prod", "values": { "region": "APAC" } }
  }
}
```

`instance` nombra una instancia de configuración. `values` son texto, números o valores booleanos. La entrada de un pipeline reemplaza los valores de todo el proyecto para ese pipeline. El informe enumera los parámetros utilizados y los que se renombraron para ajustarse a los nombres de variables de PlaidCloud.

## Leer el informe de conversión

La respuesta contiene el informe de conversión. Léalo antes de ejecutar los flujos de trabajo.

| Sección | Qué le indica |
| --- | --- |
| Resumen | Cuántos pasos se convirtieron con confianza alta, media o baja, y cuántos no se convirtieron. |
| Advertencias | Todo lo que el convertidor supuso, aproximó u omitió, incluidos los conjuntos de datos sin vincular y las claves de vinculación que no coincidieron con nada. |
| Conversiones parciales | Pasos que se convierten pero difieren del gem en algún modo u opción. Cada uno incluye una nota sobre qué comprobar. |
| Marcadores de posición sin convertir | Gems sin equivalente en PlaidCloud, con el motivo. |
| Componentes omitidos | Gems que no realizan ningún trabajo propio, como los marcadores de límite del control de flujo, y el paso que absorbió cada uno. |
| Archivos de origen que se deben cargar | La ruta de documento de la que lee cada conjunto de datos sin vincular. |
| Flujos de trabajo | El flujo de trabajo creado para cada pipeline, en orden de ejecución. Se marca un pipeline que el convertidor rechazó. |

El informe también indica el prefijo de tabla utilizado y los parámetros aplicados. Un paso sobre el que el convertidor no está seguro se convierte según la lectura más probable e incluye una nota en el informe. Compare esos pasos con la salida de Prophecy.

## Código del proyecto en los pasos

Los proyectos de Prophecy contienen código: gems Script, instrucciones SQL, macros, entradas dinámicas, llamadas a procedimientos almacenados y gems personalizados. El convertidor no ejecuta ese código. Lo coloca dentro de un paso:

- El SQL se traduce al dialecto SQL de su inquilino y se coloca en un paso SQL, con las entradas del gem disponibles con los nombres con los que la consulta las lee.
- Los scripts de Python se colocan en un paso de Python, con el acceso a tablas reescrito. Un script que llama a métodos de DataFrame de Spark conserva esas llamadas y las ejecuta en el paso.
- Un gem personalizado, incluido un gem de Gem Builder, ejecuta en un paso de Python el código de PySpark que la exportación de su pipeline contiene para él.
- Una macro de un paquete dbt conocido se convierte en los pasos estándar que hacen lo que hace la macro. También se lee y se convierte una macro de su propio proyecto o de un paquete que incluye la exportación, con bloques if y for, set, filtros, macros anidadas y adapter dispatch.
- Una función de agregación definida por el usuario en Python en un gem Aggregate se ejecuta en un paso de Python para cada grupo.

Todo paso que contiene código del proyecto recibe una advertencia, igual que el SQL traducido. Revise el código de cada uno de esos pasos antes de ejecutar el flujo de trabajo. El convertidor omite cualquier elemento similar a una credencial que encuentre en cadenas y comentarios del código, así que agregue las credenciales a una conexión y no al código.

## Marcadores de posición para gems sin convertir

Un gem que el convertidor no puede reproducir se crea como un paso marcador de posición que lleva el nombre del gem. Algunos ejemplos son un gem personalizado cuyo código no está en la exportación y un gem que modifica datos fuera de la conversión, como una solicitud REST que puede cambiar datos, un Email o una operación sobre tablas o archivos, cuando no ha vinculado su clave `operation:`. Un conjunto de datos de base de datos o un External Table sin conexión vinculada no es un marcador de posición: se convierte en un paso que espera a que usted seleccione una conexión. De forma predeterminada, un marcador de posición falla cuando el flujo de trabajo llega a él, de modo que una ejecución no puede notificar éxito por un trabajo que nunca se realizó.

Establezca `allow_unconverted_placeholders` en `true` (en la ventana, **Importar los componentes sin convertir como marcadores de posición de paso directo**) para importar cada marcador de posición como un paso de paso directo. La ejecución continúa entonces más allá de él y la salida del marcador de posición es su entrada. El informe cuenta los marcadores de posición de paso directo y enumera sus pasos. Recree la funcionalidad con un paso nativo cuando su resultado importe.

## Ejecutar los flujos de trabajo convertidos

1. Abra los nuevos flujos de trabajo en el proyecto. El informe los enumera en orden de ejecución.
2. Defina las variables de proyecto que procedan de parámetros de Prophecy.
3. Cargue los archivos de los conjuntos de datos sin vincular en las rutas indicadas en el informe.
4. Revise los pasos que contienen código del proyecto.
5. Ejecute los flujos de trabajo y revise la tabla de salida de cada paso.

Los eventos programados creados a partir de las programaciones de Prophecy están habilitados si lo estaban en Prophecy, por lo que empiezan a ejecutar los flujos de trabajo convertidos según su programación. Para revisar primero los flujos de trabajo, deshabilite los eventos en [Eventos programados](/es/administration/scheduled-events/) y habilítelos cuando esté listo.

## Qué se convierte

Cada gem de Prophecy se convierte por completo en pasos nativos, variables de proyecto, eventos programados u objetos del lienzo, con las opciones que ofrece. La [matriz de conversión de Prophecy](/es/reference/prophecy-conversion-matrix/) enumera cada gem con el paso de PlaidCloud en el que se convierte, y [Casos límite](#casos-límite) enumera los pocos comportamientos que debe comprobar; el informe de conversión nombra cada uno donde ocurre.

### Movimiento de datos

| Funcionalidad | Cómo se convierte |
| --- | --- |
| Modos de escritura | Los modos de escritura de destino se convierten en pasos de la plataforma: SCD2 con las estrategias de comprobación y de marca de tiempo (la estrategia de marca de tiempo fecha cada versión a partir de la columna que nombra `scd2.updatedAtColumn` del gem), merge, `replaceWhere` e `insertInto`. Un merge aplica las expresiones SET por columna de sus cláusulas de actualización por coincidencia e inserción sin coincidencia; una cláusula que no establece ninguna columna toma todas las columnas de la fila entrante. La primera ejecución sobre un destino vacío escribe todas las filas, como hacen dbt y Delta. La primera ejecución no necesita una tabla creada de antemano, ni siquiera para un pipeline que lee un conjunto de datos en el que también escribe, a menos que la exportación no indique qué columnas tiene ese conjunto de datos: en ese caso, cree la tabla antes de la primera ejecución. Las ejecuciones posteriores aplican el filtro incremental o la condición de merge. Los modos `error` e `ignore` comprueban con la [condición de existencia de tabla](/es/guides/workflows/step-conditions/#condiciones-de-existencia-de-tabla). |
| Time travel | Un origen de tabla Delta o de catálogo que lee una versión anterior de su tabla, mediante `versionAsOf` o `timestampAsOf`, lee esa versión desde Databricks a través de la conexión que usted vincule. |
| Transmisión | Los orígenes y destinos de transmisión se ejecutan como lotes programados. El receptor de transmisión reemplaza su tabla en lugar de anexar, de modo que una nueva ejecución nunca duplica filas. Programe el flujo de trabajo para recoger los datos recién llegados. |
| Bases de datos | Los gems JDBC, Snowflake, Redshift, Hive, BigQuery, SAP HANA y External Table leen y escriben a través de la conexión de PlaidCloud que usted vincule. Un conjunto de datos de BigQuery se lee con [Importar SQL](/es/reference/workflow-steps/import/import-sql/) y se escribe con [Export External Database Tables](/es/reference/workflow-steps/export/export-external-tables/) (paso) en una [conexión de BigQuery](/es/reference/connectors/google/big-query/). Una tabla de SAP HANA escrita en cualquiera de los modos de merge del gem de HANA, incluidos SCD2 y los modos de eliminación, se almacena temporalmente junto al destino y se combina con él por la clave primaria del destino o por las columnas de merge del gem; si falta el destino, se crea primero. |
| MongoDB y Kafka | Un conjunto de datos de MongoDB se lee con [Importar MongoDB](/es/reference/workflow-steps/import/import-mongodb/), incluidos su filtro o pipeline de agregación, y una lectura que no declara columnas las toma de los primeros documentos, como hace el conector de Spark. Una escritura usa [Exportar MongoDB](/es/reference/workflow-steps/export/export-mongodb/) en el modo de escritura correspondiente: `update` actualiza los campos del documento coincidente o inserta uno, `ignore` escribe solo mientras la colección no contenga ningún documento, y `error` detiene la ejecución cuando contiene alguno. Un origen de Kafka lee sus temas entre los desplazamientos inicial y final con [Importar Kafka](/es/reference/workflow-steps/import/import-kafka/), y un destino de Kafka envía cada fila con [Exportar Kafka](/es/reference/workflow-steps/export/export-kafka/). Un conjunto de datos de Kafka que inicia sesión con `OAUTHBEARER` usa el [inicio de sesión OAuth](/es/reference/connectors/databases/apache-kafka/#oauth-oauthbearer) de la conexión de Kafka que usted vincule, porque la exportación no contiene credenciales. |
| Azure Cosmos DB | Una lectura envía la consulta del conjunto de datos, o lee todos los documentos, con [Solicitud REST](/es/reference/workflow-steps/general/rest-request/) en una conexión REST con autenticación de Cosmos DB, y sigue el encabezado de continuación de una página a otra. Una escritura envía una solicitud por cada fila según la estrategia de escritura del gem: overwrite, append, delete o patch. Una fila que contiene el ETag de su documento se reemplaza o elimina solo si el documento no ha cambiado desde entonces, y una fila que el contenedor rechaza por ese motivo, o por un documento inexistente o ya existente, se omite, como hace el conector de Spark. El modo `ignore` escribe solo mientras el contenedor no contenga ningún documento. |
| Salesforce | Una lectura usa [Salesforce: consultar objeto](/es/reference/workflow-steps/salesforce/query-salesforce-object/), con los registros eliminados y archivados incluidos cuando el gem lo solicita. Una escritura inserta, actualiza, hace upsert o elimina, con una solicitud por cada fila; un upsert busca coincidencias en el campo de ID externo del gem, o en `Id` cuando no nombra ninguno. |
| Smartsheet, Slack y Pinecone | Una lectura de Smartsheet de una hoja con nombre y columnas declaradas obtiene la hoja a través de su conexión REST y genera una fila por cada fila de la hoja y una columna por cada columna declarada. Las demás lecturas de Smartsheet, y las lecturas de Slack e Iceberg, usan [Import Singer Source](/es/reference/workflow-steps/import/import-singer/) (paso). Una escritura de Smartsheet agrega las filas a la hoja con nombre, y un overwrite elimina primero las filas de la hoja. Una escritura de Slack publica un mensaje por cada fila, y un mensaje que Slack rechaza hace fallar el paso. Un índice de Pinecone se lee como sus vectores y sus metadatos, y una escritura hace upsert de las filas como vectores. |
| Tableau y Power BI | Tableau y Tableau Write publican la entrada como una extracción Hyper mediante [Publish to Tableau](/es/reference/workflow-steps/export/export-to-tableau/) (paso) en la conexión de Tableau que usted vincule. Power BI Write envía las entradas a un conjunto de datos de inserción de Power BI mediante una conexión REST con OAuth 2.0, buscando el espacio de trabajo por nombre y creando el conjunto de datos cuando es nuevo. |
| Formatos de archivo | CSV, JSON, Parquet, Avro, Excel, XML, ancho fijo y ORC mediante [Importar ORC](/es/reference/workflow-steps/import/import-orc/). Las opciones de formato se asignan, o se marcan como neutras cuando no cambian ninguna fila: la ventana de hora de modificación de una lectura de Avro, la codificación EBCDIC de un archivo de ancho fijo, los registros de encabezado y de pie y los registros sin saltos de línea, el mapa de hojas y la contraseña de una lectura de Excel, las opciones de comillas de una escritura de CSV y una escritura de Excel con una hoja por cada valor. Los archivos de texto comprimidos se leen y escriben con gzip, Deflate (zlib), Zstandard, LZ4, Snappy y LZO; un archivo comprimido se lee cuando su nombre termina con la extensión de su códec. Los archivos cifrados se descifran y se cifran en el mismo lugar. Consulte [Archivos cifrados](#archivos-cifrados). |
| File Operation | Copy y Move se convierten en [Documento: copiar archivo](/es/reference/workflow-steps/document/copy-document-file/) o en Copy Directory sobre la carpeta que usted vincule, conservando solo los archivos cuyo nombre coincide con el `filenameRegex` del gem, y conservando la ruta de cada archivo bajo la carpeta de origen cuando el gem es recursivo. |
| Directory | Enumera los archivos de la carpeta de documentos vinculada con [Listado de directorio](/es/reference/workflow-steps/document/directory-listing/), en las columnas del gem. Con la opción de nombre de hoja activada, cada libro de Excel genera una fila por hoja y su `sheet_name`; los demás archivos generan una fila con un `sheet_name` vacío. |

### Columnas y filas

| Gem o función | Cómo se convierte |
| --- | --- |
| Surrogate Key | Las claves continúan desde una tabla que conserva la última clave emitida, como hace el archivo de claves del gem. Todos los gems que nombran el mismo archivo de claves comparten esa tabla, por lo que sus claves nunca se solapan. Una ejecución sin filas la deja como estaba, y las claves empiezan desde el valor inicial antes de que ninguna ejecución haya emitido una. |
| Column Parser, XML Parse, análisis de JSON | El texto XML y JSON se analiza con los pasos [Análisis de XML](/es/reference/workflow-steps/tables/table-xml-parse/) y [Analizar JSON](/es/reference/workflow-steps/tables/table-json-parse/), leyendo cada campo del texto del elemento, de un atributo o de un elemento secundario. El XML analizado sin esquema toma el tipo de cada campo de los datos, como hace `schema_of_xml` de Spark. |
| Reglas de negocio | Una regla de negocio del proyecto invocada en una expresión se convierte en las mismas condiciones, un `CASE` por cada columna que establece. |
| Conversiones de tipo | La conversión de texto a decimal o a long sigue exactamente a Spark: se recortan los espacios y los caracteres de control alrededor del número, un decimal se redondea hacia arriba a su escala, y el texto que no es un número, o un valor fuera de rango, es nulo. |
| Fechas y horas | Los formatos de fecha y hora se escriben para el motor de su espacio de trabajo, incluido Databend, y `window()` coloca cada marca de tiempo en su ventana de saltos, alineada como la alinea Spark. |
| Salidas de iteradores | Un Table Iterator o While Iterator cuyas columnas de salida solo se conocen en el momento de la ejecución reúne las filas de cada pasada por posición con [Tabla: unión de todo](/es/reference/workflow-steps/tables/table-union-all/#coincidencia-de-columnas), con cada columna ampliada a un tipo que admita todas las pasadas, como apila Prophecy las pasadas. |
| Data Encoder/Decoder AES | Se ejecuta en todos los motores. La clave, y el vector de inicialización y los datos adicionales cuando el gem los nombra, proceden de las variables de flujo de trabajo `aes_key`, `aes_iv` y `aes_aad`, que usted define. |
| Hash de Data Masking | Calcula los mismos valores que `hash()` de Spark. |
| Buffer, Simplify, Heat Map | Buffer dibuja una esquina redondeada con el mismo número de segmentos que Prophecy, Simplify elimina los mismos vértices, y Heat Map suma el calor en hexágonos H3 a la resolución del gem, de modo que un calor decimal sigue siendo decimal. |

### Servicios y control

| Gem | Cómo se convierte |
| --- | --- |
| Pipeline | Ejecuta el pipeline que nombra con un [Workflow Loop](/es/reference/workflow-steps/workflow-control/workflow-loop/) (paso), una vez por cada fila de entrada (una vez cuando no tiene entrada, nunca si no hay filas), con cada parámetro establecido a partir de una constante, una columna de la fila o una expresión sobre ella. Cada ejecución sigue adelante aunque falle una anterior, y la salida del gem tiene una fila por cada ejecución con su estado, mensaje y horas, como las registra Prophecy. |
| Programaciones | Una programación de un trabajo de Prophecy o de un pipeline SQL se convierte en un [evento programado](/es/administration/scheduled-events/) llamado `Prophecy <name>` en el flujo de trabajo convertido, habilitado a menos que esté deshabilitado en Prophecy. Un trabajo de Spark se convierte así cuando ejecuta un pipeline convertido sin reemplazos de configuración ni condiciones de ejecución. |
| Script | Un script de Python se coloca en un paso de Python. Un valor que el script establece en `Config` se convierte en una variable de flujo de trabajo que leen los pasos posteriores, restablecida al valor del pipeline al comienzo de cada ejecución, como ocurre con `Config` en Prophecy. |
| REST API, REST API Enrich | Pasos de [Solicitud REST](/es/reference/workflow-steps/general/rest-request/), una solicitud por cada fila de entrada, conservando una respuesta de error como hace Prophecy. Enrich también lee el estado, el motivo y la URL final. Una solicitud que espera un resultado asíncrono consulta periódicamente hasta que la respuesta indica que ha terminado. |
| Stored Procedure | Un gem que pasa argumentos llama a su procedimiento con [Ejecución remota: SQL](/es/reference/workflow-steps/agent/agent-remote-execution-of-sql/#ejecutar-una-instrucción-una-vez-por-fila) una vez por cada fila de entrada, con cada argumento vinculado desde su columna como parámetro. Un gem sin argumentos lo llama una vez a través de un agente. Elija la conexión o el agente en el paso convertido. |
| Email, Email Data | [Notify Via Email](/es/reference/workflow-steps/notifications/notify-via-email/) (paso) con Cc, Cco, Responder a y un mensaje por cada fila cuando un campo se lee de una columna. |
| OpenAI, Bedrock, SageMaker Endpoint | [Text: NLP (AI)](/es/reference/workflow-steps/text-documents/nlp-ai/) (paso) en la conexión de LLM de su espacio de trabajo. Las incrustaciones de OpenAI y Bedrock usan la tarea Embed, que requiere una conexión compatible con OpenAI o de Azure OpenAI; se rechaza una conexión de Anthropic. |
| Pinecone Lookup | Una solicitud REST por cada fila. |
| Data Quality Check, Deequ, Soda | Las comprobaciones se ejecutan en el almacén de datos y escriben la tabla de resultados. Un Data Quality Check detiene la ejecución solo cuando el gem establece `minFailedChecks` o una acción posterior `fail_pipeline`; en caso contrario, la tabla de resultados enumera los fallos. Deequ y Soda nunca detienen la ejecución. Una comprobación de longitud mínima o máxima sobre una columna numérica mide el número como texto. Las comprobaciones de Soda se convierten a partir del YAML del proyecto, incluidos valores faltantes, no válidos y válidos, estadísticas, longitudes, percentiles, duplicados entre columnas, actualidad, filas con error y sus propias consultas de métricas. |
| ToDo | Genera un error que nombra la herramienta y el mensaje originales cuando la ejecución llega a él. |

### Archivos cifrados

Un gem File Storage que lee un archivo cifrado se convierte en [Documento: descifrar archivo](/es/reference/workflow-steps/document/encrypt-decrypt-file/), que descifra el archivo en una carpeta propia antes de que lo lea la importación; la copia descifrada se elimina después. Un gem que escribe un archivo cifrado exporta a esa carpeta y luego cifra el archivo en su lugar con Documento: cifrar archivo. Se admiten archivos AES y Blowfish y libros de Excel protegidos con contraseña.

La exportación nunca contiene una clave, por lo que los pasos convertidos la leen de una variable de flujo de trabajo: `aes_key` para una clave AES o Blowfish, y `xlsx_password` para la contraseña de un libro. Defina la variable antes de ejecutar el flujo de trabajo y asígnele una clave destinada solo a estos archivos. Los campos de clave y de contraseña aceptan únicamente una referencia a una variable, de modo que nunca se escribe una clave en un paso.

## Casos límite

Estos son los comportamientos que un flujo de trabajo convertido no reproduce por sí solo. El informe de conversión nombra cada uno donde ocurre.

- **Código o datos que la exportación no incluye**: Un gem de Gem Builder u otro gem personalizado cuyo código no está en la exportación, y una llamada a una macro de un paquete dbt que la exportación omite, se convierten en un paso que indica lo que falta; exporte el proyecto con el código de sus pipelines y los paquetes dbt, o recree la lógica en un paso de Python o SQL. Los gems Ab Initio Error Detection y MTime pasan su entrada sin cambios, porque la regla que aplican no está en la exportación. Las comprobaciones de Soda que se leen de un archivo fuera del proyecto, y las que comparan con análisis anteriores o con otro conjunto de datos o prueban un formato que Soda nombra, no tienen fila en la tabla de resultados; calcúlelas en un paso posterior.
- **Resultados que solo se conocen cuando se ejecuta el pipeline**: Un gem REST API que aplana su respuesta coloca toda la respuesta en una columna cuando nada declara los nombres de los campos, algo que solo una ejecución revela; extraiga los campos que necesite en un paso posterior. Una macro de dbt que consulta el almacén de datos mientras dbt compila se convierte en un paso que la nombra; reemplace la consulta por los valores que devuelve. Un gem StoredProcedure de Spark se ejecuta, pero no se devuelven sus valores OUT; la salida son las columnas de paso directo. `input_file_name()` devuelve una cadena vacía sobre un origen de tabla o Delta, que no tiene archivo que nombrar, y `hash()` / `xxhash64()` dentro de una agregación, una ventana o un gem con varias entradas los calcula el almacén de datos, por lo que pueden diferir de los de Spark.
- **Valores escritos en un paso cuando se convierte el proyecto**: Un valor de parámetro que contiene una comilla, una barra invertida o una llave, un valor de pipeline que lee un paso SQL y la base de datos que una operación de tabla Delta nombra mediante configuración se escriben en el paso como valores fijos, por lo que cambiar la variable del flujo de trabajo no los modifica; edite el paso cuando cambie la configuración.
- **Código Scala**: Un script Scala, una expresión Scala o una función definida por el usuario o de agregación en Scala se convierte en un paso que la nombra; reescríbala en SQL o Python.
- **Inicio de sesión Kerberos de Kafka**: Un origen o destino de Kafka que inicia sesión con Kerberos (GSSAPI) se convierte sin el nombre del servicio Kerberos ni el mecanismo de inicio de sesión; defínalos en la conexión de PlaidCloud.
- **Transmisión**: Los orígenes, destinos y pipelines de transmisión se ejecutan como flujos de trabajo por lotes sobre los datos presentes cuando se ejecutan; programe el flujo de trabajo para que se ejecute con la frecuencia que necesite.
- **Componentes de trabajo**: Un trabajo de Spark convierte su único pipeline y su programación; sus demás componentes, condiciones de ejecución y reemplazos de configuración no se convierten.
- **Llamadas poco habituales**: Una función de agregación definida por el usuario invocada desde un rollup o una ventana, y una macro de dbt que usa Jinja más allá de if, for, set y los filtros comunes, se convierten en un paso que nombra el gem; llame a la función desde un gem Aggregate, o incorpore la macro en línea.

## Guías relacionadas

- [Migrar análisis de Savant](/es/guides/workflows/migrate-savant-analyses/)
- [Migrar flujos de trabajo de Alteryx](/es/guides/workflows/migrate-alteryx-workflows/)
- [Agregar cuentas de documentos](/es/guides/documents/adding-accounts/)
- [Administrar variables de flujo de trabajo](/es/guides/workflows/manage-workflow-variables/)
- [Ejecutar un flujo de trabajo](/es/guides/workflows/run-a-workflow/)
