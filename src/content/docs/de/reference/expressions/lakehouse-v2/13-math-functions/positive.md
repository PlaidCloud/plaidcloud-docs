---
title: POSITIVE (Lakehouse v2)
description: POSITIVE – gibt den Wert unverändert zurück (unäres Plus).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/positive.md
---

Gibt den Wert unverändert zurück (unäres Plus).

## Analyze-Syntax

```python
func.positive(<x>)
```

## Analyze-Beispiele

```python
func.positive(-5)

┌────┐
│ -5  │
└────┘
```

## SQL-Syntax

```sql
POSITIVE(<x>)
```

## SQL-Beispiele

```sql
SELECT POSITIVE(-5);

┌────┐
│ -5  │
└────┘
```
