---
title: DLOG10 (Lakehouse v2)
description: DLOG10 — alias for `LOG10`. See [LOG10](log10).
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
