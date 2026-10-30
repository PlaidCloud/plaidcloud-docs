---
title: INSPECT_HIVE_PART_INFO (Lakehouse v2)
description: INSPECT_HIVE_PART_INFO：返回外部表的 Hive 分区信息。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-hive-part-info.md
---

返回外部表的 Hive 分区信息。

## Analyze 语法

```python
func.inspect_hive_part_info(<catalog>, <db>, <table>)
```

## Analyze 示例

```python
func.inspect_hive_part_info('hive_catalog', 'db', 'tbl')

┌──────────────────┐
│ (partition info)  │
└──────────────────┘
```

## SQL 语法

```sql
INSPECT_HIVE_PART_INFO(<catalog>, <db>, <table>)
```

## SQL 示例

```sql
SELECT * FROM TABLE(INSPECT_HIVE_PART_INFO('hive_catalog', 'db', 'tbl'));

┌─────────────────────┐
│ (partition details)  │
└─────────────────────┘
```
