---
title: LOOKUP_STRING (Lakehouse v2)
description: LOOKUP_STRING — sucht eine Zeichenfolge in einem Wörterbuch und gibt die zugehörige ID zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/lookup-string.md
---

Sucht eine Zeichenfolge in einem Wörterbuch und gibt die zugehörige ID zurück.

## Analyze-Syntax

```python
func.lookup_string(<dict_table>, <value>)
```

## Analyze-Beispiele

```python
func.lookup_string('status_dict', 'Active')

┌───┐
│ 1  │
└───┘
```

## SQL-Syntax

```sql
LOOKUP_STRING(<dict_table>, <value>)
```

## SQL-Beispiele

```sql
SELECT LOOKUP_STRING('status_dict', 'Active');

┌───┐
│ 1  │
└───┘
```
