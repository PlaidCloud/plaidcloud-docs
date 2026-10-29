---
title: COS (Lakehouse v2)
description: COS – gibt den Kosinus einer Zahl im Bogenmaß zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cos.md
---

Gibt den Kosinus einer Zahl im Bogenmaß zurück.

## Analyze-Syntax

```python
func.cos(<x>)
```

## Analyze-Beispiele

```python
func.cos(0)

┌─────┐
│ 1.0  │
└─────┘
```

## SQL-Syntax

```sql
COS(<x>)
```

## SQL-Beispiele

```sql
SELECT COS(0);

┌─────┐
│ 1.0  │
└─────┘
```
