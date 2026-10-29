---
title: SIN (Lakehouse v2)
description: SIN – gibt den Sinus einer Zahl im Bogenmaß zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sin.md
---

Gibt den Sinus einer Zahl im Bogenmaß zurück.

## Analyze-Syntax

```python
func.sin(<x>)
```

## Analyze-Beispiele

```python
func.sin(0)

┌─────┐
│ 0.0  │
└─────┘
```

## SQL-Syntax

```sql
SIN(<x>)
```

## SQL-Beispiele

```sql
SELECT SIN(0);

┌─────┐
│ 0.0  │
└─────┘
```
