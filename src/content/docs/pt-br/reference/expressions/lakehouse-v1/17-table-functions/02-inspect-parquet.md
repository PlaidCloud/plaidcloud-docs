---
title: INSPECT_PARQUET (Lakehouse v1)
description: INSPECT_PARQUET — obtém uma tabela de metadados abrangentes de um arquivo Parquet em stage.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/02-inspect-parquet.md
---

Obtém uma tabela de metadados abrangentes de um arquivo Parquet em stage, incluindo as seguintes colunas:

| Coluna                           | Descrição                                                      |
|----------------------------------|----------------------------------------------------------------|
| created_by                       | A entidade ou origem responsável por criar o arquivo Parquet   |
| num_columns                      | O número de colunas do arquivo Parquet                         |
| num_rows                         | O número total de linhas ou registros do arquivo Parquet       |
| num_row_groups                   | A contagem de grupos de linhas do arquivo Parquet              |
| serialized_size                  | O tamanho do arquivo Parquet em disco (compactado)             |
| max_row_groups_size_compressed   | O tamanho do maior grupo de linhas (compactado)                |
| max_row_groups_size_uncompressed | O tamanho do maior grupo de linhas (descompactado)             |

## Sintaxe SQL

```sql
INSPECT_PARQUET('@<path-to-file>')
```

## Exemplos de SQL

Este exemplo obtém os metadados de um arquivo Parquet de exemplo em stage chamado [books.parquet](https://datafuse-1253727613.cos.ap-hongkong.myqcloud.com/data/books.parquet). O arquivo contém dois registros:

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
