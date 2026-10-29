---
title: Exportar MongoDB
description: Escriba una tabla de PlaidCloud en una colección de MongoDB como documentos insertados, reemplazados, actualizados o con upsert.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-mongodb.md
---

## Descripción

Escribe cada fila de una tabla de proyecto en una colección de MongoDB como un documento. La colección se crea si no existe. El paso accede a MongoDB mediante una [conexión de MongoDB](/es/reference/connectors/databases/mongodb/).

## Origen y destino

| Configuración | Obligatoria | Qué hace |
| --- | --- | --- |
| Tabla de origen | Sí | La tabla que se escribe. |
| Conexión de MongoDB | Sí | La conexión mediante la cual se escribe. |
| Base de datos | No | La base de datos en la que se escribe. Déjela en blanco para usar la **Base de datos predeterminada** de la conexión. |
| Colección | Sí | La colección en la que se escribe. |

## Opciones de escritura

| Configuración | Qué hace |
| --- | --- |
| Modo de escritura | **Insertar un documento por fila** (el valor predeterminado), **Reemplazar el documento coincidente**, **Actualizar los campos del documento coincidente**, **Reemplazar el documento coincidente o insertar**, o **Actualizar los campos del documento coincidente o insertar**. |
| Columnas de coincidencia | Las columnas, separadas por comas, que identifican un documento. Obligatorias en todos los modos excepto insertar. |
| Eliminar todos los documentos de la colección antes de escribir | Vacía primero la colección, de modo que contenga solo las filas de esta ejecución. |
| Detenerse en la primera escritura fallida | Se detiene en el primer documento que MongoDB rechaza. Desmárquelo para continuar con el resto. |
| Esperar a que la escritura llegue al diario | Espera hasta que MongoDB haya escrito cada lote en su diario. |
| Write Concern | En blanco para el de la conexión, un número de servidores o `majority`. |
| Documentos por solicitud | Cuántos documentos se envían en cada solicitud. |

Insertar vuelve a agregar los documentos cada vez que se ejecuta el paso. Los modos que reemplazan o actualizan dejan la colección igual sin importar cuántas veces se ejecute el paso, así que use uno de ellos cuando un flujo de trabajo pueda ejecutarse dos veces sobre las mismas filas.

## Relacionado

- [Importar MongoDB](/es/reference/workflow-steps/import/import-mongodb/)
- [Conexión de MongoDB](/es/reference/connectors/databases/mongodb/)
