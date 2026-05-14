---
title: INSPECT_HIVE_PART_INFO
description: "Learn how to use the INSPECT_HIVE_PART_INFO meta function in PlaidCloud Lakehouse. Returns Hive partition information for an external table."
---

Returns Hive partition information for an external table.

## Analyze Syntax

```python
func.inspect_hive_part_info(<catalog>, <db>, <table>)
```

## Analyze Examples

```python
func.inspect_hive_part_info('hive_catalog', 'db', 'tbl')

┌──────────────────┐
│ (partition info)  │
└──────────────────┘
```

## SQL Syntax

```sql
INSPECT_HIVE_PART_INFO(<catalog>, <db>, <table>)
```

## SQL Examples

```sql
SELECT * FROM TABLE(INSPECT_HIVE_PART_INFO('hive_catalog', 'db', 'tbl'));

┌─────────────────────┐
│ (partition details)  │
└─────────────────────┘
```
