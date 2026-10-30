---
title: INSPECT_PARQUET (Lakehouse v1)
description: INSPECT_PARQUET：从暂存的 Parquet 文件中检索包含完整元数据的表。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/02-inspect-parquet.md
---

从暂存的 Parquet 文件中检索包含完整元数据的表，包括以下列：

| 列 | 说明 |
|----------------------------------|----------------------------------------------------------------|
| created_by | 创建该 Parquet 文件的实体或来源 |
| num_columns | Parquet 文件中的列数 |
| num_rows | Parquet 文件中的总行数或记录数 |
| num_row_groups | Parquet 文件中的行组数量 |
| serialized_size | Parquet 文件在磁盘上的大小（压缩后） |
| max_row_groups_size_compressed | 最大行组的大小（压缩后） |
| max_row_groups_size_uncompressed | 最大行组的大小（未压缩） |

## SQL 语法

```sql
INSPECT_PARQUET('@<path-to-file>')
```

## SQL 示例

此示例从名为 [books.parquet](https://datafuse-1253727613.cos.ap-hongkong.myqcloud.com/data/books.parquet) 的暂存示例 Parquet 文件中检索元数据。该文件包含两条记录：

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
