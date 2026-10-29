---
title: INSPECT_PARQUET (Lakehouse v1)
description: INSPECT_PARQUET — ステージされた Parquet ファイルから包括的なメタデータのテーブルを取得します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/02-inspect-parquet.md
---

ステージされた Parquet ファイルから、次の列を含む包括的なメタデータのテーブルを取得します。

| 列                           | 説明                                                    |
|----------------------------------|----------------------------------------------------------------|
| created_by                       | Parquet ファイルの作成元のエンティティまたはソース |
| num_columns                      | Parquet ファイル内の列数                      |
| num_rows                         | Parquet ファイル内の行（レコード）の総数        |
| num_row_groups                   | Parquet ファイル内の行グループ数                |
| serialized_size                  | ディスク上の Parquet ファイルのサイズ（圧縮後）              |
| max_row_groups_size_compressed   | 最大の行グループのサイズ（圧縮後）            |
| max_row_groups_size_uncompressed | 最大の行グループのサイズ（非圧縮）               |

## SQL 構文

```sql
INSPECT_PARQUET('@<path-to-file>')
```

## SQL の例

この例では、ステージされたサンプル Parquet ファイル [books.parquet](https://datafuse-1253727613.cos.ap-hongkong.myqcloud.com/data/books.parquet) からメタデータを取得します。このファイルには 2 件のレコードが含まれています。

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
