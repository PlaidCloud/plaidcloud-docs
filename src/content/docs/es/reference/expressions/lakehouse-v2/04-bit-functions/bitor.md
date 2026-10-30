---
title: BITOR (Lakehouse v2)
description: BITOR — devuelve el OR bit a bit de dos valores numéricos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitor.md
---

Devuelve el OR bit a bit de dos valores numéricos.

## Sintaxis de Analyze

```python
func.bitor(<x>, <y>)
```

## Ejemplos de Analyze

```python
func.bitor(12, 10)

┌────┐
│ 14  │
└────┘
```

## Sintaxis de SQL

```sql
BITOR(<x>, <y>)
```

## Ejemplos de SQL

```sql
SELECT BITOR(12, 10);

┌────┐
│ 14  │
└────┘
```
