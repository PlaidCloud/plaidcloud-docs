---
title: Matriz de conversión de Prophecy
description: Cómo PlaidCloud convierte los pipelines y proyectos SQL de Prophecy en pasos nativos de flujos de trabajo avanzados, con el estado de compatibilidad de cada gem.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/prophecy-conversion-matrix.md
---

PlaidCloud convierte los pipelines de Spark y los proyectos SQL de Prophecy en
flujos de trabajo avanzados nativos. El importador asigna cada gem de Prophecy a un paso del flujo de trabajo,
una variable de proyecto o un objeto del lienzo, de modo que un flujo de trabajo convertido se ejecuta de forma nativa en la nube
y no como una emulación.

Todos los gems, conectores y estructuras de proyecto se convierten: **Completo** significa que el gem
se convierte en un paso, una variable o un objeto del lienzo nativo de PlaidCloud que realiza el trabajo
del gem. Los pocos comportamientos que un flujo de trabajo convertido no reproduce por sí
mismo se enumeran en [Casos límite conocidos](#casos-límite-conocidos), cada uno con lo que
debe hacer.

Para ejecutar una conversión, consulte [Migrar proyectos de Prophecy](/es/guides/workflows/migrate-prophecy-projects/).

## Gems de pipelines de Spark

### Origen/Destino

| Gem | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| Lookup | Completo | [Tabla: búsqueda](/es/reference/workflow-steps/tables/table-lookup/) | Cada llamada de búsqueda se convierte en un paso Tabla: búsqueda dentro del paso que la usa; una clave sin coincidencia devuelve NULL y una clave duplicada devuelve una de sus filas. |
| Source | Completo | Paso de importación elegido según el formato del conjunto de datos (consulte [Conectores](#conectores)) | Cada Source se convierte en un paso de importación a una tabla con el nombre del conjunto de datos; un formato que el conversor no reconoce se lee como un archivo CSV cargado en la carpeta de documentos del flujo de trabajo, con una advertencia. |
| Streaming Source | Completo | La misma importación que Source por lotes | Los orígenes de streaming se convierten en una importación por lotes de una sola vez, con una advertencia. |
| Streaming Target | Completo | Carga por lotes con anexado | Los destinos de streaming se convierten en un anexado por lotes, con una advertencia. |
| Target | Completo | Paso de exportación o carga de tabla elegido según el formato del conjunto de datos y writeMode | Cada Target se convierte en un paso de carga o exportación de tabla en el modo de escritura del gem: append, overwrite, merge con sus expresiones SET, upsert, SCD2, replaceWhere e insertInto. |

### Preparar

| Gem | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| Data Cleansing | Completo | Expresiones de columna en un paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) | Convierte las opciones de relleno de nulos, recorte y mayúsculas y minúsculas en expresiones de columna; las columnas depuradas pasan al final. |
| Sequence | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con una expresión de número de fila | Agrega una columna de secuencia a partir del valor inicial y el incremento. |
| Surrogate Key Generator | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con una expresión de número de fila | Agrega una clave secuencial a partir del valor inicial; las claves continúan entre ejecuciones a partir de una tabla que guarda la última clave emitida. |

### Transformar

| Gem | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| Aggregate | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con agregación; paso [Pivot](/es/reference/workflow-steps/tables/table-pivot/) cuando el gem pivota | Agrupa y agrega, aplica la condición HAVING y pivota en una columna por valor de pivote; propagate-all conserva todas las demás columnas de entrada. |
| Bulk Column Expressions | Completo | Se expande a una expresión por columna en un paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) | Una expresión por cada columna indicada en un paso Table Extract; la conversión advierte de que se supone el diseño del gem. |
| Bulk Column Rename | Completo | Cambio de nombre de columna en un paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) | Un cambio de nombre por cada columna indicada en un paso Table Extract; la conversión advierte de que se supone el diseño del gem. |
| Deduplicate | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con distinct o un filtro por número de fila | Conserva una fila por clave: distinct, la primera o la última según su orden de clasificación, cualquiera, o solo las claves que aparecen una vez. |
| Dynamic Replace | Completo | Transformación de reemplazo dinámico, configurada a mano | Se convierte en reglas de reemplazo de la transformación de reemplazo dinámico; la conversión advierte de que se supone el diseño del gem. |
| Dynamic Select | Completo | Selección de columnas en un paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) resuelta por tipo | Resuelve las columnas por tipo en el momento de la conversión en una selección explícita. |
| Filter | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con una expresión de filtro | Se convierte en un paso Table Extract con una expresión de filtro; las condiciones NULL descartan la fila. |
| Flatten Schema | Completo | Pasos [Tabla: analizar JSON](/es/reference/workflow-steps/tables/table-json-parse/) y [Table Extract](/es/reference/workflow-steps/tables/table-extract/) | Aplana los campos anidados en columnas con el nombre formado con el delimitador del gem y expande las matrices en una fila por elemento. |
| Fuzzy Match | Completo | Pasos [Table Extract](/es/reference/workflow-steps/tables/table-extract/) y [User Defined Transform](/es/reference/workflow-steps/general/user-defined-transform/) | Empareja los registros, puntúa cada campo de coincidencia con el método del gem, promedia las puntuaciones y conserva los pares que alcanzan o superan su umbral. |
| Group By Rollup | Completo | Unión de pasos de agregación [Table Extract](/es/reference/workflow-steps/tables/table-extract/) por nivel de rollup | Expande el rollup en una agregación por nivel de agrupación, unidas con subtotales NULL. |
| Limit | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con un límite de filas | Se convierte en un límite de filas; las referencias de configuración se convierten en variables de proyecto. |
| Normalize | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con una expresión de expansión | Repite cada registro según la expresión de longitud, calcula las columnas de salida por índice y se detiene en el primer índice en el que se cumple la condición de finalización. |
| Order By | Completo | Ordenación en un paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) | Se convierte en una ordenación con las mismas claves, dirección y ubicación de los nulos. |
| Reformat | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con expresiones de columna | Se convierte en un paso Table Extract con una expresión por columna de salida; las columnas no indicadas se descartan. |
| Sample Rows | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con un límite de filas o una muestra aleatoria | Conserva una fracción o un número aleatorio de filas; las filas elegidas difieren de las de la ejecución de Spark porque el muestreo es aleatorio. |
| Schema Transform | Completo | Cadena de pasos [Table Extract](/es/reference/workflow-steps/tables/table-extract/) aplicados en orden | Aplica cada operación en orden: agregar o reemplazar una columna, eliminar, cambiar de nombre, agregar si falta con su valor predeterminado y agregar una regla de negocio del proyecto. |
| Set Operation | Completo | [Tabla: unión de todo](/es/reference/workflow-steps/tables/table-union-all/); [Tabla: anticombinación](/es/reference/workflow-steps/tables/table-anti-join/) para except; [Tabla: combinación interna](/es/reference/workflow-steps/tables/table-inner-join/) para intersect | Union all apila las entradas; except all e intersect all conservan el número correcto de filas duplicadas. |
| TransposeAgg | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con agregación | Convierte la agrupación, las agregaciones y el pivote del gem como un Aggregate, con una advertencia para revisarlo. |
| Unpivot | Completo | Paso [Melt](/es/reference/workflow-steps/tables/table-melt/) | Apila las columnas seleccionadas en columnas de nombre y de valor. |
| Watermark | Completo | No se necesita ningún paso | Descartado: una ejecución por lotes lee todos los datos presentes, por lo que no hay un límite de datos tardíos que aplicar. |
| Window Function | Completo | Expresiones de ventana en un paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) | Agrega columnas de ventana con la partición, el orden y el marco del gem, por filas o por rango, con límites sin acotar, de la fila actual o con desplazamiento. |

