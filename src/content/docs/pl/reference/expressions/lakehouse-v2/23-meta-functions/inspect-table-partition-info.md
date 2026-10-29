---
title: INSPECT_TABLE_PARTITION_INFO (Lakehouse v2)
description: INSPECT_TABLE_PARTITION_INFO — zwraca informacje o partycjach tabeli.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-table-partition-info.md
---

Zwraca informacje o partycjach tabeli.

## Składnia Analyze

```python
func.inspect_table_partition_info(<catalog>, <db>, <table>)
```

## Przykłady Analyze

```python
func.inspect_table_partition_info('default', 'mydb', 'my_table')

┌──────────────┐
│ (partitions)  │
└──────────────┘
```

## Składnia SQL

```sql
INSPECT_TABLE_PARTITION_INFO(<catalog>, <db>, <table>)
```

## Przykłady SQL

```sql
SELECT * FROM TABLE(INSPECT_TABLE_PARTITION_INFO('default', 'mydb', 'my_table'));

┌──────────────────┐
│ (partition info)  │
└──────────────────┘
```
