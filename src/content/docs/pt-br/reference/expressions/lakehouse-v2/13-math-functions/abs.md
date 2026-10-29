---
title: ABS (Lakehouse v2)
description: ABS — retorna o valor absoluto de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/abs.md
---

Retorna o valor absoluto de um número.

## Sintaxe do Analyze

```python
func.abs(<x>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT ABS(-5);

┌───┐
│ 5  │
└───┘
```
