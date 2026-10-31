---
title: NULLIF (Lakehouse v2)
description: NULLIF — renvoie NULL si deux expressions sont égales, sinon renvoie la première expression.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/nullif.md
---

Renvoie NULL si deux expressions sont égales, sinon renvoie la première expression.

## Syntaxe Analyze

```python
func.nullif(get_column(table, 'value'), 0)
```

## Exemples Analyze

```python
func.nullif(get_column(table, 'divisor'), 0)
```

## Syntaxe SQL

```sql
NULLIF(<value>, 0)
```

## Exemples SQL

```sql
SELECT 100 / NULLIF(divisor, 0) AS safe_division FROM calculations;

┌───────────────┐
│ safe_division │
├───────────────┤
│         50.00 │
│          NULL │
│         25.00 │
└───────────────┘
```
