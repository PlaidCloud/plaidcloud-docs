---
title: ASIN (Lakehouse v2)
description: ASIN — devuelve el arcoseno de un número en radianes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/asin.md
---

Devuelve el arcoseno de un número en radianes.

## Sintaxis de Analyze

```python
func.asin(<x>)
```

## Ejemplos de Analyze

```python
func.asin(0.5)

┌────────────────────┐
│ 0.5235987755982988  │
└────────────────────┘
```

## Sintaxis de SQL

```sql
ASIN(<x>)
```

## Ejemplos de SQL

```sql
SELECT ASIN(0.5);

┌────────────────────┐
│ 0.5235987755982988  │
└────────────────────┘
```