### Combinar/Dividir

| Gem | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| Compare Columns | Completo | Combinación externa completa más agregaciones por columna | Compara las columnas mediante una combinación externa completa de los datos sin pivotar, con recuentos de coincidencias y discrepancias. |
| Join | Completo | [Tabla: combinación interna](/es/reference/workflow-steps/tables/table-inner-join/), [Combinación de varias tablas](/es/reference/workflow-steps/tables/table-multi-table-join/), [Tabla: anticombinación](/es/reference/workflow-steps/tables/table-anti-join/) o [Tabla: combinación cruzada](/es/reference/workflow-steps/tables/table-cross-join/) | Construye la combinación de cada tipo (interna, izquierda, derecha, completa, semi, anti, cruzada y natural) con cualquier condición de combinación, aplica la cláusula where y escribe la lista de selección. |
| Repartition | Completo | No se necesita ningún paso | Descartado: PlaidCloud administra el particionamiento, por lo que el paso siguiente lee directamente la tabla anterior. |
| Row Distributor | Completo | Un filtro [Table Extract](/es/reference/workflow-steps/tables/table-extract/) por salida | Se convierte en un filtro por salida; las filas pueden llegar a varias salidas. |

### Analizar

| Gem | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| Column Parser | Completo | [Tabla: analizar JSON](/es/reference/workflow-steps/tables/table-json-parse/) / [Tabla: análisis de XML](/es/reference/workflow-steps/tables/table-xml-parse/) | Se convierte en un análisis JSON o XML de la columna indicada; la conversión advierte de que se supone el diseño del gem. |

### Personalizado

