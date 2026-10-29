---
title: DEGREES (Lakehouse v2)
description: DEGREES — converte radianos em graus.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/degrees.md
---

Converte radianos em graus.

## Sintaxe do Analyze

```python
func.degrees(<x>)
```

## Exemplos do Analyze

```python
func.degrees(3.141592653589793)

┌───────┐
│ 180.0  │
└───────┘
```

## Sintaxe SQL

```sql
DEGREES(<x>)
```

## Exemplos de SQL

```sql
SELECT DEGREES(PI());

┌───────┐
│ 180.0  │
└───────┘
```
