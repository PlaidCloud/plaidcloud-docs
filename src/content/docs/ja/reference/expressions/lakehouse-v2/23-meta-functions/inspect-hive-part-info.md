---
title: INSPECT_HIVE_PART_INFO（Lakehouse v2）
description: INSPECT_HIVE_PART_INFO — 外部テーブルの Hive パーティション情報を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-hive-part-info.md
---

外部テーブルの Hive パーティション情報を返します。

## Analyze 構文

```python
func.inspect_hive_part_info(<catalog>, <db>, <table>)
```

## Analyze の例

```python
func.inspect_hive_part_info('hive_catalog', 'db', 'tbl')

┌──────────────────┐
│ (partition info)  │
└──────────────────┘
```

## SQL 構文

```sql
INSPECT_HIVE_PART_INFO(<catalog>, <db>, <table>)
```

## SQL の例

```sql
SELECT * FROM TABLE(INSPECT_HIVE_PART_INFO('hive_catalog', 'db', 'tbl'));

┌─────────────────────┐
│ (partition details)  │
└─────────────────────┘
```
