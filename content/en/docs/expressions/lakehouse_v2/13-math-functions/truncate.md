---
title: TRUNCATE
description: "Learn how to use the TRUNCATE math function in PlaidCloud Lakehouse. Truncates a number to a specified number of decimal places - with syntax and examples."
---

Truncates a number to a specified number of decimal places.

## Analyze Syntax

```python
func.truncate(<x>, <d>)
```

## Analyze Examples

```python
func.truncate(3.14159, 2)

┌──────┐
│ 3.14  │
└──────┘
```

## SQL Syntax

```sql
TRUNCATE(<x>, <d>)
```

## SQL Examples

```sql
SELECT TRUNCATE(3.14159, 2);

┌──────┐
│ 3.14  │
└──────┘
```