| Gem | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| Custom Gem (Gem Builder) | Completo | Paso [User Defined Transform](/es/reference/workflow-steps/general/user-defined-transform/) que ejecuta el código generado del gem | El código PySpark generado del gem, procedente de la exportación del pipeline, se ejecuta en un paso de Python, con una advertencia para revisarlo. |
| CustomReformatBitbucket | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) | Se convierte como el Reformat cuyas expresiones contiene el gem, con una advertencia para revisarlo. |
| Data Quality Check | Completo | [Tabla: unión de todo](/es/reference/workflow-steps/tables/table-union-all/) de una fila de resultado por comprobación; [Generar error de flujo de trabajo](/es/reference/workflow-steps/workflow-control/raise-workflow-error/) para detenerse ante los fallos | Evalúa cada comprobación sobre la entrada y escribe una fila de resultado por comprobación con su estado y mensaje. Los datos pasan sin cambios y la ejecución se detiene cuando se alcanza el umbral de fallos del gem. |
| Deequ | Completo | Comprobaciones con paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) | Deja pasar los datos y genera la tabla de resultados de restricciones para las reglas isComplete, isUnique, isNonNegative e isContainedIn. |
| Delta Table Operations | Completo | Pasos [Table In-Place Delete](/es/reference/workflow-steps/tables/table-in-place-delete/), [Table Update](/es/reference/workflow-steps/tables/table-update/), [Table Drop](/es/reference/workflow-steps/tables/table-drop/), [Table Restore to Timestamp](/es/reference/workflow-steps/tables/table-restore-timestamp/) | Eliminar, actualizar, descartar y restaurar a una marca de tiempo se asignan a pasos de tabla; optimize, vacuum y restore por versión dejan pasar los datos con una advertencia. |
| Directory | Completo | [Listado de directorio](/es/reference/workflow-steps/document/directory-listing/) | Enumera los archivos de la carpeta de documentos vinculada en las columnas del gem; con la opción de nombre de hoja, cada libro genera una fila por hoja. Una carpeta inexistente genera cero filas. |
| Email | Completo | Paso [Notify Via Email](/es/reference/workflow-steps/notifications/notify-via-email/) | Envía el correo electrónico, con un adjunto de datos opcional, a través de una conexión de correo vinculada. |
| Email Data | Completo | Paso [Notify Via Email](/es/reference/workflow-steps/notifications/notify-via-email/) | Envía por correo electrónico las filas de entrada como tabla y deja pasar la entrada sin cambios. |
| File Operation | Completo | Paso [Copy Document File](/es/reference/workflow-steps/document/copy-document-file/) o paso [Copy Document Directory](/es/reference/workflow-steps/document/copy-document-directory/) | Copia, mueve o sincroniza archivos de la carpeta de documentos vinculada a la carpeta de documentos del flujo de trabajo convertido; un movimiento elimina los archivos de origen. |
| Log | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) | Escribe la fila de evento del gem (hora, nombre del gem, tipo de evento y texto) en su tabla de salida. |
| REST API Enrich | Completo | [Solicitud REST](/es/reference/workflow-steps/general/rest-request/) | Llama a la API una vez por fila y agrega las columnas de la respuesta. |
| Script | Completo | Paso de Python con reescritura del acceso a los marcos de datos | Incrusta el cuerpo del script en un paso de Python, con el acceso a los marcos de datos reescrito; los cuerpos en Scala se conservan con una nota. |
| Soda Data Quality Check | Completo | Comprobaciones con paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) | Genera la tabla de resultados de las comprobaciones a partir de las comprobaciones de Soda. |
| SQL Statement | Completo | Paso de SQL por pestaña de salida, con el texto traducido al dialecto del inquilino | Incrusta cada pestaña como un paso de SQL con las entradas vinculadas como tablas temporales; traducido al dialecto del inquilino. |
| Todo | Completo | [Generar error de flujo de trabajo](/es/reference/workflow-steps/workflow-control/raise-workflow-error/) o paso [Notify via Log](/es/reference/workflow-steps/notifications/notify-via-log/) | Marca la lógica que aún falta por escribir: un mensaje de registro cuando nada la lee, o un paso que detiene la ejecución con el mensaje del gem cuando un paso posterior depende de ella. |

### Informe

| Gem | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| Tableau | Completo | Paso [Publish to Tableau](/es/reference/workflow-steps/export/export-to-tableau/) | Escribe una extracción Hyper y la publica en la conexión de Tableau vinculada. |

### ML/IA

| Gem | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| Bedrock | Completo | Paso [Text NLP AI](/es/reference/workflow-steps/text-documents/nlp-ai/) | Incrusta la columna de texto mediante la conexión de IA del espacio de trabajo. |
| OpenAI | Completo | Paso [Text NLP AI](/es/reference/workflow-steps/text-documents/nlp-ai/) | Responde preguntas o incrusta texto mediante la conexión de IA del espacio de trabajo. |
| Pinecone Lookup | Completo | [Solicitud REST](/es/reference/workflow-steps/general/rest-request/) | Consulta el índice de Pinecone para cada fila y agrega las columnas pinecone_matches y pinecone_error. |
| SageMaker Endpoint | Completo | Paso [Text NLP AI](/es/reference/workflow-steps/text-documents/nlp-ai/) | Responde preguntas mediante la conexión de IA del espacio de trabajo. |
| Text Processing | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) para la división en fragmentos; [Solicitud REST](/es/reference/workflow-steps/general/rest-request/) para el raspado web | La división en fragmentos se convierte en una expresión de fragmentos de caracteres; el raspado web obtiene la URL de cada fila y reincorpora el contenido de la página a la fila. |

### Subgrafo/Control

| Gem | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| Control Flow Input | Completo | Descartado (solo marcador de límite) | Se descarta; solo marca el límite de entrada del subflujo de trabajo iterador. |
| Control Flow Output | Completo | Descartado (solo marcador de límite) | Se descarta; solo marca el límite de salida del subflujo de trabajo iterador. |
| Subgraph (Basic) | Completo | Contenedor del lienzo / flujo de trabajo anidado a partir de procesos en línea | Convierte el grafo interno en línea en un flujo de trabajo anidado (o pasos integrados en línea) con parámetros de tabla de entrada y salida. |
| Table Iterator | Completo | Paso [Workflow Loop](/es/reference/workflow-steps/workflow-control/workflow-loop/) | Ejecuta el cuerpo del bucle una vez por fila de entrada, estableciendo cada valor de configuración a partir de su columna, hasta maxIteration. |
| While Iterator | Completo | Paso [Workflow Loop](/es/reference/workflow-steps/workflow-control/workflow-loop/) | Ejecuta el cuerpo del bucle una vez por pasada, pasando el número de iteración, hasta que el cuerpo no devuelve filas o se alcanza el máximo del gem. |

