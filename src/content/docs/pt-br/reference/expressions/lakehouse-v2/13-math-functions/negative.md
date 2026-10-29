---
title: NEGATIVE (Lakehouse v2)
description: NEGATIVE — retorna a negação de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/negative.md
---

Retorna a negação de um número.

## Sintaxe do Analyze

```python
func.negative(<x>)
```

## Exemplos do Analyze

```python
func.negative(5)

┌────┐
│ -5  │
└────┘
```

## Sintaxe SQL

```sql
NEGATIVE(<x>)
```

## Exemplos de SQL

```sql
SELECT NEGATIVE(5);

┌────┐
│ -5  │
└────┘
```
