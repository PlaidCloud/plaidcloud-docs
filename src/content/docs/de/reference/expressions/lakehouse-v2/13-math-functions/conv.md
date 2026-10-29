---
title: CONV (Lakehouse v2)
description: CONV – wandelt eine Zahl von einer Basis in eine andere um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/conv.md
---

Wandelt eine Zahl von einer Basis in eine andere um.

## Analyze-Syntax

```python
func.conv(<num>, <from_base>, <to_base>)
```

## Analyze-Beispiele

```python
func.conv('ff', 16, 10)

┌───────┐
│ '255'  │
└───────┘
```

## SQL-Syntax

```sql
CONV(<num>, <from_base>, <to_base>)
```

## SQL-Beispiele

```sql
SELECT CONV('ff', 16, 10);

┌─────┐
│ 255  │
└─────┘
```
