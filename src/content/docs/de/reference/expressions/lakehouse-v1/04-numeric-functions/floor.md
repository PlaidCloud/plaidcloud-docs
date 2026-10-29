---
title: FLOOR (Lakehouse v1)
description: FLOOR – rundet die Zahl ab.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/floor.md
---

Rundet die Zahl ab.

## Analyze-Syntax

```python
func.floor( <x> )
```

## Analyze-Beispiele

```python
func.floor(1.23)

┌──────────────────┐
│ func.floor(1.23) │
├──────────────────┤
│                1 │
└──────────────────┘
```

## SQL-Syntax

```sql
FLOOR( <x> )
```

## SQL-Beispiele

```sql
SELECT FLOOR(1.23);

┌─────────────┐
│ floor(1.23) │
├─────────────┤
│           1 │
└─────────────┘
```
