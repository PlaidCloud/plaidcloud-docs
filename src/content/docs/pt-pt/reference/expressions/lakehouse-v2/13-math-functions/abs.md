---
title: ABS (Lakehouse v2)
description: ABS — devolve o valor absoluto de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/abs.md
---

Devolve o valor absoluto de um número.

## Sintaxe de Analyze

```python
func.abs(<x>)
```

## Exemplos de Analyze

```python
func.abs(-5)

┌───┐
│ 5  │
└───┘
```

## Sintaxe SQL

```sql
ABS(<x>)
```

## Exemplos SQL

```sql
SELECT ABS(-5);

┌───┐
│ 5  │
└───┘
```
