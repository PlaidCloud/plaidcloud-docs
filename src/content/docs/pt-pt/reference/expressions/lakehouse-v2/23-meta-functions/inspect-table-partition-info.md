---
title: INSPECT_TABLE_PARTITION_INFO (Lakehouse v2)
description: INSPECT_TABLE_PARTITION_INFO — devolve informação de partições de uma tabela.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-table-partition-info.md
---

Devolve informação de partições de uma tabela.

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

## Exemplos SQL

```sql
SELECT * FROM TABLE(INSPECT_TABLE_PARTITION_INFO('default', 'mydb', 'my_table'));

┌──────────────────┐
│ (partition info)  │
└──────────────────┘
```
