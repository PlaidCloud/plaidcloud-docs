---
title: REGEXP_EXTRACT_ALL
description: "Learn how to use the REGEXP_EXTRACT_ALL pattern matching function in PlaidCloud Lakehouse. Extracts all substrings that match a regular expression pattern."
---

Extracts all substrings that match a regular expression pattern.

## Analyze Syntax

```python
func.regexp_extract_all(<str>, <pattern>)
```

## Analyze Examples

```python
func.regexp_extract_all('a1b2c3', '\\d+')

┌───────────────┐
│ ['1','2','3']  │
└───────────────┘
```

## SQL Syntax

```sql
REGEXP_EXTRACT_ALL(<str>, <pattern>)
```

## SQL Examples

```sql
SELECT REGEXP_EXTRACT_ALL('a1b2c3', '\\d+');

┌───────────────┐
│ ["1","2","3"]  │
└───────────────┘
```
