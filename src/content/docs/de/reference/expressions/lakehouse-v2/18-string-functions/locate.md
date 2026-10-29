---
title: LOCATE (Lakehouse v2)
description: LOCATE — gibt die Position des ersten Vorkommens einer Teilzeichenfolge in einer Zeichenfolge zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/locate.md
---

Gibt die Position des ersten Vorkommens einer Teilzeichenfolge in einer Zeichenfolge zurück.

## Analyze-Syntax

```python
func.locate(<substr>, <str>[, <pos>])
```

## Analyze-Beispiele

```python
func.locate('or', 'hello world')

┌───┐
│ 8  │
└───┘
```

## SQL-Syntax

```sql
LOCATE(<substr>, <str>[, <pos>])
```

## SQL-Beispiele

```sql
SELECT LOCATE('or', 'hello world');

┌───┐
│ 8  │
└───┘
```
