---
title: FUSE_TIME_TRAVEL_SIZE (Lakehouse v1)
description: FUSE_TIME_TRAVEL_SIZE：计算表的历史数据（用于时间旅行）的存储大小。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-time-travel-size.md
---

计算表的历史数据（用于时间旅行）的存储大小。

## SQL 语法

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

## 输出

该函数返回包含以下列的结果集：

| 列 | 说明 |
|----------------------------------|-------------------------------------------------------------------------------------------------------|
| `database_name` | 表所在数据库的名称。 |
| `table_name` | 表的名称。 |
| `is_dropped` | 指示表是否已被删除（已删除的表为 `true`，否则为 `false`）。 |
| `time_travel_size` | 表的历史数据（用于时间旅行）的总存储大小，单位为字节。 |
| `latest_snapshot_size` | 表的最新快照的存储大小，单位为字节。 |
| `data_retention_period_in_hours` | 时间旅行数据的保留期，单位为小时（`NULL` 表示使用默认保留策略）。 |
| `error` | 获取存储大小时遇到的任何错误（未发生错误时为 `NULL`）。 |

## SQL 示例

此示例计算 `default` 数据库中所有表的历史数据：

```sql
SELECT * FROM fuse_time_travel_size('default')

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ database_name │ table_name │ is_dropped │ time_travel_size │ latest_snapshot_size │ data_retention_period_in_hours │       error      │
├───────────────┼────────────┼────────────┼──────────────────┼──────────────────────┼────────────────────────────────┼──────────────────┤
│ default       │ books      │ true       │             2810 │                 1490 │                           NULL │ NULL             │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
