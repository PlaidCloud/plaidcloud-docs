---
title: INSPECT_TABLE_PARTITION_INFO (Lakehouse v2)
description: INSPECT_TABLE_PARTITION_INFO — Retorna informações de partição de uma tabela.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-table-partition-info.md
---

Retorna informações de partição de uma tabela.

## Sintaxe do Analyze

```python
func.inspect_table_partition_info(<catalog>, <db>, <table>)
```

## Exemplos do Analyze

```python
func.inspect_table_partition_info('default', 'mydb', 'my_table')

┌──────────────┐
│ (partitions)  │
└──────────────┘
```

## Sintaxe SQL

```sql
INSPECT_TABLE_PARTITION_INFO(<catalog>, <db>, <table>)
```

## Exemplos de SQL

```sql
SELECT * FROM TABLE(INSPECT_TABLE_PARTITION_INFO('default', 'mydb', 'my_table'));

┌──────────────────┐
│ (partition info)  │
└──────────────────┘
```
