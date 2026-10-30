---
title: POSITIVE (Lakehouse v2)
description: POSITIVE — retorna o valor sem alteração (mais unário).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/positive.md
---

Retorna o valor sem alteração (mais unário).

## Sintaxe do Analyze

```python
func.positive(<x>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT POSITIVE(-5);

┌────┐
│ -5  │
└────┘
```
