---
title: INSPECT_HIVE_PART_INFO (Lakehouse v2)
description: INSPECT_HIVE_PART_INFO — gibt Hive-Partitionsinformationen für eine externe Tabelle zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-hive-part-info.md
---

Gibt Hive-Partitionsinformationen für eine externe Tabelle zurück.

## Analyze-Syntax

```python
func.inspect_hive_part_info(<catalog>, <db>, <table>)
```

## Analyze-Beispiele

```python
func.inspect_hive_part_info('hive_catalog', 'db', 'tbl')

┌──────────────────┐
│ (partition info)  │
└──────────────────┘
```

## SQL-Syntax

```sql
INSPECT_HIVE_PART_INFO(<catalog>, <db>, <table>)
```

## SQL-Beispiele

```sql
SELECT * FROM TABLE(INSPECT_HIVE_PART_INFO('hive_catalog', 'db', 'tbl'));

┌─────────────────────┐
│ (partition details)  │
└─────────────────────┘
```
