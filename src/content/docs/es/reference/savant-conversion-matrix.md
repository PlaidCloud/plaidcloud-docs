---
title: Matriz de conversión de Savant
description: Cómo PlaidCloud convierte los análisis de Savant Labs en flujos de trabajo avanzados nativos, con el nivel de asignación de cada agente y los pocos casos límite con nombre.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/savant-conversion-matrix.md
---

PlaidCloud convierte los análisis de Savant Labs en flujos de trabajo avanzados nativos. El
importador asigna cada agente de Savant a un paso del flujo de trabajo, una variable de proyecto o un
objeto del lienzo, de modo que un flujo de trabajo convertido se ejecuta de forma nativa en la nube.

Para ejecutar una conversión, consulte [Migrar análisis de Savant](/es/guides/workflows/migrate-savant-analyses/).

Cada agente tiene un nivel de asignación. **Completo** significa que cada opción del agente tiene una
asignación válida a un paso de PlaidCloud. Las construcciones que se rechazan por su nombre se enumeran
en Rechazos con nombre.

Los conectores de sistemas externos están **conectados, no convertidos**; consulte
[Conexión con sistemas externos](#conexión-con-sistemas-externos).

## Compatibilidad de agentes

Los 33 agentes se convierten en el nivel Completo.

| Agente | Nivel | Equivalente en PlaidCloud | Qué convierte |
| --- | --- | --- | --- |
| Agente Adapter (`adapter`) | Completo | Paso de selección y proyección de esquema | Cambia el nombre, el tipo y el orden de los campos. |
| Agente API / Infer (servicio heredado) (`service`) | Completo | Igual que el agente API o el agente Infer, según serviceType | Un LLMService se convierte como el agente Infer y un APIService como el agente API; un serviceType ausente o mal escrito se lee de las claves del nodo con una advertencia. |
| Agente API (`apiService`) | Completo | Table Extract, [Solicitud REST](/es/reference/workflow-steps/general/rest-request/) y una combinación izquierda de vuelta | Una solicitud GET, POST, PUT, PATCH o DELETE por cada fila de entrada; el cuerpo de la respuesta sin procesar llega a una columna de texto, los errores HTTP permanecen como filas, se conservan todas las filas de entrada, y una cuota por período se convierte en una cantidad fraccionaria de solicitudes por segundo. Una URL relativa se une a la URL base de api_bindings o al host de la conexión REST; un host, un puerto o una ruta tomados de un campo de la fila se sustituyen en cada fila; se siguen la paginación por URL siguiente, por encabezado Link, por desplazamiento y por página, incluido un inicio, un tamaño de página o un nombre de parámetro definidos mediante una plantilla a partir de un campo de la fila. |
| Agente Blend (`blend`) | Completo | [Combinación interna](/es/reference/workflow-steps/tables/table-inner-join/), [Combinación externa](/es/reference/workflow-steps/tables/table-outer-join/), [Anticombinación](/es/reference/workflow-steps/tables/table-anti-join/) | Combinaciones interna, izquierda, derecha, completa, anticombinación y externa excluyendo la interna, condiciones unidas con OR, contiene y es parte de, con flujos coincidentes y sin coincidencia; se transfieren las columnas que un pivote o un análisis nombra solo en tiempo de ejecución. |
| Agente Dedupe (`deduplicate`) | Completo | [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con filas distintas | Conserva el primer registro por clave, dentro de los grupos de Agrupar por, y envía los duplicados a un segundo flujo o los marca. |
| Agente Destination (`destination`) | Completo | [Exportar: CSV](/es/reference/workflow-steps/export/export-to-csv/), [Exportar: Excel](/es/reference/workflow-steps/export/export-to-excel/), Exportar: Parquet, JSON, Avro o XML, [Export to PDF](/es/reference/workflow-steps/export/export-to-pdf/), [Exportar: Tableau Hyper](/es/reference/workflow-steps/export/export-hyper/) con [Publish to Tableau](/es/reference/workflow-steps/export/export-to-tableau/), [Export: External Database Tables](/es/reference/workflow-steps/export/export-external-tables/), [Export to Google Spreadsheet](/es/reference/workflow-steps/export/export-to-google-spreadsheet/), [Notify via Slack](/es/reference/workflow-steps/notifications/notify-via-slack/) o correo electrónico | Escribe mediante destination_bindings en una cuenta de documentos (CSV, TSV, TXT, Excel, Parquet, JSON, Avro, XML, PDF o un .hyper de Tableau, en cualquier juego de caracteres de Java, incluidos los alias, CESU-8 y las formas con marca de orden de bytes; un carácter que el juego de caracteres no tiene se escribe como ?), una tabla de conexión, una hoja de Google, un origen de datos de Tableau o un canal de Slack, o destinatarios de correo electrónico. Un destino sin vincular escribe en su lugar una tabla de proyecto o un archivo de Document (consulte Dónde va más abajo). Un archivo, una subcarpeta o una pestaña por valor de campo divide los archivos CSV, Excel, Parquet y PDF y las pestañas de Hojas de cálculo de Google; una plantilla inicializa cada libro de una división. Las opciones de Excel se asignan así: los valores en blanco van a `Sheet1`, los nombres de hoja que colisionan reciben un sufijo, `formatFromTemplate`, `topLeftCell` y el modo `create`. Append, upsert, update y groupReplace combinan según las claves de coincidencia (se vuelve a leer un archivo o una tabla y se reescribe; una división vuelve a leer el archivo en el que se escribe cada valor de la ejecución y combina dentro de él, sin tocar los demás archivos; Tableau actualiza sus filas en el mismo lugar). Las columnas que solo nombran los datos (las de un encabezado promovido, los valores de un pivote, las claves de un JSON o XML analizado) se escriben junto a las conocidas en todas las exportaciones y escrituras de tablas, se ordenan y se dividen según ellas, y se anexan o combinan en una tabla, o en un archivo que se vuelve a leer con todas sus columnas. |
| Agente Explode (`explode`) | Completo | [Combinación cruzada](/es/reference/workflow-steps/tables/table-cross-join/) | Combina de forma cruzada un lado pequeño con el flujo principal. |
| Agente Filter (`filter`) | Completo | [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con una expresión de filtro | Divide los registros mediante un asistente o una expresión en rutas verdadera y falsa. |
| Filter Pushdown (`pdfilter`) | Completo | [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con una expresión de filtro | Filtro del lado de la base de datos, convertido igual que Filter. |
| Agente Format (`format`) | Completo | [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con cambios de nombre de columna, o Promote Header | Oculta, cambia el tipo, cambia el nombre y rellena los campos que coinciden por nombre (contiene, empieza por, termina en) o por estar vacíos; un relleno escribe su valor predeterminado en cualquier columna a cuyo tipo se pueda convertir el valor predeterminado (texto, número, fecha). La promoción de la fila de encabezado y la coincidencia de vacíos se ejecutan en tiempo de ejecución en el paso Promote Header, y un encabezado promovido lee todas las columnas de su archivo. |
| Agente Fuse (`fuzzy_match`) | Completo | [Fuzzy Match](/es/reference/workflow-steps/tables/table-fuzzy-match/), entre un Union All y dos combinaciones | Apila ambas entradas, hace coincidir los registros por los campos clave con un umbral de similitud de 80 y vuelve a combinar ambos lados con una puntuación de confianza (Confidence Score). |
| Group (`group`) | Completo | Contenedor del lienzo | Se conserva como organización del flujo de trabajo. |
| Agente Infer (`gen_ai`) | Completo | Tarea de instrucciones de [AI/NLP](/es/reference/workflow-steps/text-documents/nlp-ai/) | La instrucción se ejecuta por fila sobre los campos de entrada en la conexión LLM visible que coincide con el proveedor y el modelo de Savant; la respuesta llega a una columna AI Answer junto a cada columna de entrada. rowLimit limita las filas respondidas por ejecución y conserva las respuestas anteriores: una fila respondida antes (misma instrucción, modelo y valores de entrada) conserva su respuesta, y solo las filas sin responder cuentan para el límite. |
| Agente JSON (`json`) | Completo | [Analizar JSON](/es/reference/workflow-steps/tables/table-json-parse/) | Aplana un campo JSON en columnas con claves separadas por puntos, o expande una matriz en una fila por elemento; las claves se leen de los datos en tiempo de ejecución. |
| Agente Notes (`notes`) | Completo | Anotación del lienzo | Se conserva como contexto del flujo de trabajo. |
| Agente Pivot (`pivot`) | Completo | [Pivot](/es/reference/workflow-steps/tables/table-pivot/) | Convierte filas en columnas con agregación. |
| Agente Recursion (`hierarchy`) | Completo | Hierarchy Closure, [Table Extract](/es/reference/workflow-steps/tables/table-extract/) y [Combinación de varias tablas](/es/reference/workflow-steps/tables/table-multi-table-join/) | Recorre un árbol de padres e hijos a cualquier profundidad, agregando cada nodo sobre los identificadores de su ruta hasta la raíz, incluido el propio nodo, y escribiendo Depth y Path; un bucle se detiene en el nodo repetido. |
| Agente Sample (`sample`) | Completo | [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con un límite de filas | Conserva las primeras N filas, opcionalmente por grupo, un porcentaje aleatorio o N filas aleatorias, o una fila de cada N. |
| Buscar y reemplazar (`search_replace`) | Completo | [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con expresiones de reemplazo anidadas, divididas en etapas | Reglas de buscar y reemplazar (contiene o coincide; reemplazar o anexar), con o sin distinción entre mayúsculas y minúsculas, con palabra completa o sin ella, aplicadas en orden sobre los campos de texto elegidos, o sobre todos los campos de texto cuando no se nombra ninguno. |
| Agente Source (`source`) | Completo | Pasos de importación vinculados mediante `source_bindings` ([Importar: CSV](/es/reference/workflow-steps/import/import-csv/), [Importar: Excel](/es/reference/workflow-steps/import/import-excel/), [Importar: SQL](/es/reference/workflow-steps/import/import-sql/)) o una tabla existente | Lee la tabla o el documento vinculado; un origen sin vincular crea una importación vacía y una advertencia. El texto XML lee su documento mediante Importar XML (uno sin vincular lee savant/<workflow>/<name>.xml). Un origen vinculado a un documento XML también escribe las demás columnas de la exportación: una columna de nombre de archivo o de ruta del documento, y el resto en blanco. Un origen situado debajo de un Format que promueve una fila de encabezado lee por posición todas las columnas de su archivo CSV, Excel (incluido Excel 97 .xls), JSON, Parquet o Avro. |
| Agente Spatial Match (`spatial_match`) | Completo | [Coincidencia espacial (ejecutor)](/es/reference/workflow-steps/spatial/spatial-match-executor/), [Combinación cruzada](/es/reference/workflow-steps/tables/table-cross-join/) o [Buscar el más cercano](/es/reference/workflow-steps/spatial/spatial-find-nearest/) | Coincidencias de tipo intersects, within, contains, touches, crosses, overlaps, equals, disjoint y de varias reglas con and/or, dentro de una distancia geodésica entre cualquier geometría (puntos, líneas, polígonos: la distancia mínima sobre una esfera de 6371 km), los N más cercanos por esa misma distancia con una distancia máxima (una única regla de más cercano no escribe ninguna columna Distance, igual que Savant; combinada con otras reglas como más cercano y luego filtro, las combinaciones AND y las uniones OR, cada regla de más cercano agrega su propia columna Distance), y Cross, con flujos coincidentes y sin coincidencia. |
| Agente Spatial Summarize (`spatial_summarize`) | Completo | [Combinación espacial](/es/reference/workflow-steps/spatial/spatial-combine/), Spatial Centroid y pasos de punto a línea | Unión, intersección, cuadro delimitador, uno o varios centros geométricos, y construcciones de polilínea o polígono, por grupo con una ordenación opcional. |
| Agente Split (`split`) | Completo | Split Text, o [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con columnas split_part | Divide un campo de texto por un separador literal de cualquier longitud en filas o columnas, con recorte y conservación del original; la cantidad de columnas se lee de los datos en tiempo de ejecución. |
| Dividir la salida (`outlet`) | Completo | Arista del flujo de trabajo | Dirige una salida con nombre a sus consumidores. |
| Agente Stack (`multi_stack`) | Completo | [Union All](/es/reference/workflow-steps/tables/table-union-all/) | Apila cualquier cantidad de entradas por nombre o posición. |
| Agente Summarize (`summarize`) | Completo | [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con agregación | Agrupa y agrega, incluidos primero/último según una ordenación determinista y agregados de ventana por fila (useWindow). |
| Summarize Pushdown (`pdsummarize`) | Completo | [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con agregación | Agregación del lado de la base de datos, convertida igual que Summarize. |
| Text (`text`) | Completo | Anotación del lienzo | Se conserva como contexto del flujo de trabajo. |
| Agente Time Series (`rollup`) | Completo | Agregación de [Table Extract](/es/reference/workflow-steps/tables/table-extract/) sobre una expresión de intervalo de período, Period Spine, [Anticombinación](/es/reference/workflow-steps/tables/table-anti-join/) y [Union All](/es/reference/workflow-steps/tables/table-union-all/) | Resume los registros por períodos de día, semana, mes, trimestre, año o década entre fechas de inicio y fin opcionales, por grupo, excluyendo las fechas NULL y rellenando con ceros los períodos vacíos. |
| Agente Transform (`edit`) | Completo | [Table Extract](/es/reference/workflow-steps/tables/table-extract/) con expresiones de columna | Columnas calculadas, cambios de tipo y cálculos de ventana (lag, lead, suma acumulada, número de fila, relleno hacia delante y hacia atrás), evaluados en orden. Una edición que solo lleva sus pasos compilados se convierte como esos pasos aplicados en orden, cada uno alimentando al siguiente. |
| Agente Unpivot (`unpivot`) | Completo | [Melt](/es/reference/workflow-steps/tables/table-melt/) | Convierte columnas en filas como un par de nombre y valor. |
| Agente Vision (`vision`) | Completo | [Image OCR](/es/reference/workflow-steps/text-documents/image-ocr/) y luego la tarea de instrucciones de [AI/NLP](/es/reference/workflow-steps/text-documents/nlp-ai/) | Cada documento se envía al proveedor como imagen o PDF cuando este acepta ese tipo y tamaño; de lo contrario, se envía su capa de texto del PDF o el texto del OCR; la respuesta a la instrucción llega a una columna AI Answer. |
| Agente XML (`xml`) | Completo | [Análisis de XML](/es/reference/workflow-steps/tables/table-xml-parse/) | Selecciona elementos, extrae valores secundarios y atributos en columnas, o convierte XML a JSON; una ruta simple //a/b se convierte como antes y cualquier otra ruta XPath 1.0 (predicados, pruebas de atributos, comodines, funciones como count(), name() y contains()) se evalúa como XPath, con o sin espacios de nombres según esté escrita. |

Los tipos de nodo de conexión, lienzo y pushdown (Dividir la salida, Group, Text, Filter Pushdown, Summarize Pushdown) son tipos de nodo de Savant sin un artículo propio de agente en el centro de ayuda; cada uno se convierte como el agente al que refleja.

Una credencial en una solicitud del agente API nunca se copia en un paso de flujo de trabajo. Mediante https pasa a una conexión REST; mediante http, sin permiso para escribir conexiones, o en una conversión realizada a través de MCP, se retiene con una advertencia. Es intencional y no reduce el nivel.

Dos límites de destino no reducen el nivel. Unos pocos juegos de caracteres poco comunes (por ejemplo `x-ISCII91` o `JIS_X0212`) no se pueden escribir; el archivo se escribe como UTF-8 y la conversión emite una advertencia. Una publicación en Tableau que combina por claves necesita `replace: true` en su vinculación de destino; sin ella, la conversión emite una advertencia y publica un nuevo origen de datos, lo que falla en una ejecución en la que ya existe uno.

## Rechazos con nombre

Ocho construcciones se rechazan por su nombre en lugar de convertirse. Ninguna reduce el nivel de un agente.

| Construcción | Por qué se rechaza |
| --- | --- |
| Una solicitud del agente API que lleva una credencial y toma su host de un campo de entrada | Cada fila podría enviar la credencial a un host elegido por los datos. La solicitud se convierte en un marcador de posición con nombre. Una solicitud sin credencial, y una credencial en un host fijo, sí se convierten. |
| Una edición de Transform sin expresión y sin pasos compilados, como una edición de Copilot que solo tiene su instrucción | No hay nada que convertir: una instrucción no es una fórmula. Una edición con pasos compilados sí se convierte. |
| Una construcción de expresión regular en una expresión de Transform o Filter que PlaidCloud no puede leer: una clase dentro de una clase, una intersección de clases (`&&`) o una propiedad `\p{}` desconocida | El paso se convierte en un marcador de posición con nombre que se rechaza en tiempo de ejecución. |
| Una función de agregado o de ventana en una expresión de Transform o Filter | El propio Savant falla con ella en tiempo de ejecución. Como cálculo de Transform o en un Summarize, sí se convierte. |
| `HASH` en una expresión de Transform o Filter con un algoritmo literal distinto de `md5` o `sha1` | El propio Savant falla con ella (el algoritmo es `md5` o `sha1`). Un algoritmo leído de una columna sí se convierte y da NULL para cualquier otro valor. |
| Una ordenación de destino por una columna que su entrada no incluye | El propio Savant falla con ella en tiempo de ejecución. |
| Un archivo, una subcarpeta, una pestaña o una hoja de cálculo de destino por cada valor de una columna que su entrada no incluye | El propio Savant falla con ella en tiempo de ejecución. |
| Una ruta del agente XML que no es XPath 1.0 | Savant tampoco puede ejecutarla. |

Una URL relativa de API se convierte cuando vincula una URL base o una conexión REST con `api_bindings`; consulte [Vinculaciones en tiempo de conversión](/es/guides/workflows/migrate-savant-analyses/#vinculaciones-en-el-momento-de-la-conversión).

## Lenguaje de expresiones

Las funciones y los operadores de expresión de Savant se convierten en expresiones de PlaidCloud. Nivel: **Completo**. Se convierten todas las funciones y todos los formatos, incluidos `TO_TEXT` con un patrón numérico, un formato conocido solo por fila, fracciones de segundo, tokens de fecha basados en semana, trimestre y zona, años de dos dígitos y construcciones de expresiones regulares de Java. Las funciones GEO_* en cualquier parte de una expresión se ejecutan en pasos espaciales complementarios. Las excepciones son los [rechazos con nombre](#rechazos-con-nombre).

Casos límite conocidos: `TO_DATE` o `TO_DATETIME` con un formato que contiene un literal `[`, `]`, comilla, barra invertida o `^`, sobre texto que se lee como 9999-12-30 o 9999-12-31, que supera la última marca de tiempo que admite el almacén; la conversión emite una advertencia.

## Formatos de exportación

El cargador acepta todas las formas de exportación de Savant (plana, envuelta en modelo, de registro de servidor, sobre de receta, envuelta en matriz, con prefijo BOM y alias de tipo heredados) y las normaliza en un solo modelo. Nivel: **Completo**.

## Parámetros de análisis

Los parámetros de análisis de Savant se convierten en variables del flujo de trabajo, y las referencias a ellos dentro de las configuraciones de nodo se reescriben a la sintaxis de variables de PlaidCloud. Se cargan las formas de parámetros de lista, de diccionario y con alias. Nivel: **Completo**.

Casos límite conocidos: un parámetro cuyo nombre contiene una palabra secreta o cuyo valor parece una credencial se convierte en una variable con un valor en blanco, con una advertencia. Un parámetro que usa un nodo y que la exportación no declara se convierte en una variable con un valor vacío, con una advertencia.

## Conexión con sistemas externos

Los conectores de Savant son destinos de origen y de destino, no pasos, y una exportación no incluye conjuntos de datos ni credenciales. PlaidCloud llega a estos sistemas mediante una conexión y no mediante un nodo en el lienzo.

| Savant | Dónde va en PlaidCloud |
| --- | --- |
| Conector de origen | `source_bindings` asigna el nodo o el conjunto de datos de Savant a una tabla de PlaidCloud o a un archivo de Document, que se lee mediante el paso de importación correspondiente; un origen sin vincular emite una advertencia y no procesa nada |
| Destino: CSV, Excel y otros formatos de archivo | Un paso de exportación ([Exportar: CSV](/es/reference/workflow-steps/export/export-to-csv/), [Exportar: Excel](/es/reference/workflow-steps/export/export-to-excel/), [Export to PDF](/es/reference/workflow-steps/export/export-to-pdf/)) |
| Destino: Hojas de cálculo de Google, Tableau, Slack | [Export to Google Spreadsheet](/es/reference/workflow-steps/export/export-to-google-spreadsheet/), [Publish to Tableau](/es/reference/workflow-steps/export/export-to-tableau/) o [Notify via Slack](/es/reference/workflow-steps/notifications/notify-via-slack/), mediante una conexión que usted vincula con `destination_bindings` |
| Destino: base de datos, almacén o destino SaaS sin vincular (Oracle, base de datos genérica, Looker Studio, NetSuite, SAP, y Hojas de cálculo de Google, Tableau o Slack sin conexión vinculada) | Una tabla de proyecto con el nombre del nodo de destino, con una advertencia que nombra el destino original |
| Destino: sistema de archivos sin vincular (S3, GCS, Box, SFTP, SharePoint, Google Drive, OneDrive) | El archivo, en el tipo de archivo del destino, en una carpeta de Document que refleja la carpeta de destino, con una advertencia. Las credenciales y los tokens para compartir se eliminan de la ruta de la carpeta |
| Destino: correo electrónico sin vincular | Un CSV con una advertencia |
| Destino: vinculación que no se puede usar | Un CSV con una advertencia que nombra el destino original |

La conversión nunca se pone en contacto con el sistema de origen ni de destino.
