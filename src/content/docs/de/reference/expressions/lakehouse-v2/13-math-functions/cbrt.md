---
title: CBRT (Lakehouse v2)
description: CBRT – gibt die Kubikwurzel einer Zahl zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cbrt.md
---

Gibt die Kubikwurzel einer Zahl zurück.

## Analyze-Syntax

```python
func.cbrt(<x>)
```

## Analyze-Beispiele

```python
func.cbrt(27)

┌─────┐
│ 3.0  │
└─────┘
```

## SQL-Syntax

```sql
CBRT(<x>)
```

## SQL-Beispiele

```sql
SELECT CBRT(27);

┌─────┐
│ 3.0  │
└─────┘
```