## Gems de SQL y de analista

### Origen/Destino

| Gem | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| External table Source/Target (BigQuery, Databricks, SAP HANA, MongoDB, MSSQL, Oracle, Postgres, Redshift, Salesforce, Snowflake, Synapse) | Completo | Paso de importación o exportación de datos externos con la conexión de base de datos correspondiente | Lee o escribe una tabla en una base de datos externa a través de una conexión de PlaidCloud. |
| File storage Source/Target (ADLS, Databricks Volumes, GCS, OneDrive, S3, SFTP, SharePoint, Smartsheet) | Completo | Pasos de importación y exportación de archivos con una cuenta de documentos (ADLS/GCS/S3/SFTP/SharePoint/OneDrive) | Lee o escribe archivos en almacenamiento en la nube o SFTP con unión mediante comodines, desencadenador, eliminación o movimiento y opciones de cifrado. |
| Model | Completo | Tabla de salida del paso anterior | Lee otro modelo como la tabla producida por el paso anterior al que se hace referencia. |
| Seed | Completo | [Importar: CSV](/es/reference/workflow-steps/import/import-csv/) | El CSV de seed se importa a una tabla de PlaidCloud. |
| Source | Completo | Paso de importación elegido según el formato del conjunto de datos (consulte [Conectores](#conectores)) | Cada Source se convierte en un paso de importación a una tabla con el nombre del conjunto de datos; un formato que el conversor no reconoce se lee como un archivo CSV cargado en la carpeta de documentos del flujo de trabajo, con una advertencia. |
| Target Model / Table (Target) | Completo | Pasos [Table Extract](/es/reference/workflow-steps/tables/table-extract/), [Upsert](/es/reference/workflow-steps/tables/table-upsert/), [Copiar tabla](/es/reference/workflow-steps/tables/table-copy/) y [Tabla: unión de todo](/es/reference/workflow-steps/tables/table-union-all/) | Escribe la selección final del modelo en una tabla de PlaidCloud como replace, append, upsert, delete-and-insert, SCD2 o reemplazo por predicado. |
| Upload Files | Completo | [Importar: CSV](/es/reference/workflow-steps/import/import-csv/) | Los archivos locales cargados se convierten en una tabla mediante un paso de importación. |

### Preparar

| Gem | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| Data Cleansing | Completo | Expresiones de columna en un paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) | Convierte las opciones de relleno de nulos, recorte y mayúsculas y minúsculas en expresiones de columna; las columnas depuradas pasan al final. |
| Data Masking | Completo | Expresiones de columna para el enmascaramiento de caracteres o el hash | Enmascara o aplica hash a columnas de texto seleccionadas en el mismo lugar o como columnas nuevas. |
| Find Duplicates | Completo | Expresión de ventana de número de fila más filtro | Devuelve las filas únicas, duplicadas o seleccionadas por recuento o posición, por clave. |
| Generate Rows | Completo | Tabla de secuencia combinada y filtrada por fila de entrada | Genera filas por cada fila de entrada a partir de las expresiones de inicio, condición y bucle. |
| Imputation | Completo | Agregación más reincorporación por combinación y expresión de columna | Reemplaza los nulos o los valores centinela por el promedio, la mediana, la moda o un valor fijo. |
| Multi-Column Edit | Completo | Expresiones por columna expandidas a partir de la plantilla | Aplica una plantilla de expresión a cada columna seleccionada. |
| Multi-Column Rename | Completo | Asignación de cambio de nombre de columnas en un paso de selección | Cambia el nombre de las columnas seleccionadas mediante prefijo, sufijo o expresión de nombre. |
| Record ID | Completo | Expresión de columna de número de fila o uuid | Agrega una columna de ID de registro UUID o secuencial. |
| Sample | Completo | Límite de filas u opción de muestra en el paso de extracción | Toma las filas primeras, últimas, aleatorias, cada N o por porcentaje, en conjunto o por grupo. |
| Tile | Completo | Expresiones de ventana para el número de segmento y la secuencia | Asigna números de segmento por suma igual, recuento, bandas de desviación estándar, valores distintos o puntos de corte manuales. |

### Transformar

| Gem | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| Aggregate | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con agregación; paso [Pivot](/es/reference/workflow-steps/tables/table-pivot/) cuando el gem pivota | Agrupa y agrega, aplica la condición HAVING y pivota en una columna por valor de pivote; propagate-all conserva todas las demás columnas de entrada. |
| Count Records | Completo | Paso de agregación con funciones de recuento | Devuelve los recuentos totales, no nulos o distintos como una sola fila. |
| Data Encoder/Decoder | Completo | Expresiones de columna para codificar y decodificar en base64 y hexadecimal | Codifica o decodifica las columnas seleccionadas; AES solo en Databricks. |
| Deduplicate | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con distinct o un filtro por número de fila | Conserva una fila por clave: distinct, la primera o la última según su orden de clasificación, cualquiera, o solo las claves que aparecen una vez. |
| Dynamic Select | Completo | Selección de columnas en un paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) resuelta por tipo | Resuelve las columnas por tipo en el momento de la conversión en una selección explícita. |
| Filter | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con una expresión de filtro | Se convierte en un paso Table Extract con una expresión de filtro; las condiciones NULL descartan la fila. |
| Finance | Completo | Expresión de columna que implementa la función financiera | Anexa el resultado de una función financiera (FV, PV, NPV, IRR, ...) como una columna nueva. |
| Flatten Schema | Completo | Pasos [Tabla: analizar JSON](/es/reference/workflow-steps/tables/table-json-parse/) y [Table Extract](/es/reference/workflow-steps/tables/table-extract/) | Aplana los campos anidados en columnas con el nombre formado con el delimitador del gem y expande las matrices en una fila por elemento. |
| Fuzzy Match | Completo | Pasos [Table Extract](/es/reference/workflow-steps/tables/table-extract/) y [User Defined Transform](/es/reference/workflow-steps/general/user-defined-transform/) | Empareja los registros, puntúa cada campo de coincidencia con el método del gem, promedia las puntuaciones y conserva los pares que alcanzan o superan su umbral. |
| Limit | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con un límite de filas | Se convierte en un límite de filas; las referencias de configuración se convierten en variables de proyecto. |
| Order By | Completo | Ordenación en un paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) | Se convierte en una ordenación con las mismas claves, dirección y ubicación de los nulos. |
| Pivot | Completo | Paso [Pivot](/es/reference/workflow-steps/tables/table-pivot/) | Convierte los valores de pivote seleccionados en columnas de agregaciones; una lista de valores en modo Simple obtenida en tiempo de diseño se convierte como los valores enumerados. |
| Reformat | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con expresiones de columna | Se convierte en un paso Table Extract con una expresión por columna de salida; las columnas no indicadas se descartan. |
| Running Total | Completo | Columna con expresión de ventana de suma acumulada | Anexa sumas acumuladas por cada columna seleccionada. |
| Snowflake Unpivot (third-party) | Completo | Paso [Melt](/es/reference/workflow-steps/tables/table-melt/) | Despivota columnas mediante UNPIVOT de Snowflake. |
| Transpose | Completo | Paso [Melt](/es/reference/workflow-steps/tables/table-melt/) | Apila las columnas de datos en columnas de nombre y de valor de texto. |
| TransposeAgg | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con agregación | Convierte la agrupación, las agregaciones y el pivote del gem como un Aggregate, con una advertencia para revisarlo. |
| Unpivot | Completo | Paso [Melt](/es/reference/workflow-steps/tables/table-melt/) | Apila las columnas de datos en columnas de nombre y de valor. |
| Weighted Average | Completo | Paso de agregación con expresión de promedio ponderado | Calcula una media ponderada en conjunto o por grupo. |
| Window Function | Completo | Expresiones de ventana en un paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) | Agrega columnas de ventana con la partición, el orden y el marco del gem, por filas o por rango, con límites sin acotar, de la fila actual o con desplazamiento. |

