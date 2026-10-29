---
title: Solicitud REST
description: "Llame a una API REST en un paso de flujo de trabajo: importe puntos de conexión desde Postman, OpenAPI o HAR y dirija la respuesta a una tabla o a variables del flujo de trabajo."
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/rest-request.md
---

## Descripción

El paso **Solicitud REST** llama a una API REST y dirige la respuesta a una tabla de destino o a variables del flujo de trabajo. Reemplaza a los pasos anteriores de estilo REST con un único paso unificado al estilo de Postman: elija un punto de conexión (manual, Postman, OpenAPI/Swagger o HAR), edite los encabezados, la consulta y el cuerpo, envíe una solicitud de prueba y guarde.

Para ver un recorrido completo, consulte la [guía del paso Solicitud REST](/es/guides/workflows/rest-request-step/).

Mientras edita, el navegador conserva un borrador local del paso. Si cierra o recarga la página antes de guardar, al volver a abrir el paso se le ofrece restaurar ese borrador sin guardar.

## Configuración

### Solicitud

* **Origen de puntos de conexión**: `Manual`, `From the connection's API definition`, `Postman collection (file/URL)`, `OpenAPI / Swagger (URL/file)` o `HAR archive (file)`. Use **Cargar catálogo** para enumerar los puntos de conexión de un origen importado; al elegir uno se rellenan su método, URL, encabezados, parámetros de consulta y cuerpo, y antes se le pregunta si ha editado la solicitud. Los tres orígenes de archivo también ofrecen **Pegar…**, que le permite proporcionar directamente la colección o la especificación en lugar de elegir un archivo.
* **Conexión** *(opcional)*: una conexión REST para la autenticación y la URL base; omítala para llamar directamente a una URL completa. El acceso directo de edición junto al selector abre el editor de la conexión seleccionada para verla o editarla.
* **Método**: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`.
* **Punto de conexión**: la ruta (con una conexión) o la URL completa.
* **Encabezados** / **Parámetros de consulta**: filas de nombre/valor con un conmutador de activado/desactivado.
* **Cuerpo**: la carga de la solicitud (JSON, formulario o sin formato).
* **Enviar solicitud de prueba** / **Copiar como curl** / **Importar desde curl**: envían la solicitud y permiten inspeccionar la respuesta en el mismo lugar; copian un comando curl equivalente (con los secretos enmascarados); o permiten pegar un comando curl para rellenar el método, la URL, los encabezados y el cuerpo.
* **Enviar**: `One request` (predeterminado) o `One request per table row` para repartir la solicitud sobre una tabla de inductores.

Guardar cambios de la solicitud saliente antes de una **Enviar solicitud de prueba** correcta pide confirmación. En el modo de reparto, **Probar fila 1** es la prueba correcta que elimina la advertencia.

Cuando **Enviar** es `One request per table row`, elija una **Tabla de inductores** (con el selector de tablas o escribiendo un nombre) y use tokens `{{row.column}}` en el punto de conexión, la consulta, los encabezados o el cuerpo para sustituir los valores de cada fila. Los menús de inserción de variables del punto de conexión y del cuerpo incluyen las columnas de la tabla de inductores seleccionada. Opcionales: **Filtro de inductor** (una cláusula SQL `WHERE`), **Columnas clave** (que se trasladan a cada fila de salida), **Límite de filas**, **Simultaneidad**, **Máx. solicitudes/s** (límite de la rapidez con la que se inician las solicitudes en todos los trabajadores, independiente de la simultaneidad; admite fracciones, de modo que 0.5 envía una solicitud cada dos segundos; 0 = sin límite; un valor superior a 1000 se limita a 1000 con una advertencia), **Add Idempotency-Key header** (envía un `Idempotency-Key` estable por fila en un único POST/PUT/PATCH sin paginación para que las reejecuciones no creen duplicados; en caso contrario se omite con una advertencia) y **Continue on error** (registra una fila fallida y advierte en lugar de abortar), y **Respuesta** (`Parsed records` de forma predeterminada; `Text (one row per request)` escribe cada respuesta como una fila con las columnas `DownloadData` y `DownloadHeaders`; `Raw text, errors as rows` hace lo mismo con el cuerpo exactamente como lo envió el servidor, agrega una columna `DownloadStatus` y conserva como fila un error HTTP o de transporte, con las credenciales enmascaradas en el cuerpo, los encabezados y el texto del error). **Probar fila 1** envía la solicitud para la primera fila de inductores a fin de que pueda obtener una vista previa del reparto antes de ejecutarlo. El reparto escribe en la tabla de destino; no puede capturar en variables.

Con **Respuesta** establecida en `Text (one row per request)`, se aplican dos opciones de reparto más:

* **Cuerpo de la respuesta**: `As returned` (predeterminado); `Visible page text` escribe en `DownloadData` el texto visible de una página HTML en lugar de su marcado; y `Raw bytes (Base64)` escribe los bytes del cuerpo exactamente como los envió el servidor, codificados en base64, para un archivo u otra respuesta binaria.
* **Seguir consultando mientras la respuesta coincida**: para una API que responde “aún en curso” hasta que termina un trabajo. Indique una **Ruta de la respuesta** (`$` para toda la respuesta, y después `.name`, `[0]`, `['name']` o `["name"]`), un operador (`==`, `!=`, `<`, `<=`, `>` o `>=`) y un valor con su tipo (`Text`, `Number`, `True/False` o `Empty`). La solicitud de cada fila se vuelve a enviar mientras su respuesta coincida, cada **N seconds** (de 1 a 600, 5 de forma predeterminada) hasta **M requests per row** (de 1 a 1000, 60 de forma predeterminada); una fila que sigue coincidiendo tras la última solicitud falla.

Para enviar contenido binario, como un archivo o audio almacenado como texto base64 en una columna, active **El cuerpo es texto base64: enviar los bytes decodificados** (`body_base64`). Con una solicitud por fila de tabla, el cuerpo, una vez rellenados sus tokens `{{row.column}}`, se lee como texto base64 y se envían los bytes que resultan de decodificarlo.

Las secciones **Opciones de respuesta de texto** e **Inicio de sesión, proxy y TLS** tienen estos campos. Los flujos de trabajo de KNIME convertidos también los usan.

Con una solicitud por fila de tabla y **Respuesta** establecida en `Text (one row per request)`:

* **Añadir el estado HTTP de cada respuesta como columna DownloadStatus** (`include_status`): añade el estado HTTP de cada respuesta como columna `DownloadStatus`. **Columna de estado** (`status_column`) da nombre a esa columna en su lugar, y al establecerla se añade la columna.
* **Conservar la fila de una solicitud fallida, con DownloadStatus y DownloadError** (`keep_error_rows`): una solicitud fallida conserva su fila, con el cuerpo vacío y `DownloadStatus` y `DownloadError` rellenados.
* **Conservar la fila de una solicitud fallida** (`keep_failed_rows`): una solicitud que respondió HTTP 400 o superior conserva su fila con el estado, los encabezados de la respuesta y el cuerpo del error en `DownloadError`; una solicitud sin respuesta conserva solo sus columnas clave. Un fallo sigue deteniendo el paso cuando **Continue on error** está desactivado. **Hacer fallar el paso según el estado de la respuesta** (`fail_on_status`) enumera las familias de estado, como `5xx`, que hacen fallar el paso; una respuesta de cualquier otra familia se conserva como fila.
* `document` *(se establece con un asistente de IA o con la API REST)*: guarda cada respuesta como un archivo en esta carpeta de Document, `{account, path, file_name}`, donde `file_name` es, de forma predeterminada, el último segmento de la URL. La fila contiene `FilePath` en lugar del cuerpo.
* **Escribir el cuerpo como documento de página web** (`html_document`): escribe cada cuerpo como un documento HTML normalizado (`html`) o su forma XML (`xml`). **Convertir en absolutos los valores relativos de href y src** (`html_absolute_urls`, predeterminado verdadero) convierte en absolutos, respecto de la URL de la solicitud, los valores relativos de `href` y `src`.
* **Tipar la columna de cuerpo según la primera respuesta correcta** (`typed_body`): tipa la columna de cuerpo según la primera respuesta correcta: JSON, texto o binario según su `Content-Type`. Una respuesta posterior de otro tipo, un JSON que no se analiza y un cuerpo vacío quedan como valores ausentes.
* **Añadir una columna por cabecera de respuesta** (`all_headers`): añade una columna de texto por cada cabecera de la respuesta, después de la columna de estado; una cabecera que una respuesta no envió queda como valor ausente.
* **Añadir las cookies de la respuesta (DownloadCookies)** (`cookies`): añade `DownloadCookies`, las cookies de cada respuesta.

Con una solicitud por fila de tabla:

* **Omitir una fila cuya URL no es una URL http(s) absoluta** (`skip_invalid_urls`): una fila cuya URL no es una URL HTTP o HTTPS absoluta no envía ninguna solicitud y no escribe ninguna fila. **Hacer fallar el paso si la URL de una fila no es una URL http(s) absoluta** (`fail_invalid_urls`) hace fallar el paso en su lugar ante una fila así.
* **No enviar una cabecera cuyo valor de fila sea NULL** (`skip_null_headers`): una cabecera cuyo valor `{{row.column}}` es NULL no se envía. **Hacer fallar el paso si el valor de fila de una cabecera es NULL** (`fail_null_headers`) hace fallar el paso en su lugar.
* **Operación SOAP** (`soap`): llama una vez por fila a una operación del WSDL que nombra el punto de conexión: `service`, `port` y `operation` (el primero si están en blanco), `inputs`, que asigna cada parámetro a una columna o a una constante, `outputs`, que nombra los elementos de la respuesta que se escribirán como columnas (una columna por cada elemento hoja si está vacío), y `xml` para añadir el elemento de la respuesta como XML. El WSDL y la dirección del servicio deben ser URL HTTP o HTTPS públicas.

Para cualquier solicitud:

* **Responder a un desafío HTTP Digest** (`digest_auth`): responde a un desafío HTTP Digest con el nombre de usuario y la contraseña de autenticación básica de la conexión. **Responder a un desafío NTLM** (`ntlm_auth`) responde a un desafío NTLM del mismo modo; escriba el nombre de usuario como `DOMAIN\user` para indicar un dominio.
* `proxy`: envía las solicitudes a través de un proxy HTTP o SOCKS, que se establece con **Protocolo del proxy** (`protocol`: `http`, `https`, `socks`, `socks4` o `socks5`), **Host del proxy** (`host`), **Puerto del proxy** (`port`), **Hosts a los que se envía directamente** (patrones de host `excluded`) y **Nombre de usuario del proxy** (`username`). La contraseña es el `proxy_password` de la conexión, que solo se usa cuando el `proxy_host` de la conexión es este host.

Las referencias `{{name}}` a variables del flujo de trabajo (también `{{var.name}}` / `{{project_var.name}}`) se sustituyen en el punto de conexión, los encabezados, los valores de consulta y el cuerpo en tiempo de ejecución. Solo se sustituyen las llaves dobles, por lo que las llaves simples de un cuerpo JSON se dejan tal cual. Las ejecuciones de sensor/webhook también exponen `{{trigger_sensor_id}}`, `{{trigger_sensor_type}}`, `{{trigger_fired_at}}` y `{{trigger_payload_json}}` (vacíos en las ejecuciones no desencadenadas).

El editor resalta los tokens `{{...}}` detectados en el punto de conexión, en las tablas de encabezados y de consulta, y en el editor del cuerpo.

Los **Reintentos** se aplican solo a los métodos idempotentes (GET/HEAD/OPTIONS/DELETE); un POST/PUT/PATCH se envía siempre una sola vez para que un cuerpo no idempotente nunca se reenvíe. **Reintentos** acepta de 0 a 100. **Tiempo de espera (s)** es el límite por solicitud, de 1 a 600 s; las solicitudes de prueba esperan como máximo 300 s. Consulte [Paso Solicitud REST](/es/guides/workflows/rest-request-step/) para ver el filtro del catálogo, pegar y soltar, las herramientas JSON, las advertencias de las solicitudes y los resultados de las pruebas.

### Destino de la respuesta

* **Tabla** *(predeterminado)*: analiza la respuesta y la guarda en la **Tabla de destino** (obligatoria; solo tablas, no vistas). Controles: Formato de fila (`Object` o `Array`; una solicitud por fila de tabla requiere `Object`), Ruta de elementos, Modo de paginación (`No Paging`, `Offset Paging`, `Page Number Paging`, `Next Page URL Paging`, `Cursor Paging` o `Link Header Paging (RFC 5988)`), Parámetros del modo, Rutas del modo, “Dump raw JSON instead of parsing rows”, Reintentos, Tiempo de espera. La pestaña **Selección de datos de la tabla** asigna los campos de la respuesta a columnas; **Inspeccionar origen → Populate** la rellena a partir de una respuesta en vivo, lo cual requiere una conexión y pregunta antes de enviar un método distinto de GET, HEAD u OPTIONS. No se ofrecen Resumir ni Distinto.
* **Variables del flujo de trabajo**: envía una solicitud y establece `{prefix}_status`, `{prefix}_body`, `{prefix}_headers` y `{prefix}_elapsed_ms`. El **Prefijo de variable** debe ser un identificador simple y no puede ser `cloud`, `project`, `model` ni `date`.

## Comportamiento

* En el modo de variables, el paso realiza una sola solicitud; la paginación y el análisis de filas no se aplican.
* Las variables capturadas se referencian más adelante por su nombre, por ejemplo `{my_call_status}`.
