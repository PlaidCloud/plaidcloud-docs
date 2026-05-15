---
title: REGEXP_EXTRACT_ALL (Lakehouse v2)
description: REGEXP_EXTRACT_ALL — extracts all substrings that match a regular expression pattern.
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