### Combinar/Dividir

| Gem | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| Except | Completo | [Tabla: anticombinación](/es/reference/workflow-steps/tables/table-anti-join/) sobre todas las columnas más un paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con distinct | Conserva las filas de la primera entrada que no aparecen en ninguna de las demás entradas. |
| Intersect | Completo | [Tabla: combinación interna](/es/reference/workflow-steps/tables/table-inner-join/) sobre todas las columnas más distinct | Conserva las filas presentes en todas las entradas. |
| Join | Completo | [Tabla: combinación interna](/es/reference/workflow-steps/tables/table-inner-join/), [Combinación de varias tablas](/es/reference/workflow-steps/tables/table-multi-table-join/), [Tabla: anticombinación](/es/reference/workflow-steps/tables/table-anti-join/) o [Tabla: combinación cruzada](/es/reference/workflow-steps/tables/table-cross-join/) | Construye la combinación de cada tipo (interna, izquierda, derecha, completa, semi, anti, cruzada y natural) con cualquier condición de combinación, aplica la cláusula where y escribe la lista de selección. |
| Union | Completo | [Tabla: unión de todo](/es/reference/workflow-steps/tables/table-union-all/) | Apila las entradas por posición y elimina los duplicados cuando el gem no los conserva. |
| Union By Name | Completo | [Tabla: unión de todo](/es/reference/workflow-steps/tables/table-union-all/) | Se convierte en una unión de todo que alinea las columnas por nombre y rellena con nulos las que faltan. |

### Analizar

| Gem | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| JSON Parse | Completo | [Tabla: analizar JSON](/es/reference/workflow-steps/tables/table-json-parse/) | Analiza una columna de texto JSON en campos estructurados. |
| Regex | Completo | Expresiones regulares en un paso Table Extract o de transformación | Reemplaza, analiza, hace coincidir o divide en tokens una columna de texto con una expresión regular. |
| Text To Columns | Completo | Pasos de división de columnas o de expansión con delimitador de expresión regular | Divide una columna delimitada en columnas o filas mediante un delimitador de expresión regular. |
| XML Parse | Completo | [Tabla: análisis de XML](/es/reference/workflow-steps/tables/table-xml-parse/) | Analiza una columna de texto XML en campos estructurados. |

### Personalizado

