---
title: LOG10 (Lakehouse v2)
description: LOG10 — devuelve el logaritmo en base 10 de un número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log10.md
---

Devuelve el logaritmo en base 10 de un número.

## Sintaxis de Analyze

```python
func.log10(<x>)
```

## Ejemplos de Analyze

```python
func.log10(1000)

┌─────┐
│ 3.0  │
└─────┘
```

## Sintaxis de SQL

```sql
LOG10(<x>)
```

## Ejemplos de SQL

```sql
SELECT LOG10(1000);

┌─────┐
│ 3.0  │
└─────┘
```
