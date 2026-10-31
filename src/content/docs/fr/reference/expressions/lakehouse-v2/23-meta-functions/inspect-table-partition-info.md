---
title: INSPECT_TABLE_PARTITION_INFO (Lakehouse v2)
description: INSPECT_TABLE_PARTITION_INFO — renvoie les informations de partition d'une table.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-table-partition-info.md
---

Renvoie les informations de partition d'une table.

## Syntaxe Analyze

```python
func.inspect_table_partition_info(<catalog>, <db>, <table>)
```

## Exemples Analyze

```python
func.inspect_table_partition_info('default', 'mydb', 'my_table')

┌──────────────┐
│ (partitions)  │
└──────────────┘
```

## Syntaxe SQL

```sql
INSPECT_TABLE_PARTITION_INFO(<catalog>, <db>, <table>)
```

## Exemples SQL

```sql
SELECT * FROM TABLE(INSPECT_TABLE_PARTITION_INFO('default', 'mydb', 'my_table'));

┌──────────────────┐
│ (partition info)  │
└──────────────────┘
```
