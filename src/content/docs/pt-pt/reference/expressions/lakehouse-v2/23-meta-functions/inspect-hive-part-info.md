---
title: INSPECT_HIVE_PART_INFO (Lakehouse v2)
description: INSPECT_HIVE_PART_INFO — devolve informação de partições Hive de uma tabela externa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-hive-part-info.md
---

Devolve informação de partições Hive de uma tabela externa.

## Sintaxe do Analyze

```python
func.inspect_hive_part_info(<catalog>, <db>, <table>)
```

## Exemplos do Analyze

```python
func.inspect_hive_part_info('hive_catalog', 'db', 'tbl')

┌──────────────────┐
│ (partition info)  │
└──────────────────┘
```

## Sintaxe SQL

```sql
INSPECT_HIVE_PART_INFO(<catalog>, <db>, <table>)
```

## Exemplos SQL

```sql
SELECT * FROM TABLE(INSPECT_HIVE_PART_INFO('hive_catalog', 'db', 'tbl'));

┌─────────────────────┐
│ (partition details)  │
└─────────────────────┘
```
