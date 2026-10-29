---
title: CONV (Lakehouse v2)
description: CONV — convierte un número de una base a otra.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/conv.md
---

Convierte un número de una base a otra.

## Sintaxis de Analyze

```python
func.conv(<num>, <from_base>, <to_base>)
```

## Ejemplos de Analyze

```python
func.conv('ff', 16, 10)

┌───────┐
│ '255'  │
└───────┘
```

## Sintaxis de SQL

```sql
CONV(<num>, <from_base>, <to_base>)
```

## Ejemplos de SQL

```sql
SELECT CONV('ff', 16, 10);

┌─────┐
│ 255  │
└─────┘
```
