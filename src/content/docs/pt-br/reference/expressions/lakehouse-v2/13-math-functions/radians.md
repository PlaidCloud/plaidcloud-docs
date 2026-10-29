---
title: RADIANS (Lakehouse v2)
description: RADIANS — converte graus em radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/radians.md
---

Converte graus em radianos.

## Sintaxe do Analyze

```python
func.radians(<x>)
```

## Exemplos do Analyze

```python
func.radians(180)

┌───────────────────┐
│ 3.141592653589793  │
└───────────────────┘
```

## Sintaxe SQL

```sql
RADIANS(<x>)
```

## Exemplos de SQL

```sql
SELECT RADIANS(180);

┌───────────────────┐
│ 3.141592653589793  │
└───────────────────┘
```
