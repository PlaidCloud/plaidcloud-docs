---
title: INSPECT_HIVE_PART_INFO (Lakehouse v2)
description: INSPECT_HIVE_PART_INFO — zwraca informacje o partycjach Hive dla tabeli zewnętrznej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-hive-part-info.md
---

Zwraca informacje o partycjach Hive dla tabeli zewnętrznej.

## Składnia Analyze

```python
func.inspect_hive_part_info(<catalog>, <db>, <table>)
```

## Przykłady Analyze

```python
func.inspect_hive_part_info('hive_catalog', 'db', 'tbl')

┌──────────────────┐
│ (partition info)  │
└──────────────────┘
```

## Składnia SQL

```sql
INSPECT_HIVE_PART_INFO(<catalog>, <db>, <table>)
```

## Przykłady SQL

```sql
SELECT * FROM TABLE(INSPECT_HIVE_PART_INFO('hive_catalog', 'db', 'tbl'));

┌─────────────────────┐
│ (partition details)  │
└─────────────────────┘
```
