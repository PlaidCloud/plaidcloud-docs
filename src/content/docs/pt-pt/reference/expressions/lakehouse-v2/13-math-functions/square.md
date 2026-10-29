---
title: SQUARE (Lakehouse v2)
description: SQUARE — devolve o quadrado de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/square.md
---

Devolve o quadrado de um número.

## Sintaxe de Analyze

```python
func.square(<x>)
```

## Exemplos de Analyze

```python
func.square(7)

┌────┐
│ 49  │
└────┘
```

## Sintaxe SQL

```sql
SQUARE(<x>)
```

## Exemplos SQL

```sql
SELECT SQUARE(7);

┌────┐
│ 49  │
└────┘
```
