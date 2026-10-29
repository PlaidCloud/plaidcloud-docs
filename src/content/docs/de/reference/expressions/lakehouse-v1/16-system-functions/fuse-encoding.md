---
title: FUSE_ENCODING (Lakehouse v1)
description: FUSE_ENCODING gibt die Kodierungstypen zurück, die auf eine bestimmte Spalte einer Tabelle angewendet wurden.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-encoding.md
---

Gibt die Kodierungstypen zurück, die auf eine bestimmte Spalte einer Tabelle angewendet wurden. Die Funktion hilft Ihnen zu verstehen, wie Daten in der Tabelle komprimiert und in einem nativen Format gespeichert werden.

## SQL-Syntax

```sql
FUSE_ENCODING('<database_name>', '<table_name>', '<column_name>')
```

Die Funktion gibt eine Ergebnismenge mit den folgenden Spalten zurück:

| Spalte            | Datentyp         | Beschreibung                                                                                                                                                                              |
|-------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VALIDITY_SIZE     | Nullable(UInt32) | Die Größe eines Bitmap-Werts, der angibt, ob jede Zeile der Spalte einen Wert ungleich NULL hat. Diese Bitmap dient dazu, das Vorhandensein oder Fehlen von NULL-Werten in den Daten der Spalte zu erfassen. |
| COMPRESSED_SIZE   | UInt32           | Die Größe der Spaltendaten nach der Komprimierung.                                                                                                                                           |
| UNCOMPRESSED_SIZE | UInt32           | Die Größe der Spaltendaten vor der Anwendung der Kodierung.                                                                                                                                    |
| LEVEL_ONE         | String           | Die primäre oder erste auf die Spalte angewendete Kodierung.                                                                                                                                   |
| LEVEL_TWO         | Nullable(String) | Ein sekundäres oder rekursives Kodierungsverfahren, das nach der ersten Kodierung auf die Spalte angewendet wird.                                                                                               |

## SQL-Beispiele

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
