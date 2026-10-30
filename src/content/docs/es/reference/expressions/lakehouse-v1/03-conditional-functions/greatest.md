---
title: GREATEST (Lakehouse v1)
description: GREATEST — devuelve el valor máximo de un conjunto de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/greatest.md
---

Devuelve el valor máximo de un conjunto de valores.

## Sintaxis de Analyze

```python
func.greatest(<value1>, <value2> ...)
```

## Ejemplos de Analyze

```python
func.greatest((5, 9, 4))

┌──────────────────────────┐
│ func.greatest((5, 9, 4)) │
├──────────────────────────┤
│                        9 │
└──────────────────────────┘
```

## Sintaxis de SQL

```sql
GREATEST(<value1>, <value2> ...)
```

## Ejemplos de SQL

```sql
SELECT GREATEST(5, 9, 4);

┌───────────────────┐
│ greatest(5, 9, 4) │
├───────────────────┤
│                 9 │
└───────────────────┘
```
