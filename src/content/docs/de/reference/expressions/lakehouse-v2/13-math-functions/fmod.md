---
title: FMOD (Lakehouse v2)
description: FMOD – gibt den Gleitkomma-Rest der Division zweier Zahlen zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/fmod.md
---

Gibt den Gleitkomma-Rest der Division zweier Zahlen zurück.

## Analyze-Syntax

```python
func.fmod(<x>, <y>)
```

## Analyze-Beispiele

```python
func.fmod(10.5, 3.0)

┌─────┐
│ 1.5  │
└─────┘
```

## SQL-Syntax

```sql
FMOD(<x>, <y>)
```

## SQL-Beispiele

```sql
SELECT FMOD(10.5, 3.0);

┌─────┐
│ 1.5  │
└─────┘
```
