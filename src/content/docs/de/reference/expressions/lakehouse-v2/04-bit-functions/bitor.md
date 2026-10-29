---
title: BITOR (Lakehouse v2)
description: BITOR – gibt das bitweise ODER zweier numerischer Werte zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitor.md
---

Gibt das bitweise ODER zweier numerischer Werte zurück.

## Analyze-Syntax

```python
func.bitor(<x>, <y>)
```

## Analyze-Beispiele

```python
func.bitor(12, 10)

┌────┐
│ 14  │
└────┘
```

## SQL-Syntax

```sql
BITOR(<x>, <y>)
```

## SQL-Beispiele

```sql
SELECT BITOR(12, 10);

┌────┐
│ 14  │
└────┘
```
