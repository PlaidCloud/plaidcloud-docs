---
title: INSPECT_HIVE_PART_INFO (Lakehouse v2)
description: INSPECT_HIVE_PART_INFO — Devuelve información de particiones de Hive para una tabla externa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-hive-part-info.md
---

Devuelve información de particiones de Hive para una tabla externa.

## Sintaxis de Analyze

```python
func.inspect_hive_part_info(<catalog>, <db>, <table>)
```

## Ejemplos de Analyze

```python
func.inspect_hive_part_info('hive_catalog', 'db', 'tbl')

┌──────────────────┐
│ (partition info)  │
└──────────────────┘
```

## Sintaxis de SQL

```sql
INSPECT_HIVE_PART_INFO(<catalog>, <db>, <table>)
```

## Ejemplos de SQL

```sql
SELECT * FROM TABLE(INSPECT_HIVE_PART_INFO('hive_catalog', 'db', 'tbl'));

┌─────────────────────┐
│ (partition details)  │
└─────────────────────┘
```
