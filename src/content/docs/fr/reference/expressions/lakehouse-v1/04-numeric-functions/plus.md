---
title: PLUS (Lakehouse v1)
description: PLUS — calcule la somme de deux valeurs numériques ou décimales.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/plus.md
---

Calcule la somme de deux valeurs numériques ou décimales.

## Syntaxe Analyze

```python
func.plus(<number1>, <number2>)
```

## Exemples Analyze

```python
func.plus(1, 2.3)

┌────────────────────┐
│  func.plus(1, 2.3) │
├────────────────────┤
│ 3.3                │
└────────────────────┘
```

## Syntaxe SQL

```sql
PLUS(<number1>, <number2>)
```

## Alias

- [ADD](../add)

## Exemples SQL

```sql
SELECT ADD(1, 2.3), PLUS(1, 2.3);

┌───────────────────────────────┐
│  add(1, 2.3)  │  plus(1, 2.3) │
├───────────────┼───────────────┤
│ 3.3           │ 3.3           │
└───────────────────────────────┘
```
