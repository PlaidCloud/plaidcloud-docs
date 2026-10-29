---
title: FUSE_ENCODING (Lakehouse v1)
description: FUSE_ENCODING devuelve los tipos de codificación aplicados a una columna específica de una tabla.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-encoding.md
---

Devuelve los tipos de codificación aplicados a una columna específica de una tabla. Le ayuda a comprender cómo se comprimen y almacenan los datos en formato nativo dentro de la tabla.

## Sintaxis de SQL

```sql
FUSE_ENCODING('<database_name>', '<table_name>', '<column_name>')
```

La función devuelve un conjunto de resultados con las siguientes columnas:

| Columna           | Tipo de datos    | Descripción                                                                                                                                                                              |
|-------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VALIDITY_SIZE     | Nullable(UInt32) | El tamaño de un valor de mapa de bits que indica si cada fila de la columna tiene un valor no nulo. Este mapa de bits se utiliza para registrar la presencia o ausencia de valores nulos en los datos de la columna. |
| COMPRESSED_SIZE   | UInt32           | El tamaño de los datos de la columna después de la compresión.                                                                                                                           |
| UNCOMPRESSED_SIZE | UInt32           | El tamaño de los datos de la columna antes de aplicar la codificación.                                                                                                                   |
| LEVEL_ONE         | String           | La codificación principal o inicial aplicada a la columna.                                                                                                                               |
| LEVEL_TWO         | Nullable(String) | Un método de codificación secundario o recursivo aplicado a la columna después de la codificación inicial.                                                                               |

## Ejemplos de SQL

```sql
-- Create a table with an integer column 'c' and apply 'Lz4' compression
CREATE TABLE t(c INT) STORAGE_FORMAT = 'native' COMPRESSION = 'lz4';

-- Insert data into the table.
INSERT INTO t SELECT number FROM numbers(2048);

-- Analyze the encoding for column 'c' in table 't'
SELECT LEVEL_ONE, LEVEL_TWO, COUNT(*) 
FROM FUSE_ENCODING('default', 't', 'c') 
GROUP BY LEVEL_ONE, LEVEL_TWO;

level_one   |level_two|count(*)|
------------+---------+--------+
DeltaBitpack|         |       1|

--  Insert 2,048 rows with the value 1 into the table 't'
INSERT INTO t (c)
SELECT 1
FROM numbers(2048);

SELECT LEVEL_ONE, LEVEL_TWO, COUNT(*) 
FROM FUSE_ENCODING('default', 't', 'c') 
GROUP BY LEVEL_ONE, LEVEL_TWO;

level_one   |level_two|count(*)|
------------+---------+--------+
OneValue    |         |       1|
DeltaBitpack|         |       1|
```
