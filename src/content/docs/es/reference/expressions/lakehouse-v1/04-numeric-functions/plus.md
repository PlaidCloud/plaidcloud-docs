---
title: PLUS (Lakehouse v1)
description: PLUS — calcula la suma de dos valores numéricos o decimales.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/plus.md
---

Calcula la suma de dos valores numéricos o decimales.

## Sintaxis de Analyze

```python
func.plus(<number1>, <number2>)
```

## Ejemplos de Analyze

```python
func.plus(1, 2.3)

┌────────────────────┐
│  func.plus(1, 2.3) │
├────────────────────┤
│ 3.3                │
└────────────────────┘
```

## Sintaxis de SQL

```sql
PLUS(<number1>, <number2>)
```

## Alias

- [ADD](../add)

## Ejemplos de SQL

```sql
SELECT ADD(1, 2.3), PLUS(1, 2.3);

┌───────────────────────────────┐
│  add(1, 2.3)  │  plus(1, 2.3) │
├───────────────┼───────────────┤
│ 3.3           │ 3.3           │
└───────────────────────────────┘
```
