---
title: MONEY_FORMAT
---

Formats a number as a currency string with commas and two decimal places.

## Analyze Syntax

```python
func.money_format(<num>)
```

## Analyze Examples

```python
func.money_format(1234567.89)

┌────────────────┐
│ '1,234,567.89'  │
└────────────────┘
```

## SQL Syntax

```sql
MONEY_FORMAT(<num>)
```

## SQL Examples

```sql
SELECT MONEY_FORMAT(1234567.89);

┌──────────────┐
│ 1,234,567.89  │
└──────────────┘
```
