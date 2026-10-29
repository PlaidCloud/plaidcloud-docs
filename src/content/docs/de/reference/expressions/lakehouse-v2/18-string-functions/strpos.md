---
title: STRPOS (Lakehouse v2)
description: STRPOS — gibt die Position des ersten Vorkommens einer Teilzeichenfolge zurück. Alias für `LOCATE`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strpos.md
---

Gibt die Position des ersten Vorkommens einer Teilzeichenfolge zurück. Alias für `LOCATE`.

## Analyze-Syntax

```python
func.strpos(<str>, <substr>)
```

## Analyze-Beispiele

```python
func.strpos('hello world', 'world')

┌───┐
│ 7  │
└───┘
```

## SQL-Syntax

```sql
STRPOS(<str>, <substr>)
```

## SQL-Beispiele

```sql
SELECT STRPOS('hello world', 'world');

┌───┐
│ 7  │
└───┘
```
