---
title: "TM1: consultar cubo (agente)"
description: "Lea un segmento de cubo de un servidor IBM TM1 / Planning Analytics local al que la nube no puede llegar directamente: la misma consulta de vista, MDX y punto de vista que TM1: consultar cubo, enviada a través de un agente de PlaidLink instalado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote.md
---

## Descripción

El equivalente local de [TM1: consultar cubo](/es/reference/workflow-steps/ibm-planning-analytics/tm1-query/): la misma lectura (una **vista** guardada o una consulta **MDX** sobre un cubo de TM1, con un segmento opcional de punto de vista (POV), almacenada como tabla de proyecto), enviada a través de un [agente de PlaidLink](/es/reference/cli/plaidlink/) instalado en su red en lugar de llamarse de forma directa en la nube. Use este paso, en lugar de TM1: consultar cubo, cuando el servidor de TM1 solo sea accesible desde dentro de su propia red.

Este paso aparece en el menú de pasos en **IBM TM1 / Planning Analytics**.

## Qué se diferencia de TM1: consultar cubo

| | TM1: consultar cubo | TM1: consultar cubo (agente) |
|---|---|---|
| Transporte | Directo en la nube mediante REST | Enviado a un agente de PlaidLink de su red |
| Campos de configuración | — | Idénticos, más un **Agente** obligatorio |
| Detección de cubos y vistas | En vivo, desde la base de datos conectada | No disponible: escriba los nombres a mano |
| Vista previa antes de guardar | Sí | No disponible |

Todo lo demás (la conexión, la base de datos, la elección de vista o MDX, el segmento de punto de vista, Suprimir celdas con cero o vacías, Límite de filas y el patrón de extracción incremental por período) funciona exactamente como se describe en la página [TM1: consultar cubo](/es/reference/workflow-steps/ibm-planning-analytics/tm1-query/). Solo las diferencias que se indican a continuación son específicas de este paso.

## Configuración

### Origen y destino

| Campo | Obligatorio | Notas |
|---|---|---|
| Agente | Sí | El agente de PlaidLink al que se envía esta lectura. Su compilación debe incluir el controlador de TM1 (consulte [Requisitos](#requisitos) más abajo). |
| Conexión de TM1 | Sí | La [conexión de TM1](/es/guides/connections/tm1/) mediante la que se lee. El selector de conexión no se filtra según el agente seleccionado: comparta la conexión con el agente por separado (vea más abajo). |
| Entorno | Sí | El entorno de la conexión. |
| Base de datos | Sí | La base de datos (instancia) de TM1 que se consulta. |
| Cubo | Sí | El cubo de TM1 que se consulta. Se escribe a mano: este paso no tiene detección en vivo. |
| Tabla de destino | Sí | La tabla de proyecto en la que se almacena el conjunto de celdas devuelto. |

### Segmento y opciones

Los mismos campos que en [TM1: consultar cubo](/es/reference/workflow-steps/ibm-planning-analytics/tm1-query/#segmento): Modo de origen (Por vista / Por MDX), Vista, MDX, Punto de vista, Suprimir celdas con cero o vacías y Límite de filas. Todos se escriben en lugar de detectarse, y todos se validan cuando se ejecuta el paso y no en una vista previa.

## Sin detección mediada por agente

Los selectores de Cubo, Vista y Dimensión de TM1: consultar cubo consultan el servidor conectado en vivo mientras edita el paso. Esa detección en vivo no existe para este paso: solo se puede llegar a un agente durante una ejecución, no mientras hay un formulario abierto en su navegador. El cubo, la vista y el MDX se escriben, y un nombre no reconocido hace fallar la ejecución con un error claro en lugar de fallar en silencio. Por la misma razón no hay botón de **Vista previa**: una vista previa tendría que llegar a TM1, y eso solo puede hacerlo el agente.

## Requisitos

Para leer un servidor de TM1 local se necesita:

- **Un agente de PlaidLink instalado** en una máquina con acceso de red al servidor de TM1. Consulte [Instalar PlaidLink](/es/reference/cli/plaidlink/install/).
- **Una compilación de ese agente que incluya el controlador de TM1.** PlaidCloud comprueba las capacidades que anuncia el agente antes de enviar; un agente cuya compilación sea anterior a esta capacidad no puede atender la solicitud. **PlaidLink no se actualiza automáticamente**: un agente existente debe recompilarse o reinstalarse manualmente para incorporar la compatibilidad con TM1. Consulte [Actualizar PlaidLink](/es/reference/cli/plaidlink/upgrade/).
- **La conexión de TM1 compartida con ese agente**, además del acceso de miembros o grupos que ya tenga; concédalo desde la lista `Actions > Agents` de la conexión. Consulte [Modelo de seguridad](/es/guides/connections/create-connection/#modelo-de-seguridad).

## Relacionado

- [TM1: consultar cubo](/es/reference/workflow-steps/ibm-planning-analytics/tm1-query/): el equivalente directo en la nube que este paso replica.
- [TM1: leer dimensión](/es/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/): carga una jerarquía de TM1 en una dimensión de PlaidCloud, directo en la nube.
- [Conectarse a TM1 (guía)](/es/guides/connections/tm1/): cree la conexión.
- [Conector de TM1](/es/reference/connectors/rest/tm1/): referencia de los campos de la conexión, incluida la vía del agente local.
- [PlaidLink](/es/reference/cli/plaidlink/): instalación y actualización de agentes.
- [Pasos de IBM TM1 / Planning Analytics](/es/reference/workflow-steps/ibm-planning-analytics/)
