---
title: LEAST (Lakehouse v1)
description: LEAST — devuelve el valor mínimo de un conjunto de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/least.md
---

Devuelve el valor mínimo de un conjunto de valores.

## Sintaxis de Analyze

```python
func.least((<value1>, <value2> ...))
```

## Ejemplos de Analyze

```python
func.least((5, 9, 4))

┌───────────────────────┐
│ func.least((5, 9, 4)) │
├───────────────────────┤
│                     4 │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
LEAST(<value1>, <value2> ...)
```

## Ejemplos de SQL

```sql
SELECT LEAST(5, 9, 4);

┌────────────────┐
│ least(5, 9, 4) │
├────────────────┤
│              4 │
└────────────────┘
```
