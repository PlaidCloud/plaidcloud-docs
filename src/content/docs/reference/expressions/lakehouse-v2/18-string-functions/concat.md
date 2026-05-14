---
title: CONCAT
description: "Learn how to use the CONCAT string function in PlaidCloud Lakehouse. Concatenates two or more strings - see syntax, examples, and output."
---

Concatenates two or more strings.

## Analyze Syntax

```python
func.concat(<str1>, <str2>[, ...])
```

## Analyze Examples

```python
func.concat('Star', 'Rocks')

┌─────────────┐
│ 'StarRocks'  │
└─────────────┘
```

## SQL Syntax

```sql
CONCAT(<str1>, <str2>[, ...])
```

## SQL Examples

```sql
SELECT CONCAT('Star', 'Rocks');

┌───────────┐
│ StarRocks  │
└───────────┘
```
