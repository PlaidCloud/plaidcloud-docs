---
title: MULTI_DISTINCT_COUNT (Lakehouse v2)
description: MULTI_DISTINCT_COUNT — renvoie le nombre de valeurs distinctes. Équivalent à COUNT(DISTINCT).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/multi-distinct-count.md
---

Renvoie le nombre de valeurs distinctes. Équivalent à COUNT(DISTINCT).

## Syntaxe Analyze

```python
func.multi_distinct_count(get_column(table, 'dept'))
```

## Exemples Analyze

```python
func.multi_distinct_count(get_column(table, 'department'))

┌───┐
│ 5 │
└───┘
```

## Syntaxe SQL

```sql
MULTI_DISTINCT_COUNT(<dept>)
```

## Exemples SQL

```sql
SELECT MULTI_DISTINCT_COUNT(department) FROM employees;

┌───┐
│ 5 │
└───┘
```
