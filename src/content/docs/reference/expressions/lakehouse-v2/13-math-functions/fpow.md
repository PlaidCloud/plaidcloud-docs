---
title: FPOW (Lakehouse v2)
description: FPOW — alias for `POW`. See [POW](../pow/).
---

Alias for `POW`. See [POW](../pow/).

## Analyze Syntax

```python
func.fpow(2, 10)
```

## Analyze Examples

```python
func.fpow(2, 10)

┌────────┐
│ 1024.0 │
└────────┘
```

## SQL Syntax

```sql
FPOW(<x>)
```

## SQL Examples

```sql
SELECT FPOW(2, 10);

┌────────┐
│ 1024.0 │
└────────┘
```
