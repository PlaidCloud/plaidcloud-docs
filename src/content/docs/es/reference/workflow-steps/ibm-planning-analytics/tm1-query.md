---
title: "TM1: consultar cubo"
description: Lea datos de cubo de un servidor IBM TM1 / Planning Analytics mediante una vista guardada o MDX, aplique un segmento opcional de punto de vista y guarde el resultado como tabla, directamente desde la nube a través de REST y con vista previa antes de guardar.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-query.md
---

## Descripción

Lee datos de un cubo de IBM **TM1 / Planning Analytics** a través de su [conexión de TM1](/es/guides/connections/tm1/), ya sea ejecutando una **vista** guardada o escribiendo una consulta **MDX**. Un punto de vista (POV) puede fijar miembros de dimensión adicionales más allá de lo que la vista o la consulta MDX ya establecen. El conjunto de celdas devuelto se guarda como una tabla de proyecto, con esquema en lectura: columnas de dimensión más una columna de medida `Value`, creadas a partir de los propios ejes de la consulta.

Este paso aparece en el menú de pasos bajo **IBM TM1 / Planning Analytics**.

El paso se conecta a TM1 **directamente desde la nube** mediante su API REST: no interviene ningún agente local y, por ahora, tampoco hay ninguno disponible para este paso.

## Configuración

### Origen y destino

| Campo | Obligatorio | Notas |
|---|---|---|
| Conexión de TM1 | Sí | La [conexión de TM1](/es/guides/connections/tm1/) a través de la cual se lee. |
| Entorno | Sí | El entorno de la conexión. |
| Base de datos | Sí | La base de datos (instancia) de TM1 que se consulta. Si la conexión tiene una base de datos predeterminada, se usa esa de forma predeterminada. |
| Cubo | Sí | El cubo de TM1 que se consulta. Se detecta en vivo desde la base de datos conectada o se escribe a mano. |
| Tabla de destino | Sí | La tabla de proyecto en la que se guarda el conjunto de celdas devuelto. |

### Segmento

| Campo | Obligatorio | Notas |
|---|---|---|
| Modo de origen | Sí | `By View` (predeterminado) ejecuta una vista de TM1 guardada. `By MDX` ejecuta una consulta MDX sin procesar que usted escribe. |
| Vista | Con By View | La vista de cubo de TM1 guardada que se ejecuta. Se detecta en vivo una vez elegido el cubo o se escribe a mano. |
| MDX | Con By MDX | La consulta MDX que se ejecuta sobre el cubo. |

### Punto de vista

Fije un miembro por dimensión para acotar el segmento más allá de lo que la vista o la consulta MDX ya establecen; resulta útil para una extracción incremental (vea más abajo). Agregue una fila de dimensión, elija la dimensión y escriba el miembro. El valor de un miembro puede ser un literal (`Jan-2026`) o un token `{variable}` que se resuelve a partir de las variables del propio flujo de trabajo en el momento de la ejecución, la misma sustitución que recibe el propio campo MDX. Deje el punto de vista vacío para una lectura simple de una vista o de una consulta MDX. No se admite aplicar un punto de vista junto con `By View`; use `By MDX` si necesita uno.

### Opciones

| Campo | Valor predeterminado | Notas |
|---|---|---|
| Suprimir celdas con cero o vacías | Desactivado | Descarta las celdas cuyo valor es exactamente el número `0` **después** de haberlas obtenido. No ahorra ancho de banda y, en un cubo de planificación donde un `0` registrado es un dato real, lo descarta. Es preferible suprimir los ceros en la propia consulta (`NON EMPTY` en su MDX o la opción de supresión de la propia vista guardada) para que TM1 nunca los calcule. |
| Límite de filas | 250,000 | Limita el número de celdas devueltas. Déjelo en blanco para usar el límite predeterminado de 250,000; auméntelo o redúzcalo de forma explícita: un Límite de filas sin definir no es ilimitado. Una consulta que supera el límite efectivo se rechaza en lugar de truncarse en silencio. |

## Extracciones incrementales

TM1 no tiene seguimiento de cambios integrado, por lo que no existe una llamada del tipo “dame solo lo que cambió desde la última vez”. En su lugar, el patrón consiste en **segmentar por período (o versión)** en cada ejecución: fije `Period` en el punto de vista a una variable de flujo de trabajo `{period}` en lugar de a un nombre de miembro literal, de modo que cada ejecución sustituya el período de destino propio y obtenga los datos de un solo período en lugar de todo el cubo. Combínelo con un flujo de trabajo programado y una variable que avance en cada ejecución para construir un historial incremental período a período.

## Vista previa

Antes de guardar, **Vista previa** ejecuta el segmento actual en TM1 y muestra las primeras filas y un recuento de celdas, limitado a un número reducido de filas, independientemente del Límite de filas configurado en el propio paso.

## Cuando Value se guarda como texto

Una dimensión de medidas de TM1 suele contener elementos numéricos (`Sales`, `Cost`) junto con elementos de tipo cadena (`Comment`, `Status`) en la misma dimensión. Un segmento que abarca ambos guarda la columna `Value` como texto: una columna tiene un único tipo físico y basta una sola celda no numérica en el segmento para decidirlo.

Este es el tratamiento correcto: convertir las celdas de cadena en nulos haría perder datos, hacer fallar la consulta bloquearía un cubo legítimo y dividir en dos columnas haría que el esquema dependiera de los datos devueltos. Lo que hace el paso es avisarlo. Emite una advertencia que indica la columna, la escala y los elementos responsables, por ejemplo:

> Column Value landed as text: 3 of 4,812 cells are non-numeric (text or boolean), and a column can only have one type. The non-numeric cells come from element Comment. Exclude that element from the slice, or query it separately, to keep this column numeric.

**Vista previa** muestra el mismo detalle antes de guardar, y el selector de miembros del punto de vista indica el tipo de TM1 de cada elemento (Numeric, String o Consolidated) para que un elemento de tipo cadena sea visible antes de fijarlo. No se impide fijar un elemento de tipo cadena en el punto de vista, ya que es una forma legítima de leer una medida de texto, pero al hacerlo toda la columna `Value` se guarda como texto, porque la medida está en el POV y no en un eje; en ese caso la advertencia informa de los recuentos sin nombrar ningún elemento, porque todos los miembros de los ejes son igualmente no numéricos y ninguno distingue el segmento.

Para mantener `Value` numérica, excluya el elemento de tipo cadena del segmento o consulte por separado las medidas de tipo cadena y las numéricas.

## Límites de capacidad

| Limitación | Qué significa |
|---|---|
| Solo lectura | Lee datos de cubo de TM1. Sin escritura de vuelta ni ejecución de procesos TI. |
| Solo directo desde la nube | Todavía no hay una ruta de agente PlaidLink local para este paso: el servidor de TM1 necesita una ruta de red a la que PlaidCloud pueda acceder directamente. |
| Sin seguimiento de cambios | TM1 no ofrece una API de deltas ni de cambios desde una fecha. En su lugar, segmente por período o versión en cada ejecución (vea Extracciones incrementales más arriba). |
| Sin importación de dimensiones ni jerarquías | Este paso lee datos de cubo. Todavía no es posible importar jerarquías de dimensiones de TM1 como dimensiones de PlaidCloud. |

## Relacionado

- [Conectar con TM1 (guía)](/es/guides/connections/tm1/): cree la conexión y construya una consulta.
- [Conector de TM1](/es/reference/connectors/rest/tm1/): referencia de los campos de la conexión.
- [Pasos de IBM TM1 / Planning Analytics](/es/reference/workflow-steps/ibm-planning-analytics/)
