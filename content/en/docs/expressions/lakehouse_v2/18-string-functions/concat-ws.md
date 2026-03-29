---
title: CONCAT_WS
---

Concatenates strings with a separator.

## Analyze Syntax

```python
func.concat_ws(<sep>, <str1>, <str2>[, ...])
```

## Analyze Examples

```python
func.concat_ws('-', '2024', '01', '15')

┌──────────────┐
│ '2024-01-15'  │
└──────────────┘
```

## SQL Syntax

```sql
CONCAT_WS(<sep>, <str1>, <str2>[, ...])
```

## SQL Examples

```sql
SELECT CONCAT_WS('-', '2024', '01', '15');

┌────────────┐
│ 2024-01-15  │
└────────────┘
```
