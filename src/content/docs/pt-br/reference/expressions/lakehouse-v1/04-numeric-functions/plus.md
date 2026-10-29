---
title: PLUS (Lakehouse v1)
description: PLUS — calcula a soma de dois valores numéricos ou decimais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/plus.md
---

Calcula a soma de dois valores numéricos ou decimais.

## Sintaxe do Analyze

```python
func.plus(<number1>, <number2>)
```

## Exemplos do Analyze

```python
func.plus(1, 2.3)

┌────────────────────┐
│  func.plus(1, 2.3) │
├────────────────────┤
│ 3.3                │
└────────────────────┘
```

## Sintaxe SQL

```sql
PLUS(<number1>, <number2>)
```

## Aliases

- [ADD](../add)

## Exemplos de SQL

```sql
SELECT ADD(1, 2.3), PLUS(1, 2.3);

┌───────────────────────────────┐
│  add(1, 2.3)  │  plus(1, 2.3) │
├───────────────┼───────────────┤
│ 3.3           │ 3.3           │
└───────────────────────────────┘
```
