---
title: INSPECT_TABLE_PARTITION_INFO
description: "Learn how to use the INSPECT_TABLE_PARTITION_INFO meta function in PlaidCloud Lakehouse. Returns partition information for a table - with syntax and examples."
---

Returns partition information for a table.

## Analyze Syntax

```python
func.inspect_table_partition_info(<catalog>, <db>, <table>)
```

## Analyze Examples

```python
func.inspect_table_partition_info('default', 'mydb', 'my_table')

┌──────────────┐
│ (partitions)  │
└──────────────┘
```

## SQL Syntax

```sql
INSPECT_TABLE_PARTITION_INFO(<catalog>, <db>, <table>)
```

## SQL Examples

```sql
SELECT * FROM TABLE(INSPECT_TABLE_PARTITION_INFO('default', 'mydb', 'my_table'));

┌──────────────────┐
│ (partition info)  │
└──────────────────┘
```
