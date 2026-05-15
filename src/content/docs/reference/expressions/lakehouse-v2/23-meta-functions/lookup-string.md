---
title: LOOKUP_STRING (Lakehouse v2)
description: LOOKUP_STRING — looks up a string in a dictionary and returns the corresponding ID.
---

Looks up a string in a dictionary and returns the corresponding ID.

## Analyze Syntax

```python
func.lookup_string(<dict_table>, <value>)
```

## Analyze Examples

```python
func.lookup_string('status_dict', 'Active')

┌───┐
│ 1  │
└───┘
```

## SQL Syntax

```sql
LOOKUP_STRING(<dict_table>, <value>)
```

## SQL Examples

```sql
SELECT LOOKUP_STRING('status_dict', 'Active');

┌───┐
│ 1  │
└───┘
```
