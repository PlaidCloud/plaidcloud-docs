---
title: POSITIVE (Lakehouse v2)
description: POSITIVE — devolve o valor inalterado (mais unário).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/positive.md
---

Devolve o valor inalterado (mais unário).

## Sintaxe de Analyze

```python
func.positive(<x>)
```

## Exemplos de Analyze

```python
func.positive(-5)

┌────┐
│ -5  │
└────┘
```

## Sintaxe SQL

```sql
POSITIVE(<x>)
```

## Exemplos SQL

```sql
SELECT POSITIVE(-5);

┌────┐
│ -5  │
└────┘
```
