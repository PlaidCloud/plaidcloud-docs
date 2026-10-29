---
title: Exportar Kafka
description: Envíe cada fila de una tabla de PlaidCloud a un tema de Apache Kafka como mensaje.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-kafka.md
---

## Descripción

Envía cada fila de una tabla de proyecto a un tema de Apache Kafka como un mensaje. Un mensaje enviado no se puede retirar, así que volver a ejecutar el paso envía las filas de nuevo. El paso accede a Kafka mediante una [conexión de Apache Kafka](/es/reference/connectors/databases/apache-kafka/).

## Origen y destino

| Configuración | Obligatoria | Qué hace |
| --- | --- | --- |
| Tabla de origen | Sí | La tabla que se envía. |
| Conexión de Kafka | Sí | La conexión mediante la cual se envía. |
| Tema | Sí | El tema al que se envía cada fila. |

## Mensaje

| Configuración | Qué hace |
| --- | --- |
| Columna de clave | La columna cuyo valor es la clave del mensaje. Déjela en blanco para enviar los mensajes sin clave. |
| Columnas de valor | Las columnas, separadas por comas, que forman el valor del mensaje. Déjelo en blanco para enviar todas las columnas. |
| Columna de partición | Una columna de tipo entero que indica la partición de cada mensaje. Déjela en blanco para que Kafka elija. |
| Formato del valor | **JSON**, **Texto** o **Avro**. |
| Esquema Avro (JSON) | El esquema Avro del valor del mensaje. Obligatorio cuando el formato es **Avro**. |

## Entrega

| Configuración | Valor predeterminado | Qué hace |
| --- | --- | --- |
| Espera de entrega (segundos) | `60` | Cuánto espera el paso al final a que Kafka confirme cada mensaje. |
| Límite de tiempo (segundos) | `10800` | El máximo que puede durar el envío. |
| Configuración adicional del productor (JSON) | — | Configuración adicional del productor de Kafka como un objeto JSON, por ejemplo `{"compression.type": "gzip"}`. Solo se aceptan los valores que PlaidCloud permite. |

## Relacionado

- [Importar Kafka](/es/reference/workflow-steps/import/import-kafka/)
- [Conexión de Apache Kafka](/es/reference/connectors/databases/apache-kafka/)
