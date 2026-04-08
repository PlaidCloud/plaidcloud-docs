---
title: SUBSTRING_INDEX
description: "Use the SUBSTRING_INDEX string function in PlaidCloud Lakehouse. Returns a substring from a string before or after a specified number of delimiter occurrences."
---

Returns a substring from a string before or after a specified number of delimiter occurrences.

## Analyze Syntax

```python
func.substring_index(<str>, <delim>, <count>)
```

## Analyze Examples

```python
func.substring_index('www.example.com', '.', 2)

┌───────────────┐
│ 'www.example'  │
└───────────────┘
```

## SQL Syntax

```sql
SUBSTRING_INDEX(<str>, <delim>, <count>)
```

## SQL Examples

```sql
SELECT SUBSTRING_INDEX('www.example.com', '.', 2);

┌─────────────┐
│ www.example  │
└─────────────┘
```
