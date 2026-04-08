---
title: DLOG10
description: "Learn how to use the DLOG10 math function in PlaidCloud Lakehouse. Alias for `LOG10`. See [LOG10](log10) - see syntax, examples, and output."
---

Alias for `LOG10`. See [LOG10](log10).

## Analyze Syntax

```python
func.dlog10(1000)
```

## Analyze Examples

```python
func.dlog10(1000)

┌─────┐
│ 3.0 │
└─────┘
```

## SQL Syntax

```sql
DLOG10(<x>)
```

## SQL Examples

```sql
SELECT DLOG10(1000);

┌─────┐
│ 3.0 │
└─────┘
```
