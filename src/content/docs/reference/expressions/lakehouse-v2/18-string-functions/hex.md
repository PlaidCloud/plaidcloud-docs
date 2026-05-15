---
title: HEX (Lakehouse v2)
description: HEX — Returns the hexadecimal representation of a string or number.
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
