---
title: CONV (Lakehouse v2)
description: CONV — convertit un nombre d'une base à une autre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/conv.md
---

Convertit un nombre d'une base à une autre.

## Syntaxe Analyze

```python
func.conv(<num>, <from_base>, <to_base>)
```

## Exemples Analyze

```python
func.conv('ff', 16, 10)

┌───────┐
│ '255'  │
└───────┘
```

## Syntaxe SQL

```sql
CONV(<num>, <from_base>, <to_base>)
```

## Exemples SQL

```sql
SELECT CONV('ff', 16, 10);

┌─────┐
│ 255  │
└─────┘
```
