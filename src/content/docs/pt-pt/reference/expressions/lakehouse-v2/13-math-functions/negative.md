---
title: NEGATIVE (Lakehouse v2)
description: NEGATIVE — devolve a negação de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/negative.md
---

Devolve a negação de um número.

## Sintaxe de Analyze

```python
func.negative(<x>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT NEGATIVE(5);

┌────┐
│ -5  │
└────┘
```
