---
title: Conector de TM1
description: Conecte PlaidCloud a un servidor IBM TM1 / Planning Analytics mediante su API REST, con autenticación básica nativa o autenticación de espacio de nombres de CAM, de forma directa desde la nube o a través de un agente PlaidLink local para un servidor al que la nube no puede acceder directamente.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/tm1.md
---

Conecte PlaidCloud a un servidor IBM **TM1 / Planning Analytics** mediante su API REST OData v4 publicada, sin puente JVM ni controlador PAOlap. Lea datos de cubos con [TM1: consultar cubo](/es/reference/workflow-steps/ibm-planning-analytics/tm1-query/) o una jerarquía de dimensión de TM1 con [TM1: leer dimensión](/es/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/), ambos directos desde la nube. Para un servidor TM1 accesible únicamente desde el interior de su propia red, [TM1: consultar cubo (agente)](/es/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) envía la misma lectura a través de un agente PlaidLink instalado.

El tipo de conexión aparece en el selector de conexiones como **IBM Planning Analytics (TM1)**.

## Cómo funciona la autenticación

Hay dos modos de autenticación, que corresponden a los esquemas de inicio de sesión REST propios de TM1:

- **Native**: autenticación HTTP básica con un nombre de usuario y una contraseña de TM1.
- **CAM**: inicio de sesión único de IBM Cognos Access Manager, limitado a un espacio de nombres. La solicitud lleva un encabezado `Authorization: CAMNamespace` construido a partir del nombre de usuario, la contraseña y el espacio de nombres en conjunto, distinto de la autenticación básica simple.

Todavía no hay inicio de sesión con token de portador de PlanningAnalytics-as-a-Service (PAaaS); solo se admiten los dos esquemas de inicio de sesión REST anteriores.

## Configuración

| Campo | Obligatorio | Descripción |
|---|---|---|
| Nombre | Sí | Nombre para mostrar de esta conexión. |
| Host | Sí | El host de la API REST de TM1, por ejemplo `https://tm1-prod.example.com:8010` o una URL de PAaaS. |
| Base de datos predeterminada | No | Un valor de relleno previo, por comodidad, para el campo Base de datos de un paso TM1: consultar cubo. Cada paso puede reemplazarlo. |
| Modo de autenticación | Sí | `Native` (usuario y contraseña de TM1) o `CAM` (SSO de Cognos Access Manager). El valor predeterminado es Native. |
| Nombre de usuario | Sí | La cuenta de TM1 con la que se autentica. |
| Contraseña | Sí | Se almacena cifrada. |
| Espacio de nombres de CAM | Solo con CAM | El espacio de nombres de Cognos Access Manager con el que se autentica. No se usa en modo Native. |
| Verificar certificado SSL | No | Activado de forma predeterminada. Desactívelo solo para un certificado autofirmado conocido en un servidor de prueba. |
| Tiempo de espera (segundos) | No | El valor predeterminado es 30. |

## Prueba de la conexión

**Probar conexión** sondea el singleton `Configuration` del servidor (`GET {host}/api/v1/Configuration`), la llamada autenticada más económica que expone TM1 y que no necesita contexto de base de datos ni de cubo. Una prueba correcta informa del **`ProductVersion`** del servidor, lo que confirma que el host es accesible y que las credenciales se autentican.

## Solo lectura

Este conector es de solo lectura. Lee datos de cubos y jerarquías de dimensiones de TM1; no escribe, no contabiliza ni ejecuta procesos TI de vuelta en TM1.

## Qué puede hacer con la conexión

