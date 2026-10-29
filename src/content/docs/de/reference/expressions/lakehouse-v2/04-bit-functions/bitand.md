---
title: BITAND (Lakehouse v2)
description: BITAND – gibt das bitweise UND zweier numerischer Werte zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitand.md
---

Gibt das bitweise UND zweier numerischer Werte zurück.

## Analyze-Syntax

```python
func.bitand(<x>, <y>)
```

## Analyze-Beispiele

```python
func.bitand(12, 10)

┌───┐
│ 8  │
└───┘
```

## SQL-Syntax

```sql
BITAND(<x>, <y>)
```

## SQL-Beispiele

```sql
SELECT BITAND(12, 10);

┌───┐
│ 8  │
└───┘
```