| Gem | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| Directory | Completo | [Listado de directorio](/es/reference/workflow-steps/document/directory-listing/) | Enumera los archivos de la carpeta de documentos vinculada en las columnas del gem; con la opción de nombre de hoja, cada libro genera una fila por hoja. Una carpeta inexistente genera cero filas. |
| DynamicInput | Completo | Paso de SQL para las plantillas de consulta; bucle de flujo de trabajo para el modo de varios archivos | El modo de plantilla de consulta incrusta la plantilla como un paso de SQL; el modo de varios archivos se asigna con suposiciones. |
| Email | Completo | Paso [Notify Via Email](/es/reference/workflow-steps/notifications/notify-via-email/) | Envía el correo electrónico, con un adjunto de datos opcional, a través de una conexión de correo vinculada. |
| RestAPI | Completo | [Solicitud REST](/es/reference/workflow-steps/general/rest-request/) | Envía una solicitud por fila de entrada con su URL, encabezados, consulta, cuerpo y reintentos, conserva la respuesta y sondea una solicitud asíncrona hasta que termina. Las credenciales proceden de la conexión que usted vincula. |
| Script | Completo | Paso de Python con reescritura del acceso a los marcos de datos | Incrusta el cuerpo del script en un paso de Python, con el acceso a los marcos de datos reescrito; los cuerpos en Scala se conservan con una nota. |
| SQL Statement | Completo | Paso de SQL por pestaña de salida, con el texto traducido al dialecto del inquilino | Incrusta cada pestaña como un paso de SQL con las entradas vinculadas como tablas temporales; traducido al dialecto del inquilino. |
| StoredProcedure | Completo | Paso [Agent Remote Execution of SQL](/es/reference/workflow-steps/agent/agent-remote-execution-of-sql/) | Llama al procedimiento en su almacén de datos a través de la conexión que usted elige: una vez por fila de entrada con cada argumento vinculado a su columna, o una sola vez cuando no recibe argumentos. Las columnas de entrada pasan sin cambios. |
| Table Operations | Completo | Pasos [Table In-Place Delete](/es/reference/workflow-steps/tables/table-in-place-delete/), [Table Update](/es/reference/workflow-steps/tables/table-update/), [Table Drop](/es/reference/workflow-steps/tables/table-drop/) | Actualizar, eliminar y descartar se asignan a pasos de tabla; vacuum y optimize se convierten en la optimización de tablas o en una operación nula con una advertencia. |
| ToDo | Completo | [Generar error de flujo de trabajo](/es/reference/workflow-steps/workflow-control/raise-workflow-error/) o paso [Notify via Log](/es/reference/workflow-steps/notifications/notify-via-log/) | Marca la lógica que aún falta por escribir: un mensaje de registro cuando nada la lee, o un paso que detiene la ejecución con el mensaje del gem cuando un paso posterior depende de ella. |

### Espacial

| Gem | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| Buffer | Completo | Paso [Spatial Buffer](/es/reference/workflow-steps/spatial/spatial-buffer/) | Amplía cada geometría según la distancia configurada en millas o kilómetros. |
| CreatePoint | Completo | Paso [Table Extract](/es/reference/workflow-steps/spatial/spatial-sql-recipes/) con `geom_point` | Construye una geometría de puntos a partir de las columnas de longitud y latitud. |
| Distance | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) | Calcula la distancia, la dirección cardinal y el rumbo entre dos puntos WKT. |
| FindNearest | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con una combinación cruzada | Encuentra los N puntos de destino más cercanos a cada punto de origen dentro de una distancia máxima. |
| HeatMap | Completo | [Heat Map (macro)](/es/reference/workflow-steps/macros/macro-heat-map/) | Agrupa los puntos en hexágonos H3 con la resolución del gem, distribuye el calor por la cuadrícula según la distancia de rejilla con su atenuación y proporciona la densidad y el contorno de cada hexágono. |
| PolyBuild | Completo | Paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) y un paso de Python | Construye WKT de polígono o polilínea a partir de puntos ordenados por grupo. |
| Simplify | Completo | Paso [Spatial Generalize](/es/reference/workflow-steps/spatial/spatial-generalize/) | Simplifica geometrías WKT según una tolerancia en millas o kilómetros. |
| SpatialMatch | Completo | [Coincidencia espacial](/es/reference/workflow-steps/spatial/spatial-match/) | Hace coincidir geometrías de origen y destino por intersecta, contiene, está dentro, toca o envolvente. |

### Informe

| Gem | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| PowerBIWrite | Completo | [Solicitud REST](/es/reference/workflow-steps/general/rest-request/) | Crea el conjunto de datos de Power BI y envía las filas a través de la API REST de Power BI. |
| TableauWrite | Completo | Paso [Publish to Tableau](/es/reference/workflow-steps/export/export-to-tableau/) | Escribe una extracción Hyper y la publica en la conexión de Tableau vinculada. |
| Visualize | Completo | [Copiar tabla](/es/reference/workflow-steps/tables/table-copy/) | Deja pasar las filas sin cambios; cree el gráfico como un panel de control de PlaidCloud sobre la misma tabla. |

### Subgrafo/Control

| Gem | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| Condition | Completo | [Tabla: combinación cruzada](/es/reference/workflow-steps/tables/table-cross-join/) y paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) | Evalúa las condiciones sobre toda la entrada y envía cada fila a la primera salida cuya condición se cumple; si no, a la última salida. |
| Macro | Completo | Paso de SQL con el cuerpo de la macro expandido | Incrusta el cuerpo de la macro como un paso de SQL traducido al dialecto del inquilino, con las entradas vinculadas como tablas temporales. |
| Pipeline (trigger) | Completo | Paso [Workflow Loop](/es/reference/workflow-steps/workflow-control/workflow-loop/) | Ejecuta el pipeline indicado una vez por fila de entrada con sus parámetros y su condición de activación, continúa tras una ejecución fallida y devuelve una fila por ejecución. |
| Subgraph (Basic) | Completo | Contenedor del lienzo / flujo de trabajo anidado a partir de procesos en línea | Convierte el grafo interno en línea en un flujo de trabajo anidado (o pasos integrados en línea) con parámetros de tabla de entrada y salida. |

