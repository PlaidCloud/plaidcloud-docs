---
title: COT (Lakehouse v2)
description: COT — devuelve la cotangente de un número en radianes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cot.md
---

Devuelve la cotangente de un número en radianes.

## Sintaxis de Analyze

```python
func.cot(<x>)
```

## Ejemplos de Analyze

```python
func.cot(1)

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```

## Sintaxis de SQL

```sql
COT(<x>)
```

## Ejemplos de SQL

```sql
SELECT COT(1);

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```
