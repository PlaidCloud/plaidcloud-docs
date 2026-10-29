---
title: FUSE_TIME_TRAVEL_SIZE（Lakehouse v1）
description: FUSE_TIME_TRAVEL_SIZE — テーブルの履歴データ（タイムトラベル用）のストレージサイズを計算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-time-travel-size.md
---

テーブルの履歴データ（タイムトラベル用）のストレージサイズを計算します。

## SQLの構文

```sql
-- Calculate historical data size for all tables in all databases
SELECT ...
FROM fuse_time_travel_size();

-- Calculate historical data size for all tables in a specified database
SELECT ...
FROM fuse_time_travel_size('<database_name>');

-- Calculate historical data size for a specified table in a specified database
SELECT ...
FROM fuse_time_travel_size('<database_name>', '<table_name>'));
```

## 出力

この関数は、次の列を持つ結果セットを返します。

| 列                           | 説明                                                                                           |
|----------------------------------|-------------------------------------------------------------------------------------------------------|
| `database_name`                  | テーブルが配置されているデータベースの名前。                                                  |
| `table_name`                     | テーブルの名前。                                                                                |
| `is_dropped`                     | テーブルが削除済みかどうかを示します（削除済みのテーブルは `true`、それ以外は `false`）。          |
| `time_travel_size`               | テーブルの履歴データ（タイムトラベル用）の合計ストレージサイズ（バイト単位）。                  |
| `latest_snapshot_size`           | テーブルの最新スナップショットのストレージサイズ（バイト単位）。                                       |
| `data_retention_period_in_hours` | タイムトラベルデータの保持期間（時間単位）（`NULL` はデフォルトの保持ポリシーを使用することを意味します）。 |
| `error`                          | ストレージサイズの取得中に発生したエラー（エラーがない場合は `NULL`）。               |

## SQLの例

この例では、`default` データベース内のすべてのテーブルの履歴データを計算します。

```sql
SELECT * FROM fuse_time_travel_size('default')

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ database_name │ table_name │ is_dropped │ time_travel_size │ latest_snapshot_size │ data_retention_period_in_hours │       error      │
├───────────────┼────────────┼────────────┼──────────────────┼──────────────────────┼────────────────────────────────┼──────────────────┤
│ default       │ books      │ true       │             2810 │                 1490 │                           NULL │ NULL             │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
