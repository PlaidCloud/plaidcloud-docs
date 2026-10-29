---
title: Importar Kafka
description: Lea los mensajes de temas de Apache Kafka entre dos desplazamientos en una tabla de PlaidCloud, una fila por mensaje.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/import-kafka.md
---

## Descripción

Lee los mensajes de uno o más temas de Apache Kafka en una tabla de proyecto, una fila por mensaje. El paso lee un rango fijo: desde los desplazamientos iniciales hasta los desplazamientos finales, donde `latest` significa el final de cada partición cuando se inicia el paso. Los mensajes que llegan mientras se ejecuta el paso no se leen. El paso se conecta a Kafka mediante una [conexión de Apache Kafka](/es/reference/connectors/databases/apache-kafka/).

## Origen y destino

| Configuración | Obligatorio | Qué hace |
| --- | --- | --- |
| Conexión de Kafka | Sí | La conexión a través de la cual se lee. |
| Temas | Uno de los dos | Los temas que se leen, uno por línea. |
| Patrón de temas | Uno de los dos | Una expresión regular que selecciona los temas que se leen, y que se usa en lugar de **Temas**. |
| Tabla de destino | Sí | La tabla en la que se guardan los mensajes. |

## Rango de mensajes

| Configuración | Valor predeterminado | Qué hace |
| --- | --- | --- |
| Desplazamientos iniciales | `earliest` | `earliest`, `latest` o JSON que indica un desplazamiento para cada partición, como `{"orders": {"0": 1200, "1": 980}}`. En JSON, `-2` significa earliest y `-1` latest. |
| Desplazamientos finales | `latest` | `latest` o JSON con la misma forma que los desplazamientos iniciales. |
| Límite de mensajes (0 = todos) | `0` | El máximo de mensajes que se leen. `0` lee todos los mensajes del rango. |
| Tiempo de inactividad (segundos) | `10` | La lectura termina tras este número de segundos sin un mensaje nuevo. |
| Límite de tiempo (segundos) | `10800` | El tiempo máximo que puede durar la lectura. |

Los desplazamientos admiten variables de flujo de trabajo escritas como `{name}`.

## Valor del mensaje

| Configuración | Qué hace |
| --- | --- |
| Formato del valor | **JSON**, **Texto** o **Avro**. |
| Esquema de Avro (JSON) | El esquema Avro del valor del mensaje. Obligatorio cuando el formato es **Avro**. |
| Configuración adicional del consumidor (JSON) | Configuración adicional del consumidor de Kafka como objeto JSON, por ejemplo `{"fetch.min.bytes": 1}`. Solo se aceptan los valores de configuración que PlaidCloud permite. |

## Asignación de columnas

Asigne al menos una columna en la pestaña de asignación. Una columna lee una de las partes del mensaje, `key`, `value`, `topic`, `partition`, `offset`, `timestamp`, `timestamp_type` o `headers`, o un campo del valor analizado por su ruta. Este paso no tiene **Inspeccionar origen**, así que introduzca las columnas a mano.

## Relacionado

- [Exportar Kafka](/es/reference/workflow-steps/export/export-kafka/)
- [Conexión de Apache Kafka](/es/reference/connectors/databases/apache-kafka/)
