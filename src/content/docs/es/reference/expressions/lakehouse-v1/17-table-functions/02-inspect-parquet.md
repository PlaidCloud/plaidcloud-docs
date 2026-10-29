---
title: INSPECT_PARQUET (Lakehouse v1)
description: INSPECT_PARQUET — recupera una tabla con metadatos completos de un archivo Parquet almacenado provisionalmente.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/02-inspect-parquet.md
---

Recupera una tabla con metadatos completos de un archivo Parquet almacenado provisionalmente, que incluye las siguientes columnas:

| Columna                          | Descripción                                                    |
|----------------------------------|----------------------------------------------------------------|
| created_by                       | La entidad o el origen que creó el archivo Parquet             |
| num_columns                      | El número de columnas del archivo Parquet                      |
| num_rows                         | El número total de filas o registros del archivo Parquet       |
| num_row_groups                   | El recuento de grupos de filas del archivo Parquet             |
| serialized_size                  | El tamaño del archivo Parquet en disco (comprimido)            |
| max_row_groups_size_compressed   | El tamaño del grupo de filas más grande (comprimido)           |
| max_row_groups_size_uncompressed | El tamaño del grupo de filas más grande (sin comprimir)        |

## Sintaxis SQL

```sql
INSPECT_PARQUET('@<path-to-file>')
```

## Ejemplos de SQL

Este ejemplo recupera los metadatos de un archivo Parquet de muestra almacenado provisionalmente, llamado [books.parquet](https://datafuse-1253727613.cos.ap-hongkong.myqcloud.com/data/books.parquet). El archivo contiene dos registros:

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
