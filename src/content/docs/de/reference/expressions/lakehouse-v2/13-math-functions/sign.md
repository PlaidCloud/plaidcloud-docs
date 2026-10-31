---
title: SIGN (Lakehouse v2)
description: "SIGN – gibt das Vorzeichen einer Zahl zurück: -1, 0 oder 1."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sign.md
---

Gibt das Vorzeichen einer Zahl zurück: -1, 0 oder 1.

## Analyze-Syntax

```python
func.sign(<x>)
```

## Analyze-Beispiele

```python
func.sign(-42)

┌────┐
│ -1  │
└────┘
```

## SQL-Syntax

```sql
SIGN(<x>)
```

## SQL-Beispiele

```sql
SELECT SIGN(-42);

┌────┐
│ -1  │
└────┘
```
