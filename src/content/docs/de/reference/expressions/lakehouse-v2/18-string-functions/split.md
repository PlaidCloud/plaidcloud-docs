---
title: SPLIT (Lakehouse v2)
description: SPLIT — teilt eine Zeichenfolge anhand eines Trennzeichens und gibt ein Array zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/split.md
---

Teilt eine Zeichenfolge anhand eines Trennzeichens und gibt ein Array zurück.

## Analyze-Syntax

```python
func.split(<str>, <delimiter>)
```

## Analyze-Beispiele

```python
func.split('a,b,c', ',')

┌───────────────┐
│ ['a','b','c']  │
└───────────────┘
```

## SQL-Syntax

```sql
SPLIT(<str>, <delimiter>)
```

## SQL-Beispiele

```sql
SELECT SPLIT('a,b,c', ',');

┌───────────────┐
│ ["a","b","c"]  │
└───────────────┘
```