- **Leer datos de cubos mediante una vista guardada o MDX.** El paso [TM1: consultar cubo](/es/reference/workflow-steps/ibm-planning-analytics/tm1-query/) ejecuta una vista de cubo con nombre o una consulta MDX sin procesar, aplica un segmento opcional de punto de vista y deja el resultado en una tabla.
- **Cargar una jerarquía de TM1 como dimensión de PlaidCloud.** El paso [TM1: leer dimensión](/es/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) lee los elementos, las relaciones de padre e hijo y los atributos de una dimensión, y construye con ellos una dimensión de PlaidCloud.
- **Segmentar por período para una extracción incremental.** TM1 no tiene seguimiento de cambios integrado, por lo que un flujo de trabajo que solo necesita datos nuevos acota la consulta por período o versión; consulte la referencia del paso para ver el patrón.
- **Descubrir cubos, vistas y dimensiones en vivo**, directamente desde la nube. Los selectores de Cubo, Vista y Dimensión del formulario del paso consultan directamente el servidor conectado, de modo que elige nombres reales en lugar de escribirlos a ciegas.
- **Leer un servidor TM1 al que la nube no puede acceder, mediante un agente local.** Consulte [Lectura de TM1 detrás de un firewall](#lectura-de-tm1-detrás-de-un-firewall) más abajo.

## Lectura de TM1 detrás de un firewall

Un servidor TM1 accesible únicamente desde el interior de su propia red (sin punto de conexión público, sin IP en la lista de permitidos y sin VPN hacia PlaidCloud) se alcanza mediante un **agente PlaidLink** instalado en lugar de directamente desde la nube. El paso de flujo de trabajo [TM1: consultar cubo (agente)](/es/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) ejecuta la misma consulta de vista, MDX y punto de vista que TM1: consultar cubo, pero la envía al agente, que accede a TM1 en su red y devuelve el resultado.

Esta ruta requiere:

- **Un agente PlaidLink instalado** en una máquina con acceso de red al servidor TM1. Consulte [Instalar PlaidLink](/es/reference/cli/plaidlink/install/).
- **Una compilación de ese agente que incluya el controlador de TM1.** PlaidCloud comprueba las capacidades que anuncia un agente antes de enviarle una consulta, por lo que una compilación anterior del agente no puede atender solicitudes de TM1 hasta que se vuelva a compilar y a instalar; PlaidLink no se actualiza automáticamente. Consulte [Actualizar PlaidLink](/es/reference/cli/plaidlink/upgrade/).
- **Esta conexión de TM1 compartida con ese agente**, además del acceso de miembros y grupos que ya tenga, desde la lista `Actions > Agents` de la conexión. Consulte [Modelo de seguridad](/es/guides/connections/create-connection/#modelo-de-seguridad).

TM1: consultar cubo (agente) no tiene detección en vivo: un agente solo es accesible durante una ejecución, no mientras el formulario del paso está abierto, por lo que el cubo, la vista y el MDX se escriben a mano y se validan cuando se ejecuta el paso. TM1: leer dimensión es solo directo desde la nube; todavía no tiene una ruta local.

## Limitaciones conocidas

| Limitación | Qué significa |
|---|---|
| Solo lectura | Sin escritura de vuelta ni ejecución de procesos TI. |
| El alcance local es solo de consulta | La ruta del agente PlaidLink local cubre las lecturas de cubos (TM1: consultar cubo (agente)). TM1: leer dimensión todavía no tiene una ruta local; necesita una ruta de red a la que PlaidCloud pueda acceder directamente. |
| La lectura de dimensiones admite una sola jerarquía y un solo padre | Una jerarquía de TM1 con un elemento bajo más de un padre no se puede cargar como dimensión de PlaidCloud, y la magnitud del peso de una consolidación (0,5, 2,0) no se puede representar; solo su signo. Consulte [TM1: leer dimensión](/es/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/#lo-que-este-paso-no-puede-representar). |
| Sin autenticación con token de portador de PAaaS | Solo se admiten las autenticaciones Native (básica) y CAM. |

## Información relacionada

- [Conectar con TM1 (guía)](/es/guides/connections/tm1/): cree la conexión y construya una consulta.
- [TM1: consultar cubo](/es/reference/workflow-steps/ibm-planning-analytics/tm1-query/): lecturas de cubos, directas desde la nube.
- [TM1: consultar cubo (agente)](/es/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/): lecturas de cubos a través de un agente local.
- [TM1: leer dimensión](/es/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/): cargue una jerarquía de TM1 como dimensión de PlaidCloud.
- [Crear y administrar una conexión](/es/guides/connections/create-connection/)
