---
title: SPLIT_PART (Lakehouse v2)
description: SPLIT_PART — teilt eine Zeichenfolge anhand eines Trennzeichens und gibt das Element am angegebenen Index zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/split-part.md
---

Teilt eine Zeichenfolge anhand eines Trennzeichens und gibt das Element am angegebenen Index zurück.

## Analyze-Syntax

```python
func.split_part(<str>, <delimiter>, <index>)
```

## Analyze-Beispiele

```python
func.split_part('a-b-c', '-', 2)

┌─────┐
│ 'b'  │
└─────┘
```

## SQL-Syntax

```sql
SPLIT_PART(<str>, <delimiter>, <index>)
```

## SQL-Beispiele

```sql
SELECT SPLIT_PART('a-b-c', '-', 2);

┌───┐
│ b  │
└───┘
```
