---
title: INSPECT_HIVE_PART_INFO (Lakehouse v2)
description: INSPECT_HIVE_PART_INFO — renvoie les informations de partition Hive d'une table externe.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-hive-part-info.md
---

Renvoie les informations de partition Hive d'une table externe.

## Syntaxe Analyze

```python
func.inspect_hive_part_info(<catalog>, <db>, <table>)
```

## Exemples Analyze

```python
func.inspect_hive_part_info('hive_catalog', 'db', 'tbl')

┌──────────────────┐
│ (partition info)  │
└──────────────────┘
```

## Syntaxe SQL

```sql
INSPECT_HIVE_PART_INFO(<catalog>, <db>, <table>)
```

## Exemples SQL

```sql
SELECT * FROM TABLE(INSPECT_HIVE_PART_INFO('hive_catalog', 'db', 'tbl'));

┌─────────────────────┐
│ (partition details)  │
└─────────────────────┘
```
