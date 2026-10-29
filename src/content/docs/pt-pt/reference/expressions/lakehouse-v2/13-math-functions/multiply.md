---
title: MULTIPLY (Lakehouse v2)
description: MULTIPLY — devolve o produto de dois números.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/multiply.md
---

Devolve o produto de dois números.

## Sintaxe de Analyze

```python
func.multiply(<x>, <y>)
```

## Exemplos de Analyze

```python
func.multiply(6, 7)

┌────┐
│ 42  │
└────┘
```

## Sintaxe SQL

```sql
MULTIPLY(<x>, <y>)
```

## Exemplos SQL

```sql
SELECT MULTIPLY(6, 7);

┌────┐
│ 42  │
└────┘
```