## Conectores

Los formatos de conjuntos de datos y los conectores son configuraciones de origen y destino de un gem, no gems. Cada formato se convierte en el paso de importación o exportación indicado, y la conversión nunca se pone en contacto con el sistema de origen o de destino.

| Formato | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| Avro | Completo | Importar: [Avro](/es/reference/workflow-steps/import/import-avro/); Exportar: [Avro](/es/reference/workflow-steps/export/export-to-avro/) | Lee y escribe archivos Avro. |
| BigQuery | Completo | Conexión de base de datos externa con importación de tabla | Lee y escribe a través de una conexión. |
| Binary files | Completo | [Listado de directorio](/es/reference/workflow-steps/document/directory-listing/) con el contenido de los archivos; [Ejecutor de Alteryx](/es/reference/workflow-steps/general/alteryx-executor/) para escribir | Lee cada archivo de la carpeta con su ruta, hora de modificación, longitud y contenido; escribe el contenido de cada fila en el archivo que indica su ruta. |
| Catalog table | Completo | Vinculación a una tabla existente de PlaidCloud | Se vincula a una tabla por nombre; la lectura y todos los modos de escritura se convierten. |
| Cosmos DB | Completo | Importación y exportación: [Solicitud REST](/es/reference/workflow-steps/general/rest-request/) | Lee y escribe los documentos del contenedor a través de su conexión de Cosmos DB. |
| CSV | Completo | [Importar: CSV](/es/reference/workflow-steps/import/import-csv/); Exportar: CSV | Lee y escribe archivos delimitados con opciones de encabezado, separador, comillas, carácter de escape y codificación. |
| Data Generator | Completo | Paso [Table Faker](/es/reference/workflow-steps/tables/table-faker/) | Genera las columnas del conjunto de datos con los mismos tipos de datos ficticios. |
| DataHub table | Completo | [Importar SQL](/es/reference/workflow-steps/import/import-sql/) | Lee la tabla que indica el conjunto de datos a través de su conexión; una escritura llega a una tabla de PlaidCloud. |
| Delta | Completo | Vinculación a una tabla existente de PlaidCloud | Lee y escribe la tabla en todos los modos de escritura; la lectura de una versión anterior se hace a través de la conexión de Databricks que usted vincula. |
| Excel (XLSX) | Completo | Importar: Excel; Exportar: Excel | Lee y escribe hojas y rangos de libros. |
| Fixed format | Completo | Importar: [ancho fijo](/es/reference/workflow-steps/import/import-fixed-width/); Exportar: [CSV](/es/reference/workflow-steps/export/export-to-csv/) | Lee archivos de ancho fijo con el diseño derivado de los anchos de columna del conjunto de datos; escribe un archivo delimitado. |
| Hive | Completo | Importar: [Importar SQL](/es/reference/workflow-steps/import/import-sql/); Exportar: [tablas externas](/es/reference/workflow-steps/export/export-external-tables/) | Lee y escribe la tabla a través de su conexión de Hive. |
| Iceberg | Completo | Vinculación a una tabla existente de PlaidCloud | Lee y escribe la tabla. |
| JDBC | Completo | Conexión de base de datos externa con importación de tabla | Lee una tabla o consulta y escribe en modo de reemplazo o anexado a través de su conexión; una instrucción posterior a la escritura se ejecuta después de la escritura. |
| JSON | Completo | [Tabla: analizar JSON](/es/reference/workflow-steps/tables/table-json-parse/) | Carga registros y aplana los campos anidados. |
| Kafka | Completo | Importar: [Importar Kafka](/es/reference/workflow-steps/import/import-kafka/); Exportar: [Exportar Kafka](/es/reference/workflow-steps/export/export-kafka/) | Lee un tema como un lote de mensajes y escribe filas como mensajes. |
| MongoDB | Completo | Importar: [MongoDB](/es/reference/workflow-steps/import/import-mongodb/); Exportar: [MongoDB](/es/reference/workflow-steps/export/export-mongodb/) | Lee y escribe la colección a través de su conexión de MongoDB. |
| ORC | Completo | Importar: [ORC](/es/reference/workflow-steps/import/import-orc/); Exportar: ORC | Lee y escribe archivos ORC. |
| Parquet | Completo | Importar: Parquet; Exportar: Parquet | Lee y escribe archivos Parquet. |
| Pinecone | Completo | Importación y exportación: [Solicitud REST](/es/reference/workflow-steps/general/rest-request/) | Lee los registros de un índice y hace upsert de filas como vectores a través de la API REST de Pinecone. |
| Redshift | Completo | Conexión de base de datos externa con importación de tabla | Lee y escribe a través de una conexión. |
| Salesforce | Completo | Importar: [Salesforce: consultar objeto](/es/reference/workflow-steps/salesforce/query-salesforce-object/); Exportar: [Solicitud REST](/es/reference/workflow-steps/general/rest-request/) | Lee un objeto o una consulta SOQL y escribe registros a través de su conexión de Salesforce. |
| Seed (inline) | Completo | [Importar: CSV](/es/reference/workflow-steps/import/import-csv/) | Carga las filas en línea como una tabla. |
| Slack | Completo | Importar: [Singer](/es/reference/workflow-steps/import/import-singer/); Exportar: [Solicitud REST](/es/reference/workflow-steps/general/rest-request/) | Lee los mensajes de un canal y publica cada fila como un mensaje a través de su conexión de Slack. |
| Smartsheet | Completo | Importación y exportación: [Solicitud REST](/es/reference/workflow-steps/general/rest-request/) | Lee y escribe las filas de la hoja a través de su conexión de Smartsheet. |
| Snowflake | Completo | Conexión de base de datos externa con importación de tabla | Lee y escribe a través de una conexión. |
| SQL file types (CSV, Excel, JSON, Parquet, Text, XML, fixed-width) | Completo | Pasos de importación y exportación de archivos con una cuenta de documentos | Lee y escribe el tipo de archivo; las opciones sin equivalente en PlaidCloud se señalan. |
| Text | Completo | [Importar: CSV](/es/reference/workflow-steps/import/import-csv/) como una sola columna | Lee cada línea como una columna. |
| Web page | Completo | [Solicitud REST](/es/reference/workflow-steps/general/rest-request/) | Lee la página de la URL del conjunto de datos en una tabla. |
| XML | Completo | [Tabla: análisis de XML](/es/reference/workflow-steps/tables/table-xml-parse/) | Carga registros por etiqueta de fila. |

