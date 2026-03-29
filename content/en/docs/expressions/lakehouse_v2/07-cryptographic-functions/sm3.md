---
title: SM3
---

Returns the SM3 hash of a string.

## Analyze Syntax

```python
func.sm3(<str>)
```

## Analyze Examples

```python
func.sm3('hello')

┌───────────────┐
│ 'becbbfaa...'  │
└───────────────┘
```

## SQL Syntax

```sql
SM3(<str>)
```

## SQL Examples

```sql
SELECT SM3('hello');

┌──────────────────────────────────────────────────────────────────┐
│ becbbfaae6548b8bf0cfcad5a27183cd1be6093b1cceccc303d9c61d0a645268  │
└──────────────────────────────────────────────────────────────────┘
```
