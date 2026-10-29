---
title: PI (Lakehouse v1)
description: PI – gibt den Wert von π als Gleitkommawert zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/pi.md
---

Gibt den Wert von π als Gleitkommawert zurück.

## Analyze-Syntax

```python
func.pi()
```

## Analyze-Beispiele

```python
func.pi()

┌───────────────────┐
│     func.pi()     │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```

## SQL-Syntax

```sql
PI()
```

## SQL-Beispiele

```sql
SELECT PI();

┌───────────────────┐
│        pi()       │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```
