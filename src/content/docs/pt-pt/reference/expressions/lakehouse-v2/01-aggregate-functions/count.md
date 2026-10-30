---
title: COUNT (Lakehouse v2)
description: COUNT — devolve o número de linhas ou de valores não NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/count.md
---

Devolve o número de linhas ou de valores não NULL.

## Sintaxe do Analyze

```python
func.count()
```

## Exemplos do Analyze

```python
func.count()
```

## Sintaxe SQL

```sql
COUNT()
```

## Exemplos de SQL

```sql
SELECT COUNT(*) FROM employees;

┌──────────┐
│ count(*) │
├──────────┤
│     1000 │
└──────────┘

SELECT COUNT(DISTINCT department) FROM employees;

┌──────────────────────────────┐
│ count(distinct department)   │
├──────────────────────────────┤
│                            5 │
└──────────────────────────────┘
```
