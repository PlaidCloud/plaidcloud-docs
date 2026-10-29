---
title: ABS (Lakehouse v1)
description: ABS – gibt den Absolutwert von x zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/abs.md
---

Gibt den Absolutwert von `x` zurück.

## Analyze-Syntax

```python
func.abs( <x> )
```

## Analyze-Beispiele

```python
func.abs((- 5))

┌─────────────────┐
│ func.abs((- 5)) │
├─────────────────┤
│               5 │
└─────────────────┘
```

## SQL-Syntax

```sql
ABS( <x> )
```

## SQL-Beispiele

```sql
SELECT ABS(-5);

┌────────────┐
│ abs((- 5)) │
├────────────┤
│          5 │
└────────────┘
```
