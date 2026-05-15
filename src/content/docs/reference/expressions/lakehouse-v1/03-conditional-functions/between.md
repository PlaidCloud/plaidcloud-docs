---
title: "[ NOT ] BETWEEN (Lakehouse v1)"
description: "[ NOT ] BETWEEN — true if a numeric, string, or date value lies inside (or outside) the given range."
---

Returns `true` if the given numeric or string ` <expr>` falls inside the defined lower and upper limits.

## Analyze Syntax

```python
table.column.between(<lower_limit>, <upper_limit>
```

## Analyze Examples

```python
table.column.between(0, 5)
```

## SQL Syntax

```sql
<expr> [ NOT ] BETWEEN <lower_limit> AND <upper_limit>
```

## SQL Examples

```sql
SELECT 'true' WHERE 5 BETWEEN 0 AND 5;

┌────────┐
│ 'true' │
├────────┤
│ true   │
└────────┘

SELECT 'true' WHERE 'data' BETWEEN 'data' AND 'databendcloud';

┌────────┐
│ 'true' │
├────────┤
│ true   │
└────────┘
```
