---
title: INSPECT_PARQUET (Lakehouse v1)
description: INSPECT_PARQUET — récupère une table de métadonnées détaillées à partir d'un fichier Parquet placé dans un stage.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/02-inspect-parquet.md
---

Récupère une table de métadonnées détaillées à partir d'un fichier Parquet placé dans un stage, avec les colonnes suivantes :

| Colonne                          | Description                                                    |
|----------------------------------|----------------------------------------------------------------|
| created_by                       | L'entité ou la source à l'origine de la création du fichier Parquet |
| num_columns                      | Le nombre de colonnes du fichier Parquet                       |
| num_rows                         | Le nombre total de lignes ou d'enregistrements du fichier Parquet |
| num_row_groups                   | Le nombre de groupes de lignes du fichier Parquet              |
| serialized_size                  | La taille du fichier Parquet sur le disque (compressé)         |
| max_row_groups_size_compressed   | La taille du plus grand groupe de lignes (compressé)           |
| max_row_groups_size_uncompressed | La taille du plus grand groupe de lignes (non compressé)       |

## Syntaxe SQL

```sql
INSPECT_PARQUET('@<path-to-file>')
```

## Exemples SQL

Cet exemple récupère les métadonnées d'un fichier Parquet d'exemple, [books.parquet](https://datafuse-1253727613.cos.ap-hongkong.myqcloud.com/data/books.parquet), placé dans un stage. Le fichier contient deux enregistrements :

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
