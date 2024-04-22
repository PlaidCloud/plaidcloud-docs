---
title: CITY64WITHSEED
---

Calculates a City64WithSeed 64-bit hash for a string.

## Analyze Syntax

```python
func.city64withseed(<expr1>, <expr2>)
```

## Analyze Examples

```python
func.city64withseed('1234567890', 12)

+---------------------------------------+
| func.city64withseed('1234567890', 12) |
+---------------------------------------+
|                  10660895976650300430 |
+---------------------------------------+
```

## SQL Syntax

```sql
CITY64WITHSEED(<expr1>, <expr2>)
```

## SQL Examples

```sql
SELECT CITY64WITHSEED('1234567890', 12);

┌──────────────────────────────────┐
│ city64withseed('1234567890', 12) │
├──────────────────────────────────┤
│             10660895976650300430 │
└──────────────────────────────────┘
```