---
title: Importar MongoDB
description: Lea una colección de MongoDB, o el resultado de una canalización de agregación, en una tabla de PlaidCloud como un paso de flujo de trabajo.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/import-mongodb.md
---

## Descripción

Lee los documentos de una colección de MongoDB en una tabla de proyecto, una fila por documento. Use un filtro para leer solo los documentos que necesita, o una canalización de agregación para remodelarlos en MongoDB antes de que se guarden. El paso se conecta a MongoDB mediante una [conexión de MongoDB](/es/reference/connectors/databases/mongodb/).

## Origen y destino

| Configuración | Obligatorio | Qué hace |
| --- | --- | --- |
| Conexión de MongoDB | Sí | La conexión a través de la cual se lee. |
| Base de datos | No | La base de datos que se lee. Déjela en blanco para usar la **Base de datos predeterminada** de la conexión. |
| Colección | Sí | La colección que se lee. |
| Tabla de destino | Sí | La tabla en la que se guardan los documentos. Debe ser una tabla, no una vista. |

## Consulta

| Configuración | Qué hace |
| --- | --- |
| Filtro (JSON) | Un filtro de consulta de MongoDB como objeto JSON, por ejemplo `{"status": "open"}`. Solo se leen los documentos que coinciden. |
| Canalización de agregación (JSON) | Una canalización de agregación como matriz JSON, por ejemplo `[{"$match": {"status": "open"}}]`. Cuando se define, la colección se agrega en lugar de filtrarse. Se rechaza una canalización con una etapa `$out` o `$merge`, porque escribiría en MongoDB. |
| Límite de filas (0 = todas) | El máximo de documentos que se leen. `0` lee todos. |
| Límite de tiempo (segundos) | Cuánto tiempo puede dedicar MongoDB a la lectura antes de detenerla. |
| Documentos muestreados para las columnas | Cuando el paso no declara columnas, cuántos documentos, empezando por el primero, determinan las columnas y sus tipos: cada campo de nivel superior que contienen se convierte en una columna. El valor predeterminado es 1000. |

El filtro y la canalización admiten variables de flujo de trabajo escritas como `{name}`, por ejemplo `{"region": "{region}"}`. El valor de cada variable se inserta como una única cadena o número JSON, por lo que una variable no puede agregar claves ni operadores a la consulta. Una variable que no está definida detiene el paso con un error que la nombra.

## Asignación de columnas

Asigne cada campo del documento a una columna de la tabla de destino en la pestaña de asignación. Una columna lee el campo del documento que tiene el mismo nombre. Una colección que no existe termina con una advertencia y deja vacía la tabla de destino.

## Relacionado

- [Exportar MongoDB](/es/reference/workflow-steps/export/export-mongodb/)
- [Conexión de MongoDB](/es/reference/connectors/databases/mongodb/)
