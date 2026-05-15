---
title: REGEXP_EXTRACT
description: REGEXP_EXTRACT — extracts the first substring that matches a regular expression pattern.
---

Extracts the first substring that matches a regular expression pattern.

## Analyze Syntax

```python
func.regexp_extract(<str>, <pattern>[, <group>])
```

## Analyze Examples

```python
func.regexp_extract('price: $42.50', '\\$(\\d+\\.\\d+)', 1)

┌─────────┐
│ '42.50'  │
└─────────┘
```

## SQL Syntax

```sql
REGEXP_EXTRACT(<str>, <pattern>[, <group>])
```

## SQL Examples

```sql
SELECT REGEXP_EXTRACT('price: $42.50', '\\$(\\d+\\.\\d+)', 1);

┌───────┐
│ 42.50  │
└───────┘
```
