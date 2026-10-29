---
title: SQUARE (Lakehouse v2)
description: SQUARE — retorna o quadrado de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/square.md
---

Retorna o quadrado de um número.

## Sintaxe do Analyze

```python
func.square(<x>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT SQUARE(7);

┌────┐
│ 49  │
└────┘
```