## Expresiones y estructura del proyecto

| Área | Estado | Equivalente en PlaidCloud | Convierte |
| --- | --- | --- | --- |
| Expressions | Completo | Expresiones SQL de Spark y del almacén de datos, traducidas función por función | Las funciones y los operadores se convierten en expresiones de PlaidCloud; una función sin equivalente se señala por su nombre. |
| Project and graph structure | Completo | Cargador de proyectos | Cada formato de exportación de Prophecy se carga y se normaliza en un único modelo. |

## Casos límite conocidos

| Caso | Qué ocurre |
| --- | --- |
| Code or data the export does not include | Un Gem Builder u otro gem personalizado cuyo código no está en la exportación, y una llamada a una macro de un paquete dbt que la exportación omite, se convierten en un paso que indica lo que falta; exporte el proyecto con el código de sus pipelines y los paquetes dbt, o reconstruya la lógica en un paso de Python o SQL. Los gems Ab Initio Error Detection y MTime dejan pasar su entrada, porque la regla que aplican no está en la exportación. Las comprobaciones de Soda que leen de un archivo externo al proyecto, y las que comparan con análisis anteriores o con otro conjunto de datos o prueban un formato que nombra Soda, no tienen fila en la tabla de resultados; calcúlelas en un paso posterior. |
| Results only known when the pipeline runs | Un gem REST API que aplana su respuesta coloca toda la respuesta en una sola columna cuando nada declara los nombres de los campos, algo que solo una ejecución revela; extraiga los campos que necesite en un paso posterior. Una macro de dbt que consulta el almacén de datos mientras dbt compila se convierte en un paso que la nombra; reemplace la consulta por los valores que devuelve. Un gem StoredProcedure de Spark se ejecuta, pero sus valores OUT no se devuelven; la salida son las columnas de paso directo. `input_file_name()` devuelve una cadena vacía sobre un origen de tabla o Delta, que no tiene un archivo que nombrar, y `hash()` / `xxhash64()` dentro de una agregación, una ventana o un gem con varias entradas los calcula el almacén de datos, por lo que pueden diferir de los de Spark. |
| Values written into a step when the project converts | Un valor de parámetro que contiene comillas, una barra invertida o llaves, un valor de pipeline que lee un paso de SQL y la base de datos que indica una operación de tabla Delta mediante la configuración se escriben en el paso como valores fijos, por lo que cambiar la variable del flujo de trabajo no los modifica; edite el paso cuando cambie la configuración. |
| Scala code | Un script de Scala, una expresión de Scala o una función definida por el usuario o de agregación de Scala se convierte en un paso que la nombra; reescríbala en SQL o Python. |
| Kafka Kerberos sign-in | Un origen o destino de Kafka que inicia sesión con Kerberos (GSSAPI) se convierte sin el nombre de servicio de Kerberos ni el mecanismo de inicio de sesión; configúrelos en la conexión de PlaidCloud. |
| Streaming | Los orígenes, destinos y pipelines de streaming se ejecutan como flujos de trabajo por lotes sobre los datos presentes en el momento de la ejecución; programe el flujo de trabajo para que se ejecute con la frecuencia que necesite. |
| Job components | Un trabajo de Spark convierte su único pipeline y su programación; sus demás componentes, condiciones de ejecución e invalidaciones de configuración no se convierten. |
| Uncommon calls | Una función de agregación definida por el usuario llamada desde un rollup o una ventana, y una macro de dbt que usa Jinja más allá de if, for, set y los filtros habituales, se convierten en un paso que nombra el gem; llame a la función desde un gem Aggregate, o integre la macro en línea. |

## Validación de un flujo de trabajo convertido

Compare la salida del flujo de trabajo convertido con la salida de su propio pipeline de Prophecy: esquema, recuento de filas y valores de las filas. Ignore el orden de las filas, salvo que el flujo de trabajo dependa de él.
