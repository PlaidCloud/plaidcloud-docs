---
title: "TM1: leer dimensión"
description: Lea en una dimensión de PlaidCloud una jerarquía de IBM TM1 / Planning Analytics (elementos, relaciones de elemento principal y secundario, y atributos de elemento), de forma directa en la nube mediante REST.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read.md
---

## Descripción

Lee una jerarquía de una dimensión de IBM **TM1 / Planning Analytics** a través de su [conexión de TM1](/es/guides/connections/tm1/) y la carga en una dimensión de PlaidCloud. Los elementos, las relaciones de elemento principal y secundario, y los atributos de elemento de la jerarquía de TM1 se almacenan primero como filas de elemento principal y secundario en una tabla, y la dimensión de PlaidCloud se crea a partir de esa tabla de ensayo: la misma carga que realiza el paso Dimension Load de PlaidCloud, de modo que una jerarquía de TM1 queda igual que una creada a mano o procedente de cualquier otro origen externo.

Este paso aparece en el menú de pasos en **IBM TM1 / Planning Analytics**.

El paso accede a TM1 **de forma directa en la nube** mediante su API REST, sin intervención de ningún agente local. Consulte [TM1: consultar cubo (agente)](/es/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) para la vía local.

## Configuración

### Origen de TM1

| Campo | Obligatorio | Notas |
|---|---|---|
| Conexión de TM1 | Sí | La [conexión de TM1](/es/guides/connections/tm1/) mediante la que se lee. |
| Entorno | Sí | El entorno de la conexión. |
| Base de datos | Sí | La base de datos (instancia) de TM1 de la que se lee. De forma predeterminada, es la Base de datos predeterminada de la conexión, si se ha definido una. |
| Dimensión de TM1 | Sí | La dimensión de TM1 que se leerá. Se detecta en vivo desde la base de datos conectada o se escribe a mano. |
| Jerarquía de TM1 | No | La jerarquía dentro de la dimensión. Se detecta en vivo una vez elegida una dimensión o se escribe a mano. Déjela en blanco para leer la jerarquía propia (implícita) de la dimensión, a la que TM1 da el nombre de la dimensión. |
| Tabla de ensayo | Sí | La tabla en la que se almacenan las filas sin procesar de elemento principal, elemento secundario y atributos antes de crear la dimensión de PlaidCloud a partir de ella. |

Una vez elegidas una dimensión y una jerarquía, el formulario muestra qué atributos de elemento de TM1 pasarán a ser **alias** de PlaidCloud y cuáles **propiedades**, según el propio tipo de atributo de TM1 (`Alias` frente a `Numeric`/`String`). El propio tipo de TM1 de cada elemento (Numeric, String o Consolidated) también pasa a ser una propiedad, llamada `tm1_element_type`.

### Dimensión de PlaidCloud de destino

| Campo | Obligatorio | Notas |
|---|---|---|
| Especificar la dimensión de forma dinámica | Una de las dos | Nombre de la dimensión de destino, que puede contener tokens `{variable}` que se resuelven en tiempo de ejecución. Seleccionada de forma predeterminada. |
| Usar una dimensión específica | Una de las dos | Elija en su lugar una dimensión de PlaidCloud existente del árbol. |
| Jerarquía alternativa | No | Una clave de jerarquía alternativa de PlaidCloud en la que cargar. Déjela en blanco para cargar la jerarquía principal. |

La carga en una jerarquía alternativa se valida antes de escribir nada: una jerarquía alternativa de PlaidCloud no puede cambiar el elemento principal de un nodo que ya existe en la jerarquía principal de la dimensión, y una jerarquía alternativa de TM1 comparte por definición sus elementos con la jerarquía principal de TM1, por lo que esta es la forma normal de esa opción, no un caso límite. Si el elemento principal de cualquier fila analizada ya existe en la jerarquía principal de la dimensión de destino, el paso falla de inmediato, antes de tocar la tabla de ensayo, y nombra los elementos principales en conflicto.

## Lo que este paso no puede representar

| Limitación | Qué significa |
|---|---|
| Se rechazan los elementos con varios elementos principales | Un nodo de una dimensión de PlaidCloud tiene exactamente un elemento principal por jerarquía. Un elemento de TM1 situado bajo dos consolidaciones de la misma jerarquía no se puede cargar: el paso falla con un error con nombre que enumera todos los elementos infractores y sus elementos principales, en lugar de descartar en silencio el elemento de la primera consolidación. Lea el acumulado alternativo como su propia dimensión de PlaidCloud o resuelva primero en TM1 la doble relación con elementos principales. |
| Las ponderaciones de consolidación solo conservan el signo | Una relación de PlaidCloud lleva un indicador de consolidación (`+`, `-` o `~`), no un coeficiente. La ponderación `0` de TM1 pasa a `~` (el miembro no se acumula en su elemento principal); una ponderación negativa pasa a `-`; una ponderación positiva pasa a `+`; una ponderación ausente (el valor predeterminado de TM1) se trata como `+`. **Una ponderación fraccionaria o multiplicadora (0.5, 2.0) no se puede representar**: pasa a un simple `+` y se pierde el multiplicador. Esto se cuenta y se nombra, no se pasa por alto: la advertencia del paso en la ejecución informa de cuántas relaciones se vieron afectadas y las enumera como `parent -> child (weight)`, por ejemplo `Total Revenue -> Product A (0.5)`, con un máximo de 10 y “(and N more)” a partir de ahí. Una relación raíz (sin elemento principal) se nombra `(root)` en lugar de dejarla en blanco. Una ponderación presente pero no numérica se rechaza de plano en lugar de adivinarla. |
| Sin detección mediada por agente | Este paso es solo directo en la nube; consulte [TM1: consultar cubo (agente)](/es/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) para leer un servidor de TM1 al que la nube no puede llegar. |

## Relacionado

- [Conectarse a TM1 (guía)](/es/guides/connections/tm1/): cree la conexión.
- [Conector de TM1](/es/reference/connectors/rest/tm1/): referencia de los campos de la conexión, incluida la vía del agente local.
- [TM1: consultar cubo](/es/reference/workflow-steps/ibm-planning-analytics/tm1-query/): lea datos de cubo, directo en la nube.
- [TM1: consultar cubo (agente)](/es/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/): lea datos de cubo mediante un agente de PlaidLink local.
- [Dimension Load](/es/reference/workflow-steps/dimensions/dimension-load/): el mismo mecanismo de carga de dimensiones en el que se basa este paso.
- [Pasos de IBM TM1 / Planning Analytics](/es/reference/workflow-steps/ibm-planning-analytics/)
