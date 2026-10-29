---
title: INSPECT_TABLE_PARTITION_INFO (Lakehouse v2)
description: INSPECT_TABLE_PARTITION_INFO — Devuelve información de particiones de una tabla.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-table-partition-info.md
---

Devuelve información de particiones de una tabla.

## Sintaxis de Analyze

```python
func.inspect_table_partition_info(<catalog>, <db>, <table>)
```

## Ejemplos de Analyze

```python
func.inspect_table_partition_info('default', 'mydb', 'my_table')

┌──────────────┐
│ (partitions)  │
└──────────────┘
```

## Sintaxis de SQL

```sql
INSPECT_TABLE_PARTITION_INFO(<catalog>, <db>, <table>)
```

## Ejemplos de SQL

```sql
SELECT * FROM TABLE(INSPECT_TABLE_PARTITION_INFO('default', 'mydb', 'my_table'));

┌──────────────────┐
│ (partition info)  │
└──────────────────┘
```
