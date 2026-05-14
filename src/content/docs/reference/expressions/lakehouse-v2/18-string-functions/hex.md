---
title: HEX
description: "Learn how to use the HEX string function in PlaidCloud Lakehouse. Returns the hexadecimal representation of a string or number - with syntax and examples."
---

Returns the hexadecimal representation of a string or number.

## Analyze Syntax

```python
func.hex(<expr>)
```

## Analyze Examples

```python
func.hex(255)

┌──────┐
│ 'FF'  │
└──────┘
```

## SQL Syntax

```sql
HEX(<expr>)
```

## SQL Examples

```sql
SELECT HEX(255);

┌────┐
│ FF  │
└────┘
```
