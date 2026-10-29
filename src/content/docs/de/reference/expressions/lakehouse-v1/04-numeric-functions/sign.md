---
title: SIGN (Lakehouse v1)
description: SIGN – gibt das Vorzeichen des Arguments als -1, 0 oder 1 zurück, je nachdem, ob x negativ, null oder positiv ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sign.md
---

Gibt das Vorzeichen des Arguments als -1, 0 oder 1 zurück, je nachdem, ob `x` negativ, null oder positiv ist, oder NULL, wenn das Argument NULL war.

## Analyze-Syntax

```python
func.sign( <x> )
```

## Analyze-Beispiele

```python
func.sign(0)

┌──────────────┐
│ func.sign(0) │
├──────────────┤
│            0 │
└──────────────┘
```

## SQL-Syntax

```sql
SIGN( <x> )
```

## SQL-Beispiele

```sql
SELECT SIGN(0);

┌─────────┐
│ sign(0) │
├─────────┤
│       0 │
└─────────┘
```
