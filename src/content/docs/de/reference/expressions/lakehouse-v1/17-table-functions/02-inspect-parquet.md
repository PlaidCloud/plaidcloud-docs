---
title: INSPECT_PARQUET (Lakehouse v1)
description: INSPECT_PARQUET – Ruft eine Tabelle mit umfassenden Metadaten aus einer bereitgestellten Parquet-Datei ab.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/02-inspect-parquet.md
---

Ruft eine Tabelle mit umfassenden Metadaten aus einer bereitgestellten Parquet-Datei ab, einschließlich der folgenden Spalten:

| Spalte                           | Beschreibung                                                   |
|----------------------------------|----------------------------------------------------------------|
| created_by                       | Die Entität oder Quelle, die die Parquet-Datei erstellt hat    |
| num_columns                      | Die Anzahl der Spalten in der Parquet-Datei                    |
| num_rows                         | Die Gesamtzahl der Zeilen oder Datensätze in der Parquet-Datei |
| num_row_groups                   | Die Anzahl der Zeilengruppen in der Parquet-Datei              |
| serialized_size                  | Die Größe der Parquet-Datei auf dem Datenträger (komprimiert)  |
| max_row_groups_size_compressed   | Die Größe der größten Zeilengruppe (komprimiert)               |
| max_row_groups_size_uncompressed | Die Größe der größten Zeilengruppe (unkomprimiert)             |

## SQL-Syntax

```sql
INSPECT_PARQUET('@<path-to-file>')
```

## SQL-Beispiele

Dieses Beispiel ruft die Metadaten aus einer bereitgestellten Beispiel-Parquet-Datei namens [books.parquet](https://datafuse-1253727613.cos.ap-hongkong.myqcloud.com/data/books.parquet) ab. Die Datei enthält zwei Datensätze:

```text title='books.parquet'
Transaction Processing,Jim Gray,1992
Readings in Database Systems,Michael Stonebraker,2004
```

```sql
-- Show the staged file
LIST @my_internal_stage;

┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│      name     │  size  │        md5       │         last_modified         │      creator     │
├───────────────┼────────┼──────────────────┼───────────────────────────────┼──────────────────┤
│ books.parquet │    998 │ NULL             │ 2023-04-19 19:34:51.303 +0000 │ NULL             │
└──────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve metadata from the staged file
SELECT * FROM INSPECT_PARQUET('@my_internal_stage/books.parquet');

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│             created_by             │ num_columns │ num_rows │ num_row_groups │ serialized_size │ max_row_groups_size_compressed │ max_row_groups_size_uncompressed │
├────────────────────────────────────┼─────────────┼──────────┼────────────────┼─────────────────┼────────────────────────────────┼──────────────────────────────────┤
│ parquet-cpp version 1.5.1-SNAPSHOT │           3 │        2 │              1 │             998 │                            332 │                              320 │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
