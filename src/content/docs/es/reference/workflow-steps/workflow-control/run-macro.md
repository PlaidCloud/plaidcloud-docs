---
title: Macro Run (paso)
description: Invoque un flujo de trabajo de macro como subinvocación aislada con vinculaciones declaradas de puertos de entrada y salida; cada llamada se ejecuta en su propio esquema temporal.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/run-macro.md
---

## Descripción

Invoca un flujo de trabajo de [macro](/es/guides/workflows/create-a-macro/) como una subinvocación con ejecución aislada. A diferencia de [Ejecutar flujo de trabajo](/es/reference/workflow-steps/workflow-control/run-workflow/), cada llamada de Macro Run:

- Recibe un `run_id` nuevo y único.
- Se ejecuta en su propio esquema temporal efímero (`macrorun_<run_id>`) del catálogo del proyecto.
- Vincula las tablas y variables del llamador a los puertos de entrada declarados de la macro en la copia de entrada.
- Copia las tablas de salida declaradas de la macro a los destinos del llamador si la ejecución tiene éxito.
- Siempre elimina el esquema temporal cuando la llamada termina (con éxito, con error o por detención).

Este aislamiento permite llamar a la misma macro de forma simultánea sin riesgo (desde un bucle principal, desde flujos de trabajo independientes que se ejecutan al mismo tiempo o de forma recursiva desde otra macro) sin colisiones de nombres de tablas intermedias entre ejecuciones.

El flujo de trabajo de destino debe estar marcado como macro. Un paso Macro Run que apunta a un flujo de trabajo que no es una macro falla con un mensaje de error claro; a la inversa, un paso [Ejecutar flujo de trabajo](/es/reference/workflow-steps/workflow-control/run-workflow/) o [Workflow Loop](/es/reference/workflow-steps/workflow-control/workflow-loop/) no puede apuntar a una macro (esos pasos no incluyen el ciclo de vida de aislamiento por ejecución).

## Macro que se ejecutará

- **Proyecto**: el proyecto que contiene la macro. En la v1 debe ser el mismo proyecto que el del llamador.
- **Macro**: el flujo de trabajo de macro que se invoca. Una vez seleccionada, los puertos de entrada y salida declarados de la macro rellenan las listas de vinculaciones siguientes.

## Vinculaciones de puertos de entrada

Para cada puerto de entrada declarado en la macro, agregue una vinculación. Las vinculaciones se procesan en dos pasadas: primero las entradas escalares y de dimensiones (escritas en la superposición de variables de la macro con alcance de ejecución) y después las entradas de tabla, de modo que un filtro de una entrada de tabla puede referenciar las entradas escalares.

**Puertos de entrada de tabla:**

- **Origen**: una tabla del llamador (por nombre o id) cuyo contenido se copia en el esquema temporal de la macro con el nombre del puerto.
- **Columnas**: proyección opcional de columnas. Elija un subconjunto y cambie los nombres si es necesario (`source` → `target`); las columnas se entrecomillan y se aplican en la copia de entrada, de modo que solo se materializan las columnas proyectadas.
- **Filtro**: cláusula `WHERE` opcional que se aplica en la copia de entrada. Puede referenciar por nombre las variables de entrada de la macro (resueltas a partir de las vinculaciones escalares anteriores). Por ejemplo, `month = {month}` restringe la copia de entrada a la porción de un mes de una tabla de varios años.

**Puertos de entrada escalares y de dimensiones:**

- **Variable**: el nombre de la variable del lado de la macro que se establece (coincide con un puerto declarado en la macro).
- **Valor**: el valor que se vincula, ya sea un literal o una referencia a una variable del llamador (se resuelve con las variables del llamador antes de escribirse en la superposición de la subinvocación).

## Vinculaciones de puertos de salida

Para cada puerto de salida declarado en la macro, agregue una vinculación que apunte a una tabla de destino del llamador. El destino se crea sobre la marcha si aún no existe. La copia de salida:

- Se realiza después de que la macro termina correctamente (estado `done` o `warn`).
- Se **omite** si la macro se detiene manualmente durante la ejecución (estado `stop`); de lo contrario, las salidas parciales terminarían en silencio en el esquema duradero del llamador.
- La proyección opcional de **columnas** funciona igual que en las vinculaciones de entrada.

## Comportamiento ante errores

| Resultado de la macro   | Efecto en el llamador                                                 |
|-------------------------|-----------------------------------------------------------------------|
| `done` / `warn`         | Las tablas de salida se copian a los destinos del llamador; se elimina el esquema temporal. |
| `stop` (detención manual) | Se omite la copia de salida; se elimina el esquema temporal; se registra una advertencia en el llamador. |
| Error durante la ejecución | El paso Macro Run da error; se elimina el esquema temporal; no se escriben salidas. |

Cuando falla el flujo de trabajo de la macro, el registro del paso Macro Run muestra el mensaje de error propio de la macro (“Child workflow run failed:” seguido del mensaje), de modo que puede ver qué corregir sin abrir la ejecución de la macro.

El esquema temporal siempre se recupera en un bloque `finally`, por lo que una macro que falla o se detiene nunca deja tablas intermedias en el esquema del proyecto.

## Ejemplos

Aún no hay ejemplos…

## Elementos relacionados

- [Crear una macro](/es/guides/workflows/create-a-macro/): declare un flujo de trabajo como macro y defina su contrato de puertos.
- [Ejecutar flujo de trabajo](/es/reference/workflow-steps/workflow-control/run-workflow/): el llamador de subflujos de trabajo sin aislamiento (no puede apuntar a una macro).
