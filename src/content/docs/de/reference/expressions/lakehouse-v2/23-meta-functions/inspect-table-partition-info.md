---
title: INSPECT_TABLE_PARTITION_INFO (Lakehouse v2)
description: INSPECT_TABLE_PARTITION_INFO — Gibt Partitionsinformationen zu einer Tabelle zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-table-partition-info.md
---

Gibt Partitionsinformationen zu einer Tabelle zurück.

## Analyze-Syntax

```python
func.inspect_table_partition_info(<catalog>, <db>, <table>)
```

## Analyze-Beispiele

```python
func.inspect_table_partition_info('default', 'mydb', 'my_table')

┌──────────────┐
│ (partitions)  │
└──────────────┘
```

## SQL-Syntax

```sql
INSPECT_TABLE_PARTITION_INFO(<catalog>, <db>, <table>)
```

## SQL-Beispiele

```sql
SELECT * FROM TABLE(INSPECT_TABLE_PARTITION_INFO('default', 'mydb', 'my_table'));

┌──────────────────┐
│ (partition info)  │
└──────────────────┘
```
