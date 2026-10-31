---
title: LENGTH (Lakehouse v2)
description: LENGTH — gibt die Länge einer Zeichenfolge in Bytes zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/length.md
---

Gibt die Länge einer Zeichenfolge in Bytes zurück.

## Analyze-Syntax

```python
func.length(<str>)
```

## Analyze-Beispiele

```python
func.length('hello')

┌───┐
│ 5  │
└───┘
```

## SQL-Syntax

```sql
LENGTH(<str>)
```

## SQL-Beispiele

```sql
SELECT LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
