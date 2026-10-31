---
title: FUSE_ENCODING (Lakehouse v1)
description: FUSE_ENCODING — zwraca typy kodowania zastosowane do wskazanej kolumny tabeli.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-encoding.md
---

Zwraca typy kodowania zastosowane do wskazanej kolumny tabeli. Pomaga zrozumieć, jak dane są kompresowane i przechowywane w formacie natywnym w tabeli.

## Składnia SQL

```sql
FUSE_ENCODING('<database_name>', '<table_name>', '<column_name>')
```

Funkcja zwraca zbiór wyników z następującymi kolumnami:

| Kolumna            | Typ danych        | Opis                                                                                                                                                                              |
|-------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VALIDITY_SIZE     | Nullable(UInt32) | Rozmiar wartości bitmapy wskazującej, czy każdy wiersz w kolumnie ma wartość inną niż null. Ta bitmapa służy do śledzenia obecności lub braku wartości null w danych kolumny. |
| COMPRESSED_SIZE   | UInt32           | Rozmiar danych kolumny po kompresji.                                                                                                                                           |
| UNCOMPRESSED_SIZE | UInt32           | Rozmiar danych kolumny przed zastosowaniem kodowania.                                                                                                                                    |
| LEVEL_ONE         | String           | Podstawowe, początkowe kodowanie zastosowane do kolumny.                                                                                                                                   |
| LEVEL_TWO         | Nullable(String) | Dodatkowa lub rekurencyjna metoda kodowania zastosowana do kolumny po kodowaniu początkowym.                                                                                               |

## Przykłady SQL

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
