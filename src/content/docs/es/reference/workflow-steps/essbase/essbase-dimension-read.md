---
title: "Essbase: leer dimensión"
description: Lea el esquema de una dimensión de Oracle Essbase en la jerarquía principal de una dimensión de PlaidCloud, de nube directa, rechazando por su nombre cualquier miembro compartido, solo de etiqueta, Dynamic Calc o de atributo, y cualquier otra cosa que el esquema no pueda representar.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/essbase-dimension-read.md
---

## Descripción

Lee el esquema de una dimensión de un cubo de Oracle **Essbase** a través de su [conexión de Oracle Essbase](/es/guides/connections/essbase/) y lo carga en la **jerarquía principal** de una dimensión de PlaidCloud.

Este paso aparece en el menú de pasos en **Oracle Essbase**.

El paso accede a Essbase en **nube directa** mediante su API REST: este paso no tiene ruta mediante un agente local ni variante remota.

## Configuración

### Origen de Essbase

| Campo | Obligatorio | Notas |
|---|---|---|
| Conexión | Sí | La [conexión de Oracle Essbase](/es/guides/connections/essbase/) mediante la cual se lee. |
| Aplicación | Sí | La aplicación de Essbase de la que se lee. El selector enumera las aplicaciones que puede ver la cuenta de servicio de la conexión; si la conexión define una aplicación predeterminada, aparece preseleccionada. |
| Cubo (base de datos) | Sí | El cubo de la aplicación elegida del que se lee el esquema. |
| Dimensión | Sí | La dimensión de Essbase cuyo esquema se lee. |

### Dimensión de PlaidCloud de destino

| Campo | Obligatorio | Notas |
|---|---|---|
| Dimensión de destino | Sí | La dimensión de PlaidCloud en la que se carga el esquema. |

## Lo que este paso no puede representar

| Limitación | Qué significa |
|---|---|
| Miembros compartidos | Un miembro compartido reutiliza los datos de otro miembro bajo un segundo elemento principal. Un nodo de dimensión de PlaidCloud tiene exactamente un elemento principal, así que un miembro compartido se rechaza por su nombre en lugar de cargarse como duplicado o descartarse en silencio. Lea la consolidación principal como su propia dimensión de PlaidCloud: el segundo elemento principal de un miembro compartido no se puede representar aquí. |
| Miembros solo de etiqueta | Un miembro solo de etiqueta existe para la navegación y nunca contiene datos propios. Se rechaza por su nombre en lugar de cargarse como un miembro ordinario que nada posterior espera que esté vacío. |
| Miembros Dynamic Calc | El valor de un miembro Dynamic Calc lo calcula Essbase sobre la marcha y nunca se almacena. Este paso lee la estructura del esquema, no datos calculados, así que un miembro Dynamic Calc se rechaza por su nombre en lugar de cargarse como si fuera un miembro almacenado. |
| Dimensiones de atributo | Una dimensión de atributo clasifica miembros de una dimensión base; no es una jerarquía de hechos por sí misma. Leer una se rechaza de plano; lea en su lugar la dimensión base. |
| Operadores de consolidación no representables | Una arista de PlaidCloud lleva un indicador de consolidación (`+`, `-` o `~`). Los operadores `+` y `-` de Essbase se asignan directamente. `*`, `/` y `%` no se pueden representar como un simple signo de consolidación: un miembro que use uno de ellos se rechaza por su nombre en lugar de cargarse con el signo equivocado. |
| Esquemas que superan el límite de miembros | Un esquema de dimensión con más de **5,000 miembros de esquema en total** se rechaza en lugar de cargarse parcialmente, y el error indica tanto el recuento observado como el límite. Lea un nivel menos profundo de la jerarquía, o un subárbol más pequeño, para quedar por debajo del límite. |

## Relacionado

- [Conexión con Oracle Essbase (guía)](/es/guides/connections/essbase/): cree la conexión.
- [Conector de Oracle Essbase](/es/reference/connectors/erp/oracle-essbase/): referencia de los campos de la conexión.
- [Essbase: consultar cubo](/es/reference/workflow-steps/essbase/essbase-query/): ejecute una consulta MDX en vivo contra un cubo, en nube directa.
- [Pasos de Oracle Essbase](/es/reference/workflow-steps/essbase/)
