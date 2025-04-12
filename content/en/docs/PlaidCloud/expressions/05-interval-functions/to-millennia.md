---
title: TO_MILLENNIA
---

Converts a specified number of millennia into an Interval type.

- Accepts positive integers, zero, and negative integers as input.

## Analyze Syntax

```python
func.to_millennia(<millennia>)
```

## Analyze Examples

```python
func.to_millennia(2)
+------------------------------------------------------+
| func.to_millennia(2)                                 |
+------------------------------------------------------+
| 2000 years                                            |
+------------------------------------------------------+
```

## SQL Syntax

```sql
TO_MILLENNIA(<millennia>)
```

## Return Type

Interval (represented in years).

## SQL Examples

```sql
SELECT TO_MILLENNIA(2), TO_MILLENNIA(0), TO_MILLENNIA((- 2));

┌───────────────────────────────────────────────────────┐
│ to_millennia(2) │ to_millennia(0) │ to_millennia(- 2) │
├─────────────────┼─────────────────┼───────────────────┤
│ 2000 years      │ 00:00:00        │ -2000 years       │
└───────────────────────────────────────────────────────┘
```