---
title: Migrar análisis de Savant
description: Convierta la exportación de un análisis de Savant Labs en un flujo de trabajo avanzado de PlaidCloud desde la aplicación Analyze, la API REST o un agente de IA conectado por MCP, vincule sus orígenes y lea el informe de conversión.
sidebar:
  order: 31
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-savant-analyses.md
---

PlaidCloud es un reemplazo directo de Savant. Cada agente, expresión y configuración de Savant se convierte a PlaidCloud y se ejecuta. El convertidor transforma la exportación de un análisis de Savant Labs en un flujo de trabajo avanzado ejecutable: asigna cada agente de Savant a un paso de flujo de trabajo, una variable de proyecto o un objeto del lienzo, conserva el grafo original y devuelve un informe de conversión que nombra todo lo que no pudo convertir.

La conversión lee el archivo de exportación que usted indique y los encabezados de los archivos que vincule a sus orígenes. Nunca se conecta al sistema al que se conecta un origen o destino de Savant.

## Qué crea PlaidCloud

- Cada agente de Savant se convierte en el paso de flujo de trabajo equivalente, conservando las relaciones ascendentes y descendentes. La [matriz de conversión de Savant](/es/reference/savant-conversion-matrix/) enumera cada agente y su nivel de asignación.
- Los parámetros de análisis de Savant se convierten en variables de proyecto, y las referencias a ellos dentro de la configuración de los agentes se reescriben con la sintaxis de variables de PlaidCloud.
- Las notas y los grupos llegan al lienzo como notas y grupos.
- Cada origen se convierte en un paso de importación, o lee una tabla existente, según cómo lo vincule.
- Todos los tipos de agente de Savant se convierten por completo: cada opción tiene una asignación. Una configuración en la que falla el propio Savant o que no documenta llega como un paso marcador de posición con nombre. Consulte [Marcadores de posición para configuraciones sin convertir](#marcadores-de-posición-para-configuraciones-sin-convertir).

## Antes de empezar

1. Exporte el análisis desde Savant con **Export JSON**.
2. Cargue el archivo `.json` en una [cuenta de documentos](/es/guides/documents/adding-accounts/) que usted pueda leer.
3. Elija el proyecto de PlaidCloud que debe recibir el flujo de trabajo. Necesita acceso de escritura a él.
4. Elija una cuenta de documentos y una carpeta base desde las que se leerán los archivos de origen del análisis.

## Convertir un análisis

Convierta desde la aplicación Analyze, la API REST o el catálogo de herramientas de MCP. Las tres opciones usan los mismos campos.

### Aplicación Analyze

1. Abra **Analyze** y elija **Tools → Importar análisis de Savant**.
2. Elija el **Proyecto de destino** y el **Archivo de exportación de Savant (.json)** que cargó en una cuenta de documentos.
3. Seleccione **Cargar orígenes**. La ventana enumera cada nodo de origen de la exportación.
4. Para conectar un origen con datos que ya tenga, selecciónelo y elija **Vincular…**. Elija **Tabla del proyecto** para leer una tabla del proyecto de destino, o **Documento** para leer un archivo de una cuenta de documentos (con un nombre de hoja opcional para Excel). Elija **Desvincular** para quitar una vinculación.
5. En **Directorio de orígenes sin vincular**, elija la cuenta de documentos y la carpeta base desde las que se leen los archivos de los orígenes sin vincular.
6. En **Opciones de conversión**, elija el **Tipo de flujo de trabajo** y si desea **Permitir marcadores de posición sin convertir**. En **Prefijos de objetos**, si lo desea, defina prefijos para flujos de trabajo, pasos y tablas.
7. Seleccione **Convertir**.

Cuando termina la conversión, la ventana muestra el informe de conversión: el nombre del flujo de trabajo y el prefijo de tabla, las advertencias, una tabla con las rutas de documento en las que cargar archivos para los orígenes sin vincular y los pasos que requieren revisión. Si no se puede cargar la lista de orígenes, agregue una fila por cada origen con su ID de nodo y el ID `analyzetable_` de la tabla que se debe vincular.

### Campos

La API REST y la herramienta de MCP usan estos campos.

| Campo | Obligatorio | Qué hace |
| --- | --- | --- |
| `source_account_id` | Sí | Cuenta de documentos que contiene la exportación de Savant. |
| `source_file_path` | Sí | Ruta de la exportación dentro de esa cuenta. |
| `project_id` | Sí | Proyecto en el que se crea el flujo de trabajo. |
| `document_account_id` | Sí | Cuenta de documentos de la que leen los orígenes sin vincular. |
| `document_account_path` | Sí | Carpeta base de esa cuenta para los orígenes sin vincular. Un valor vacío o `/` es la raíz de la cuenta, y se omite una `/` inicial. Se rechazan las rutas con `..` o segmentos que empiezan por punto, llaves, letra de unidad o esquema de URL, o caracteres de control. |
| `workflow_prefix` | No | Prefijo que se agrega a los nombres de los flujos de trabajo. |
| `step_prefix` | No | Prefijo que se agrega a los nombres de los pasos. |
| `table_prefix` | No | Prefijo que se agrega a los nombres de las tablas. De forma predeterminada es el nombre del propio flujo de trabajo. Un prefijo que reutilizaría el nombre de una tabla existente se rechaza antes de crear nada. El prefijo utilizado se devuelve en el informe de conversión. |
| `workflow_type` | No | `advanced` (predeterminado) coloca el grafo en el lienzo DAG. `standard` genera una lista de pasos en serie. |
| `source_bindings` | No | Vincula orígenes a datos existentes. Consulte [Vincular orígenes](#vincular-orígenes). |
| `destination_bindings` | No | Dirige los destinos a una cuenta de documentos, una tabla de conexión, una hoja de Google, un origen de datos de Tableau, un canal de Slack o destinatarios de correo electrónico. Solo REST y MCP. Consulte [Destinos](#destinos). |
| `api_bindings` | No | Indica adónde va la URL relativa de un agente de API: una URL base o una conexión REST. Solo REST y MCP. Consulte [Vincular solicitudes de API](#vincular-solicitudes-de-api). |
| `allow_unconverted_placeholders` | No | Controla lo que hace un marcador de posición en el momento de la ejecución. Consulte [Marcadores de posición para configuraciones sin convertir](#marcadores-de-posición-para-configuraciones-sin-convertir). |

### REST

Envíe los campos como cuerpo JSON a:

```text
POST /rest/v1/analyze/savant/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/savant/quarterly-margin.json",
  "project_id": "<project id>",
  "document_account_id": "<document account id>",
  "document_account_path": "/savant-inputs"
}
```

Para enumerar los nodos de origen de una exportación antes de crear `source_bindings`, envíe `source_account_id` y `source_file_path` a:

```text
POST /rest/v1/analyze/savant/sources
```

Cada entrada de la respuesta contiene el `node_id`, el `name` y el `connector` del origen.

### MCP

Un agente de IA conectado por MCP llama a la herramienta `savant_convert` con los mismos campos. Consulte [Agentes de IA (MCP)](/es/integrations/ai-coding-agents/) para conectar un agente. La herramienta modifica su proyecto, así que revise la llamada antes de aprobarla.

## Vinculaciones en el momento de la conversión

Una exportación de Savant no contiene datos, credenciales ni conexiones, por lo que tres parámetros de conversión la conectan con los suyos. Cada uno es un mapa de un ID o nombre de nodo de Savant a un destino, y una vinculación que usted no pueda usar rechaza toda la conversión antes de que se cree nada.

| Parámetro | Vincula | Sección |
| --- | --- | --- |
| `source_bindings` | Agentes de origen a tablas o archivos | [Vincular orígenes](#vincular-orígenes) |
| `destination_bindings` | Agentes de destino a un archivo, tabla, hoja, origen de datos de Tableau, canal de Slack o correo electrónico | [Destinos](#destinos) |
| `api_bindings` | Agentes de API con una URL relativa a una URL base o una conexión REST | [Vincular solicitudes de API](#vincular-solicitudes-de-api) |

## Vincular orígenes

Una exportación de Savant describe de dónde proceden sus datos, pero no contiene datos ni credenciales. Use `source_bindings` para conectar cada origen con datos que ya tenga en PlaidCloud. La clave es el ID de nodo, el ID de conjunto de datos o el nombre del origen. El valor es uno de estos:

- Un ID `analyzetable_` de una tabla del proyecto de destino. El flujo de trabajo convertido lee esa tabla directamente.
- Un objeto con `account`, `path` y, opcionalmente, `sheet`, para leer un archivo de una cuenta de documentos.

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "Budget": { "account": "<document account id>", "path": "/finance/budget.xlsx", "sheet": "FY27" }
}
```

Se rechaza una vinculación que usted no pueda leer. Una clave que no coincide con ningún origen se notifica como advertencia.

La ruta de un archivo de origen en la exportación puede empezar por `/` o pasar por carpetas con punto inicial, como `.archive`, y se convierte. Un origen que lee XML convierte el texto XML, y un origen de documento XML también incluye las columnas de contexto de archivo de Savant.

### Orígenes sin vincular

Un origen sin vinculación se convierte en un paso de importación que aún no tiene datos, y el informe de conversión incluye una advertencia para él. El paso lee desde:

```text
<document_account_path>/savant/<workflow id>/<source name>.csv
```

Cargue el archivo en esa ruta y ejecute el flujo de trabajo. Hasta que el archivo esté allí, el paso de importación termina con una advertencia y crea una tabla vacía, y el flujo de trabajo continúa.

## Cómo se convierten los agentes

La mayoría de los agentes se convierten en el paso que usted crearía manualmente; la [matriz de conversión de Savant](/es/reference/savant-conversion-matrix/) enumera todos los agentes. Estos agentes requieren una atención especial.

| Agente de Savant | En qué se convierte | Salvedades |
| --- | --- | --- |
| Infer Agent (`gen_ai`, y `service` heredado con un servicio de LLM) | Un paso de [AI/NLP](/es/reference/workflow-steps/text-documents/nlp-ai/) con la tarea **Prompt**. El prompt se ejecuta una vez por fila sobre los campos de entrada, y la respuesta se coloca en una columna **AI Answer** junto a cada columna de entrada. Un límite de filas se convierte en **Máx. de filas**, y un origen vacío genera una advertencia y escribe una tabla vacía. **Max New Rows** responde solo a las filas nuevas y conserva las respuestas de ejecuciones anteriores. | Responde un LLM, por lo que la salida nunca es idéntica byte a byte a la de Savant y puede variar entre ejecuciones. Cada llamada tiene un costo. Consulte [Proveedores de IA](#proveedores-de-ia). Un lote que falla conserva sus filas con una respuesta vacía y genera una advertencia. |
| Vision Agent (`vision`) | Un paso [Document Read Blob](/es/reference/workflow-steps/text-documents/document-blob-extract/), [Image OCR](/es/reference/workflow-steps/text-documents/image-ocr/) y, después, la tarea **Prompt** de AI/NLP. Cada documento se envía al proveedor como imagen o PDF cuando el proveedor acepta ese tipo y tamaño. En caso contrario, el paso envía su capa de texto del PDF o el texto del OCR. | Las mismas salvedades de LLM que el Infer Agent. Los documentos completos salen de PlaidCloud hacia el proveedor, y la conversión genera una advertencia. Los archivos TIFF y BMP se envían como texto de OCR, y no existe una configuración de tamaño máximo de documento. Un documento que no se encuentra se omite y el paso genera una advertencia con su ruta. |
| API Agent (`apiService`, y `service` heredado con un servicio de API) | Un paso [Solicitud REST](/es/reference/workflow-steps/general/rest-request/) que envía una solicitud por fila de entrada, y después una combinación de vuelta que conserva todas las filas de entrada. El cuerpo de la respuesta sin procesar se coloca en una columna de texto, con una columna de estado a su lado. Una cuota por período se convierte en un valor fraccionario de **Máx. solicitudes/s**. Una URL relativa se une a la URL base o a la conexión REST que usted vincule con `api_bindings`. Un host, puerto o ruta que procede de un campo de fila se completa fila por fila. Se siguen la paginación por URL siguiente, por encabezado Link, por desplazamiento y por página, y un valor de paginación (inicio, tamaño de página o nombre de parámetro) puede proceder de un campo de entrada o de un parámetro. | Un método distinto de GET se ejecuta contra el sistema real una vez por cada fila de entrada cada vez que se ejecuta el flujo de trabajo, así que confirme el destino antes de la primera ejecución. Las solicitudes que no son GET no se reintentan automáticamente. Una solicitud fallida permanece como una fila con su estado. Una solicitud que lleva una credencial no puede tomar su host de un campo de fila. Las credenciales se tratan como se describe en [Pasos de API con credenciales](#pasos-de-api-con-credenciales). |
| Recursion Agent (`hierarchy`) | Un paso [Table Hierarchy Closure](/es/reference/workflow-steps/tables/table-hierarchy-closure/) que recorre cada fila por su cadena de elementos principales hasta cualquier profundidad y después agrega cada nodo sobre los ID de su ruta hasta la raíz, incluido él mismo. Escribe Depth y Path. Una fila con un elemento principal en blanco, o que se nombra a sí misma como su elemento principal, es una raíz. | Un bucle en los ID principales se detiene en el nodo repetido y conserva todos los ancestros anteriores a él. Las filas con varios elementos principales conservan cada una sus propios valores. |
| Search and Replace (`search_replace`) | Un paso [Table Extract](/es/reference/workflow-steps/tables/table-extract/) que aplica cada regla en orden a las columnas de texto elegidas, con distinción de mayúsculas y minúsculas o sin ella, palabra completa o no. Cada regla se ejecuta en su modo: reemplazar el texto coincidente, reemplazar toda la celda cuando contiene el texto, reemplazar toda la celda cuando coincide exactamente o anexar a la celda. | Las reglas son texto literal, no patrones. |
| Split (`split`) | Un paso [Table Split Text](/es/reference/workflow-steps/tables/table-split-text/). Divide en columnas o filas con un separador literal de cualquier longitud y decide el número de columnas a partir de los datos cuando se ejecuta el flujo de trabajo. | Ninguna. |
| Time Series (`rollup`) | Un paso Table Extract que agrupa por una expresión de período, con un [Table Period Spine](/es/reference/workflow-steps/tables/table-period-spine/), una antiunión y una unión que rellenan con ceros los períodos sin registros. | Se excluyen los registros con una fecha NULL. La secuencia de períodos se detiene en 100 000 períodos. |
| Format (`format`) | Un paso Table Extract con los cambios de nombre, los cambios de tipo, las columnas ocultas y los rellenos, o un paso [Table Promote Header](/es/reference/workflow-steps/tables/table-promote-header/) para reemplazar los nombres por una fila. | Un relleno en una columna que no es de texto convierte el valor predeterminado al tipo de la columna. Promover un encabezado sobre un origen que no declara columnas lee todas las columnas, de archivos CSV, Excel, XLS, JSON, Parquet y Avro. Consulte [Archivos sin columnas declaradas](#archivos-sin-columnas-declaradas). |
| Spatial Match Agent (`spatial_match`) | Un paso [Coincidencia espacial (ejecutor)](/es/reference/workflow-steps/spatial/spatial-match-executor/) para intersects, within, contains, touches, crosses, overlaps, equals y disjoint, con varias reglas combinadas; Combinación cruzada para una coincidencia cruzada; [Spatial Find Nearest](/es/reference/workflow-steps/spatial/spatial-find-nearest/) para una coincidencia con el más cercano. | Una coincidencia con el más cercano ordena y filtra por distancia ortodrómica, como hace Savant. Una regla del más cercano combinada con otras reglas encuentra primero los registros más cercanos y después aplica las demás reglas: con AND el resultado conserva los registros que cumplen todas las reglas, y con OR une los registros más cercanos con los registros que coinciden con las demás reglas. Una regla del más cercano sin cantidad ni distancia máxima conserva el único registro más cercano. Una coincidencia por distancia también se convierte, en kilómetros cuando la regla no indica unidad, y mide la distancia geodésica entre cualquier geometría, no solo entre puntos. Una geometría que no se puede analizar da NULL o ninguna coincidencia, con una advertencia. |
| Spatial Summarize Agent (`spatial_summarize`) | [Combinación espacial](/es/reference/workflow-steps/spatial/spatial-combine/) para unión, intersección y cuadro delimitador, además de [Spatial Centroid](/es/reference/workflow-steps/spatial/spatial-centroid/), [Spatial Point to Line](/es/reference/workflow-steps/spatial/spatial-point-to-line/) y [Spatial Line to Polygon](/es/reference/workflow-steps/spatial/spatial-line-to-polygon/) para el centro geométrico y la creación de líneas o polígonos. | Un polígono creado con menos de 3 puntos es un polígono vacío. |
| Destination Agent (`destination`) | Un paso de exportación al destino que usted vincule, o una tabla o un archivo del proyecto cuando no lo vincula. Consulte [Destinos](#destinos). | Consulte [Qué sigue siendo limitado](#what-stays-limited). |

`GEO_POINT`, `GEO_TYPE` y `GEO_SPATIAL_DISTANCE` se convierten en expresiones. Una edición cuya expresión completa es otra función `GEO_*`, como `GEO_AREA` o `GEO_UNION`, se convierte en el paso espacial correspondiente, incluido [Spatial Info](/es/reference/workflow-steps/spatial/spatial-info/). La geometría viaja como texto WKT. `GEO_AREA`, `GEO_PERIMETER` y `GEO_SPATIAL_DISTANCE` en millas usan la milla terrestre.

Un origen que lee archivos binarios, como los documentos que lee un agente Vision, se convierte en una extracción de documento del documento vinculado, o del archivo esperado en la ruta de orígenes sin vincular.

## Proveedores de IA

Un agente Infer o Vision se convierte en un paso de AI/NLP que usa una conexión de LLM. El convertidor admite Anthropic, OpenAI, Gemini, Azure OpenAI, Grok y GitHub Models.

- El convertidor elige la conexión del proveedor y el modelo que nombra el agente, entre las conexiones de LLM que el usuario que importa puede ver. Nunca nombra una que el usuario no pueda ver. A través de un asistente de IA (MCP), eso significa las conexiones que puede ver el usuario del asistente.
- Cuando el proveedor no tiene ninguna conexión visible, o el proveedor de Savant no tiene equivalente en PlaidCloud (una API de modelos alojada en la nube o un proveedor con clave propia del espacio de trabajo de Savant), el paso usa la conexión predeterminada del espacio de trabajo si el usuario puede verla. En caso contrario, deja la conexión en blanco y el paso usa la predeterminada del espacio de trabajo cuando se ejecuta. El informe de conversión genera una advertencia en ambos casos, así que elija una conexión en el paso si debe responder una distinta.

## Destinos

Un destino de Savant escribe la tabla que recibe en el destino que usted vincule. Vincule los destinos con `destination_bindings` en el cuerpo REST o en la llamada de MCP. La clave es el ID o el nombre del nodo del destino. La ventana de Analyze no vincula destinos, por lo que un destino convertido allí escribe el resultado sin vincular descrito en [Destinos sin vincular](#destinos-sin-vincular).

| Destino | Vinculación | Resultado |
| --- | --- | --- |
| Cuenta de documentos | `{account, path[, file_name]}` | Un archivo CSV, TSV, TXT, Excel, Parquet, JSON, Avro, XML, PDF o Tableau Hyper, según el tipo de destino. Necesita el permiso de escritura de almacenamiento de documentos en la cuenta. |
| Tabla en una conexión | `{connection, table[, schema, replace]}` | Un paso [Export External Database Tables](/es/reference/workflow-steps/export/export-external-tables/). Necesita permiso de escritura en la conexión. Reemplazar la tabla requiere `replace: true`. |
| Google Sheets | `{connection, spreadsheet_name[, sheet_name, replace]}` o `{connection, spreadsheet_id[, sheet_name, replace]}` | Un paso [Export to Google Spreadsheet](/es/reference/workflow-steps/export/export-to-google-spreadsheet/) en una conexión de Google Sheets. La pestaña es, de forma predeterminada, la que nombra el destino, y en su defecto `Sheet1`. Un destino que reemplaza las filas de la hoja borra la pestaña, por lo que requiere `replace: true`. |
| Tableau | `{account, connection[, path, file_name, replace, datasource_name, tableau_project]}` | Una extracción Hyper de Tableau escrita en la carpeta de la cuenta y, después, un paso [Publish to Tableau](/es/reference/workflow-steps/export/export-to-tableau/) en una [conexión de Tableau](/es/reference/connectors/collaboration/tableau/). Reemplazar el origen de datos, o cambiar sus filas según claves de coincidencia, requiere `replace: true`. |
| Slack | `{connection[, channel]}` | El CSV se escribe en una cuenta de documentos y, después, un paso [Notify via Slack](/es/reference/workflow-steps/notifications/notify-via-slack/) lo carga en el canal. La conexión necesita un token de bot, y el canal debe ser un ID de canal, tomado de la vinculación o, en su defecto, de la exportación. |
| Correo electrónico | `{email_to: [...]}`, y `email_export_recipients: true` para usar también los destinatarios que enumera la exportación | El CSV se envía por correo como archivo adjunto. Necesita permiso de escritura de correo electrónico. |

Una conexión de Sheets, Tableau o Slack se comprueba igual que una conexión de tabla: debe poder verla y tener permiso de escritura en la conexión, o se rechaza la conversión.

### Modos de escritura

- Un destino de archivo o tabla que anexa vuelve a leer el archivo anterior y lo reescribe con las filas nuevas. Nunca sobrescribe.
- Un destino upsert, update o groupReplace hace merge según las claves de coincidencia del destino. Un archivo o tabla se vuelve a leer y se reescribe, y en un origen de datos de Tableau se cambian en su lugar las filas coincidentes.
- Anexar y combinar también funcionan en archivos existentes divididos por valor, sin encabezado (las filas coinciden por posición), archivos de Excel anclados en una celda superior izquierda y archivos con un juego de caracteres distinto de UTF-8. Una división vuelve a leer el archivo en el que se escribe cada valor y combina dentro de él, dejando los demás archivos como están.
- Un destino de Tableau asigna los modos de Savant a los seis modos de [Publish to Tableau](/es/reference/workflow-steps/export/export-to-tableau/#modos): append e insert agregan filas, replace sobrescribe, y upsert, update y groupReplace buscan coincidencias por claves. Un modo que cambia datos existentes publica solo cuando la vinculación indica `replace: true`; de lo contrario, el destino publica un nuevo origen de datos y el informe lo indica.
- Un destino con codificación de salida escribe el archivo en ese juego de caracteres de Java. Un carácter que el juego no tiene se escribe como `?`, como hace Savant. Se aceptan alias de Java, CESU-8 y formas con marca de orden de bytes. Algunos juegos de caracteres poco comunes (por ejemplo `x-ISCII91` o `JIS_X0212`) no se pueden escribir; el archivo se escribe como UTF-8 y el informe genera una advertencia. Una división en un juego de caracteres distinto de UTF-8 convierte la carpeta.
- Los nombres de los archivos exportados deben permanecer dentro de la carpeta vinculada.

### Qué pueden vincular los llamadores de IA

Una conversión mediante un asistente de IA (MCP) vincula las mismas formas, reteniendo estas partes, cada una con una advertencia que nombra la parte:

| Retenido | Qué ocurre en su lugar |
| --- | --- |
| `replace` en una tabla, hoja u origen de datos de Tableau | Un destino que anexa sigue anexando a su tabla u hoja vinculada. Un destino que reemplaza escribe un CSV. Un destino de Tableau publica un nuevo origen de datos. |
| Destinatarios de correo electrónico | Se escribe un CSV en lugar del correo electrónico. |
| Slack | Se escribe un CSV en lugar de la publicación en Slack. |

Convierta desde la aplicación Analyze o la API REST, o inicie sesión usted mismo en lugar de usar un asistente, para vincularlos.

### Destinos sin vincular

Un destino sin vinculación escribe su equivalente en PlaidCloud y genera la advertencia **Destination target unbound**, que nombra el destino original. La conversión nunca se conecta al sistema de destino.

| Destino | Resultado |
| --- | --- |
| Destino de base de datos, almacén de datos o SaaS (Oracle, base de datos genérica, Looker Studio, NetSuite, SAP, y Google Sheets, Tableau o Slack sin conexión vinculada) | Una tabla en el proyecto, con el nombre del nodo de destino. |
| Almacenamiento de archivos (S3, GCS, Box, SFTP, SharePoint, Google Drive, OneDrive) | El archivo, en el tipo de archivo del destino, en una carpeta de documentos bajo la cuenta que usted indicó para los orígenes sin vincular. La carpeta replica la carpeta de destino. Las credenciales y los tokens de uso compartido se eliminan de la ruta. |
| Correo electrónico | Un CSV, en la cuenta de documentos que usted indicó para los orígenes sin vincular. |

La advertencia le indica qué vincular para llegar al destino real. Un destino cuya vinculación no se puede usar escribe un CSV y genera la advertencia **Fallback, target not written**, con el destino original en el mensaje; revise ese CSV antes de confiar en él. Un destino CSV simple escribe su propio archivo.

### Destinos divididos

Un destino que escribe un archivo, una subcarpeta o una pestaña por cada valor de un campo divide archivos CSV, Excel, Parquet y PDF y pestañas de Google Sheets.

- **Parquet y PDF.** Un archivo por valor.
- **Google Sheets.** Una pestaña por valor.
- **Plantilla.** Un libro de plantilla inicializa el libro de cada valor. Si falta la plantilla, se genera una advertencia y el libro se escribe sin ella.
- **Valores NULL.** Un valor de división NULL se escribe en su propio archivo o pestaña, no se descarta.
- **Un campo que la entrada no tiene.** Una división, o una ordenación, por un campo que la entrada no contiene se rechaza por su nombre, porque Savant falla en ese caso.
- **Un `/` o `\` en un valor.** Un valor de división que contiene una barra o una barra invertida no puede ser un nombre de archivo o de pestaña, así que se sanea. Un valor modificado recibe un sufijo fijo de seis caracteres, `-` seguido de los seis primeros caracteres del hash MD5 del valor, colocado antes de la extensión del archivo. Los valores que no requieren cambios conservan su nombre.

### Valores exportados y orden de las filas

- **Números y valores booleanos simples.** Las exportaciones CSV, TSV y TXT escriben los números como números simples y los valores booleanos como `true` y `false`, sin `+00:00` en las marcas de tiempo.
- **Orden de filas estable.** Un destino que ordena escribe el mismo orden de filas en cada ejecución: los empates se resuelven siempre del mismo modo, y las rutas de división y de partes también se ordenan. Los destinos Parquet, Google Sheets, Tableau y de tabla no conservan ningún orden de filas.

### Opciones de Excel

Un destino de Excel asigna estas opciones:

- **Pestaña por valor de campo.** Cada valor del campo se convierte en una hoja. Los valores en blanco van a `Sheet1`, y las hojas cuyos nombres coinciden reciben un sufijo numérico.
- **Formato desde plantilla.** Cada ejecución copia primero `<name>_template.xlsx` de la misma carpeta sobre el libro y después escribe en él, por lo que el libro siempre se reemplaza. Si la plantilla no está, la copia genera una advertencia y el libro se escribe sin ella.
- **Celda superior izquierda.** Las filas se escriben en el libro a partir de esa celda.
- **Modo `create`.** Cada ejecución escribe el archivo según indica el modo de escritura del destino.

## Vincular solicitudes de API

Un agente de API cuya URL es relativa, como `/v2/customers`, no tiene un host al que enviar. Vincule uno con `api_bindings`. La clave es el ID o el nombre del nodo de API, o `*` para todos los nodos de API sin una vinculación propia. El valor es uno de estos:

- Una URL base, como cadena o como `{"base_url": "https://host/path"}`. La URL relativa se une a ella. La URL debe ser `http` o `https` con un host público, y no debe llevar usuario, consulta ni fragmento.
- `{"connection": "<REST connection id>"}`. La solicitud va al host de esa [conexión REST](/es/reference/connectors/rest/generic-rest/) y lleva sus credenciales. Necesita permiso de escritura en la conexión, y la conexión debe ser una conexión REST que usted pueda ver.

```json
"api_bindings": {
  "*": "https://api.example.com/v1",
  "Customers": { "connection": "<REST connection id>" }
}
```

Una clave sin coincidencia es una advertencia, y se rechaza una vinculación que usted no pueda usar. Una URL relativa sin vinculación sigue siendo un marcador de posición con nombre.

Si un asistente de IA (MCP) no tiene permiso de escritura en la conexión, la vinculación de conexión se ignora con una advertencia, y la URL relativa que habría unido sigue siendo un marcador de posición. Vincule una URL base, o convierta desde la aplicación Analyze o la API REST.

Un host, puerto o ruta que procede de un campo de entrada no necesita vinculación. Se completa fila por fila, comprobando cada valor a medida que se usa, y el informe enumera los hosts que puede nombrar una fila. Una solicitud que lleva una credencial no puede tomar su host de un campo de fila: se rechaza enviar una credencial a un host elegido por los datos.

La paginación también se convierte. Una URL de página siguiente en la respuesta, un encabezado `Link`, un desplazamiento y un número de página se convierten cada uno en un modo de paginación del paso [Solicitud REST](/es/reference/workflow-steps/general/rest-request/), que lee todas las páginas. Un valor de paginación puede proceder de un campo de entrada (`{{Field}}`) o de un parámetro (`{{Param}}`), y un valor escrito como texto numérico, como `10.0`, se lee como número.

## Pasos de API con credenciales

Una credencial en los encabezados, la ruta de URL, la consulta o el cuerpo de un agente de API pasa a una conexión REST de PlaidCloud que crea la importación. El paso Solicitud REST hace referencia a esa conexión, de modo que la credencial nunca queda en el paso.

- La respuesta enumera en `connections` las conexiones que la importación creó o reutilizó, y el informe de importación las nombra. Importar el mismo análisis de nuevo reutiliza la misma conexión en lugar de crear otra.
- Las credenciales en la información de usuario de la URL y en los encabezados pasan a los campos de autenticación propios de la conexión o a sus encabezados predeterminados. Los secretos de la ruta, la consulta y el cuerpo se almacenan cifrados en la conexión y se completan en el momento de la ejecución, solo para solicitudes al propio host `https` de esa conexión.
- Un punto de conexión `http://` sin cifrar no se convierte con credenciales. La credencial se omite y el informe de conversión advierte de que no se copió.
- Importar mediante un asistente de IA (MCP) no crea conexiones. Las credenciales se omiten y una advertencia lo indica. Importe desde la aplicación Analyze o la API REST, o agregue la credencial manualmente a una conexión REST y selecciónela en el paso.
- Un usuario sin permiso de escritura en la conexión obtiene el mismo resultado: credenciales omitidas y una advertencia.
- Solo una ranura de credencial de API traslada un parámetro a una conexión. Un parámetro de pipeline usado en un encabezado, una consulta, una ruta o un cuerpo en el lugar donde va una credencial de API pasa a los `secret_values` cifrados de la conexión, y el paso se refiere a él a través de la conexión. Nunca se crea como variable de flujo de trabajo, sea cual sea el nombre del parámetro.
- Cualquier otro parámetro cuyo nombre contenga una palabra secreta (como `password`, `token`, `secret` o `key`, con la excepción de `key` después de una palabra de datos como `sort` o `partition`) se convierte en una variable de flujo de trabajo con un valor en blanco y una advertencia. Un nombre como `api_key_2` también se deja en blanco. Defina el valor en la variable de proyecto después de la importación.
- Un parámetro con nombre de cantidad o límite, como `max_tokens`, conserva su valor.
- Un secreto escrito en una fórmula, un filtro o un valor de reemplazo se omite del paso y el informe de conversión genera una advertencia. Se conservan una ruta, una URL y un resumen hexadecimal de 40 o 64 caracteres, salvo que parte de ellos o un nombre secreto indique lo contrario. Los vínculos para compartir carpetas y las direcciones de correo electrónico de los destinatarios nunca aparecen en advertencias ni notas.
- Una respuesta que devuelve una credencial se almacena tal como se recibe. Trate como confidencial la tabla de salida de una solicitud de este tipo.

## JWT_ENCODE

`JWT_ENCODE` se convierte en un paso [JWT Encode](/es/reference/workflow-steps/tables/table-jwt-encode/). Una clave de firma literal pasa a una conexión dedicada vinculada al paso, y el token se firma en el momento de la ejecución, de modo que la clave nunca aparece en la configuración del paso. Mediante un asistente de IA, o sin permiso de escritura en la conexión, la clave se omite, el token es NULL y una advertencia le indica que debe importar de nuevo con permiso para crear conexiones.

## Promover una fila de datos a encabezados de columna

Un agente Format configurado en **replace names with row** se convierte en un paso [Table Promote Header](/es/reference/workflow-steps/tables/table-promote-header/). En el momento de la ejecución, la fila elegida, contada desde 1, se convierte en los nombres de columna y se elimina. Un origen que no tiene orden de registros recibe una nota, porque la fila que da nombre a las columnas puede cambiar de una ejecución a otra. Una columna que esa fila nombra pero que ningún paso posterior menciona no se arrastra más allá de un paso que enumera las columnas que lee.

## Archivos sin columnas declaradas

Un origen sin columnas declaradas conserva estas columnas:

- Un origen CSV, TSV o TXT vinculado en la importación conserva todas las columnas del encabezado del archivo.
- Cualquier otro tipo de archivo, y cualquier origen sin vincular, conserva solo las columnas que nombran los pasos posteriores, y el informe de conversión genera una advertencia.
- Un encabezado promovido sobre un origen de este tipo lee todas las columnas, de archivos CSV, Excel, XLS, JSON, Parquet y Avro.

Cuando un origen de este tipo alimenta solo un encabezado promovido, la importación es un paso [Import Delimited](/es/reference/workflow-steps/import/import-delimited/) que lee todas las columnas por posición. Un paso que exporta o combina después de un encabezado promovido lleva todas las columnas que tiene la tabla en el momento de la ejecución (consulte **Incluir también columnas nombradas en tiempo de ejecución** en [Table Extract](/es/reference/workflow-steps/tables/table-extract/)).

## Comportamientos que conviene conocer

Estas conversiones se comportan como se indica a continuación.

| Agente | Comportamiento |
| --- | --- |
| Blend (`blend`) | Combina con predicados unidos por OR, contains e is-part-of. Los blends de exterior excluyendo el interior y las salidas sin coincidencia se convierten en los flujos de combinación correspondientes. Para cualquier operador, la clave duplicada del lado derecho se elimina de la salida. |
| Dedupe (`deduplicate`) | Conserva el primer registro por clave dentro de cada grupo de **Agrupar por**. El indicador de duplicados marca a todos los miembros de un grupo duplicado, y los duplicados también pueden dirigirse a un segundo flujo. Con una sola salida conectada, se comporta como Savant. |
| Summarize (`summarize`) | Los agregados de ventana agregan el valor agregado a cada fila en lugar de contraer los grupos. |
| Sample (`sample`) | Las primeras N filas, por grupo o en total, un porcentaje o un número aleatorio de filas, o una fila de cada N. |
| Time Series (`rollup`) | Períodos de día, semana, mes, trimestre, año y década entre las fechas de inicio y fin opcionales, por grupo. Los períodos de mes se etiquetan `YYYY-MM`, y los períodos sin registros aparecen con ceros. Se excluyen los registros con una fecha NULL. |
| Pivot (`pivot`) | COUNT cuenta filas. |
| XML (`xml`) | SELECT extrae elementos, las rutas pueden llevar espacios de nombres, y TO_JSON convierte XML en JSON. Cualquier ruta XPath 1.0 se convierte, incluidos predicados, pruebas de atributos, comodines y funciones como `count()`, `name()` y `contains()`, y el paso [Análisis de XML](/es/reference/workflow-steps/tables/table-xml-parse/) la lee como XPath. Con `processNs` desactivado, los nombres se comparan literalmente, prefijo incluido. Un archivo XML que falta al convertir resuelve su elemento raíz cuando se ejecuta el flujo de trabajo. |
| JSON (`json`) | Se aplana en columnas anchas. El texto que no es JSON válido da NULL, y las matrices salen como texto. |
| Split (`split`) | Divide en columnas o filas, leyendo el número de columnas de los datos cada vez que se ejecuta el flujo de trabajo. |

Estas funciones de expresión siguen los resultados de Savant:

| Función | Comportamiento |
| --- | --- |
| `DATE_DIFF` | Las semanas y los trimestres se cuentan como lo hace Savant. |
| `PAD` | No trunca un valor más largo que el ancho de destino. |
| `+` en texto | Concatena texto. Una columna de un origen sin tipos declarados se lee como número, por lo que `+` suma, y una nota lo indica. |
| Dividir en filas | Conserva las partes vacías como filas. |
| `LAST` sin ordenación | Devuelve la última fila en el orden en que llegan las filas, con una nota de que el almacén de datos no garantiza ese orden. |
| `JOIN_STR` | Une un número fraccionario como lo escribe Savant, sin relleno de ceros finales. |
| `JSON_FORMAT` | Da formato legible al JSON; en Snowflake escribe el JSON compacto en una sola línea. |
| `JSON_SET` | Conserva el orden de claves de Savant. |
| `GREATEST` y `LEAST` | Omiten los argumentos NULL. El resultado es NULL solo cuando todos los argumentos son NULL. |
| `ROUNDUP` | Redondea hacia arriba al siguiente paso entero, por lo que un número negativo se redondea hacia cero: -1,5 pasa a ser -1. `ROUNDDOWN` no cambia. |
| `DURING_DAYLIGHT_SAVING` y `DURING_STANDARD` | Si la entrada es NULL, la salida es NULL. |
| `TO_TEXT` con un formato de fecha | Lee los tokens de formato como lo hace Savant. `YYYY`, `w` y `u` son el año de semana, la semana y el día de la semana ISO, y una letra de zona o de era se escribe como para una hora UTC. |
| `TO_TEXT` y salida de número a texto | Escribe números simples como `12`, no `12.0000000000`. |
| `TO_TEXT` con un patrón numérico | Da formato como lo hace un `DecimalFormat` de Java, redondeando al par más cercano, incluidos los patrones científicos como `##0.##E0`. |
| `TO_TEXT` y análisis de fechas con un formato por fila | Lee el formato de cada fila. |
| Tokens de fecha de fracciones de segundo, de mes estrecho y basados en semanas | Se convierten. Los tokens de semana se leen como semanas ISO. |
| Años de dos dígitos (`yy`, `y`) | Se leen mediante una ventana de 80 años hacia atrás y 20 años hacia delante a partir del año actual. |
| `REGEX_MATCH` | Una coincidencia parcial: el patrón coincide en cualquier parte del texto, no con el texto completo. |

`TO_TEXT` y los formatos de fecha se convierten en un paso [Text Function](/es/reference/workflow-steps/tables/table-text-function/). Una edición que solo lleva sus pasos compilados, sin expresión, se convierte en esos pasos aplicados en orden, alimentando cada uno al siguiente, y el informe de conversión anota el orden que supuso. El convertidor rechaza por su nombre lo que falla en el propio Savant o lo que no tiene nada que convertir, y el paso se convierte en un marcador de posición: una función de agregación o de ventana simple dentro de una expresión de Transform o Filter (dentro de un cálculo o de un Summarize sí se convierte), `HASH` con un algoritmo literal distinto de `md5` o `sha1`, una construcción de expresión regular que PlaidCloud no puede leer (una clase dentro de una clase, una intersección de clases o una propiedad `\p{}` desconocida), una edición de Transform sin expresión ni pasos compilados (como una edición de Copilot que solo tiene su prompt), una ruta XML que no es XPath 1.0 y una solicitud de API que lleva una credencial y toma su host de un campo de fila. La [matriz de conversión de Savant](/es/reference/savant-conversion-matrix/#rechazos-con-nombre) enumera cada una con su motivo.

Las funciones de expresión también se convierten para `sha1`, `NOT_TRUE`, `LEVENSHTEIN`, las funciones de horario de verano (`DST`) y las funciones de expresión regular que toman una n-ésima coincidencia. `DAY_OF_WEEK` numera el domingo como 7, y `DAY_NAME` devuelve el nombre del día.

## Leer el informe de conversión

La respuesta contiene el informe de conversión: un resumen de cuántos pasos se convirtieron con confianza alta, media o baja y cuántos no se convirtieron, además de las advertencias y los nodos que el convertidor absorbió en otros. Léalo antes de ejecutar el flujo de trabajo. Nombra todos los marcadores de posición, todos los orígenes sin vincular y las vinculaciones sin coincidencia, así como el prefijo de tabla utilizado.

## Marcadores de posición para configuraciones sin convertir

Una configuración que el convertidor no puede reproducir se crea como un paso marcador de posición que lleva el nombre del agente, y el informe de conversión lo nombra. Aparece un marcador de posición para una construcción que el convertidor rechaza por su nombre (consulte la [matriz de conversión de Savant](/es/reference/savant-conversion-matrix/#rechazos-con-nombre)) o que la exportación no describe por completo, como una configuración de API ausente. De forma predeterminada, un marcador de posición falla cuando el flujo de trabajo llega a él, de modo que una ejecución no puede notificar éxito por un trabajo que nunca se realizó.

Establezca `allow_unconverted_placeholders` en `true` para importar cada marcador de posición como un paso de paso directo. La ejecución continúa entonces más allá de él y la salida del marcador de posición es su entrada. Recree la funcionalidad con un paso nativo cuando su resultado importe.

## Ejecutar el flujo de trabajo convertido

1. Abra el nuevo flujo de trabajo en el proyecto.
2. Defina las variables de proyecto que procedan de parámetros de Savant.
3. Cargue los archivos de los orígenes sin vincular en las rutas indicadas en el informe.
4. Ejecute el flujo de trabajo y revise la tabla de salida de cada paso.

## Casos límite

Estas son las únicas diferencias conocidas con respecto a Savant. El informe de conversión nombra cada una que se aplica.

- **Formatos de fecha.** `TO_DATE` o `TO_DATETIME` con un formato que contiene un literal `[`, `]`, `'`, `\` o `^`, sobre texto que se lee como 9999-12-30 o 9999-12-31, cae después de la última marca de tiempo que admite el almacén de datos, y el informe genera una advertencia.
- **Parámetros secretos.** Un parámetro cuyo nombre contiene una palabra secreta, o cuyo valor parece una credencial, se convierte en una variable de proyecto con un valor en blanco, por diseño. Defina el valor en la variable.
- **Parámetros no declarados.** Un parámetro que usa un nodo y que la exportación no declara llega como una variable de proyecto con un valor vacío.
- **`JSON_FORMAT` en Snowflake.** Escribe JSON compacto en una sola línea.
- **Orden de las filas.** Los destinos Parquet, Google Sheets, Tableau y de tabla ordenados no conservan ningún orden de filas.
- **Google Sheets y Tableau.** Publicar en cualquiera de ellos requiere que su cuenta esté vinculada mediante `destination_bindings`.

## Guías relacionadas

- [Matriz de conversión de Savant](/es/reference/savant-conversion-matrix/)
- [Conexión REST](/es/reference/connectors/rest/generic-rest/)
- [Agregar cuentas de documentos](/es/guides/documents/adding-accounts/)
- [Administrar variables de flujo de trabajo](/es/guides/workflows/manage-workflow-variables/)
- [Paso AI/NLP](/es/reference/workflow-steps/text-documents/nlp-ai/)
- [Paso Solicitud REST](/es/guides/workflows/rest-request-step/)
- [Ejecutar un flujo de trabajo](/es/guides/workflows/run-a-workflow/)
