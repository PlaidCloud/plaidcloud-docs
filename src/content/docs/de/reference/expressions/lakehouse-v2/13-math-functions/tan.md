---
title: TAN (Lakehouse v2)
description: TAN – gibt den Tangens einer Zahl im Bogenmaß zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/tan.md
---

Gibt den Tangens einer Zahl im Bogenmaß zurück.

## Analyze-Syntax

```python
func.tan(<x>)
```

## Analyze-Beispiele

```python
func.tan(0)

┌─────┐
│ 0.0  │
└─────┘
```

## SQL-Syntax

```sql
TAN(<x>)
```

## SQL-Beispiele

```sql
SELECT TAN(0);

┌─────┐
│ 0.0  │
└─────┘
```
