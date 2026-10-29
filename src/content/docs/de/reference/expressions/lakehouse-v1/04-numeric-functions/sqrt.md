---
title: SQRT (Lakehouse v1)
description: SQRT – gibt die Quadratwurzel einer nicht negativen Zahl x zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sqrt.md
---

Gibt die Quadratwurzel einer nicht negativen Zahl `x` zurück. Gibt bei negativer Eingabe NaN zurück.

## Analyze-Syntax

```python
func.sqrt( <x> )
```

## Analyze-Beispiele

```python
func.sqrt(4)

┌──────────────┐
│ func.sqrt(4) │
├──────────────┤
│            2 │
└──────────────┘
```

## SQL-Syntax

```sql
SQRT( <x> )
```

## SQL-Beispiele

```sql
SELECT SQRT(4);

┌─────────┐
│ sqrt(4) │
├─────────┤
│       2 │
└─────────┘
```
