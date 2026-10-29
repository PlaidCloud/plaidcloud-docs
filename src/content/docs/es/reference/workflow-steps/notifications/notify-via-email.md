---
title: Notify Via Email
description: Envíe notificaciones por correo electrónico desde un paso de flujo de trabajo de PlaidCloud con asunto, cuerpo, destinatarios y opciones de archivos adjuntos personalizables.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-email.md
---

## Descripción


Envía notificaciones por correo electrónico. Los mensajes se envían desde la cuenta de correo *[info@tartansolutions.com](mailto:info@tartansolutions.com)*. No se requiere ninguna configuración de salida.



### Direcciones de correo electrónico


Especifique cualquier cantidad de destinatarios de correo electrónico. Los delimitadores aceptados incluyen el punto y coma (;) y la coma (,).



### CC, CCO y Responder a

**CC** (`cc_address`), **CCO** (`bcc_address`) y **Responder a** (`reply_to`) toman direcciones con el mismo formato que los destinatarios y aceptan variables del proyecto y del flujo de trabajo. Los destinatarios en CC y CCO reciben el mismo mensaje, y las respuestas van a la dirección de Responder a. Se aplican a los cuerpos de texto sin formato y a los de plantilla Jinja. Defínalos en **Más opciones de correo** de la pestaña **Mensaje**.

### Un correo por cada fila

En **Más opciones de correo**, defina **Enviar** (`request_source`) como **Un correo por fila de una tabla** (`table`) y elija una **Tabla de inductores** (`driver_table`) para enviar un correo por cada fila de una tabla en lugar de un único correo. **Máximo de filas por correo** (`row_limit`) limita las filas usadas y tiene un valor predeterminado de 10,000. La tabla de inductores debe ser una tabla, no una vista.

Use `{{row.column}}` en las direcciones, el asunto, el mensaje y la ruta del archivo adjunto para rellenar el valor de cada fila. Si la tabla de inductores no tiene una columna indicada, el paso falla. Una fila sin dirección en Para no envía nada para esa fila y el paso termina con una advertencia que la nombra.

Una ruta de archivo adjunto rellenada desde una fila (`{{row.column}}`) debe ser un único archivo existente, nunca una carpeta, de modo que una fila cuya ruta haya salido mal no pueda enviar los archivos de otra persona. Una fila cuyo valor para esa ruta esté vacío, cuya ruta salga de su carpeta con `..` o cuyo archivo no exista se envía sin el archivo adjunto, con una advertencia que nombra la fila. El envío por fila requiere un cuerpo de texto sin formato y no está disponible con un cuerpo de plantilla Jinja.

### Mensaje


Especifique el **Asunto** y el **Cuerpo** como desee.



Tenga en cuenta que tanto las variables del proyecto como las variables del flujo de trabajo están disponibles para usarse con esta transformación, tanto en la línea de asunto como en el cuerpo del mensaje.



Además, se permite código HTML estándar en el cuerpo para personalizar aún más el aspecto de los mensajes de correo electrónico.


### Archivos adjuntos


Adjuntar archivos a los correos electrónicos es muy sencillo. Seleccione un archivo o una carpeta de Documento para adjuntar. Si selecciona una carpeta, el contenido de la carpeta se adjuntará como archivos individuales. La sustitución de variables funciona con las rutas para un mejor control de los archivos adjuntos al enviar correos personalizados.



Para adjuntar varios documentos, marque **Agregar archivo adjunto al correo electrónico** y enumérelos en **Más archivos adjuntos** (`attachments`), dentro de **Más opciones de correo**, cada uno con un **ID de cuenta** y una **Ruta del documento**; se envían junto con el archivo adjunto que seleccione, y una ruta puede usar variables y tokens de fila de la misma manera.

### Prioridad y texto sin formato

En **Más opciones de correo**, **Prioridad** (`priority`) marca el mensaje como **Baja**, **Normal** o **Alta** (`low`, `normal`, `high`), y **Enviar como** (`content_type`) definido como **Texto sin formato** (`text`) envía el cuerpo como texto sin formato en lugar de **HTML** (`html`, el valor predeterminado).

### Cuerpo (plantilla Jinja)


El cuerpo del paso se redacta como una **plantilla Jinja** que se renderiza sobre uno o más **marcos**, y produce un correo HTML enriquecido. Cada marco es una selección de una sola tabla con nombre: un Nombre del marco, una tabla del flujo de trabajo y, opcionalmente, una selección de columnas, un filtro where y una agregación (sin combinaciones). El editor se abre directamente en esta plantilla (la lista de marcos, el cuerpo de la plantilla, una vista previa en vivo y un botón **Enviarme una prueba**), sin alternar entre texto sin formato y plantilla. Un botón **Embellecer** y una paleta de inserción (`render_table(...)` para un marco, `{{ cloud }}`, un bucle for y los filtros de moneda/miles/porcentaje/fecha) ayudan a dar forma a la plantilla.

Haga referencia a cada marco en la plantilla como `frames['<Frame Name>'].rows` y `frames['<Frame Name>'].columns`; una plantilla de un solo marco puede usar `rows` / `columns` de nivel superior, que están vinculados al primer marco. La plantilla es un motor de renderizado independiente y aislado: solo `cloud` se resuelve como un valor del espacio de trabajo, y los tokens heredados `{project}` / `{model}` / `{date}` no se resuelven dentro de ella. Los pasos creados antes de la redacción con Jinja se abren con su cuerpo anterior convertido automáticamente; un cuerpo que no se puede convertir de forma segura permanece en un modo alternativo de texto sin formato y sigue enviándose con la sustitución heredada de `{token}`. Consulte [Enviar notificaciones por correo HTML con plantillas](/es/guides/workflows/notify-email-templates/) para ver las variables de plantilla disponibles, el asistente `render_table`, las etiquetas y los atributos HTML que sobreviven al depurador de correo y cómo migran los cuerpos existentes.



## Ejemplos


En este ejemplo se usan todas las variables del sistema. Además, se usa un poco de HTML para dar formato a la primera línea del cuerpo. Al ejecutar esta transformación, se enviará el siguiente correo electrónico:


* PARA: [info@tartansolutions.com](mailto:info%40tartansolutions.com)
* DE: [info@tartansolutions.com](mailto:info%40tartansolutions.com) (recuerde que todos los mensajes provienen de esta dirección)
* Asunto: DEMO – Workflow Analyze Demo Running
