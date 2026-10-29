---
title: ROUND (Lakehouse v2)
description: ROUND — arrondit un nombre à un nombre de décimales spécifié.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/round.md
---

Arrondit un nombre à un nombre de décimales spécifié.

## Syntaxe Analyze

```python
func.round(<x>[, <d>])
```

## Exemples Analyze

```python
func.round(3.14159, 2)

┌──────┐
│ 3.14  │
└──────┘
```

## Syntaxe SQL

```sql
ROUND(<x>[, <d>])
```

## Exemples SQL

```sql
SELECT ROUND(3.14159, 2);

┌──────┐
│ 3.14  │
└──────┘
```
