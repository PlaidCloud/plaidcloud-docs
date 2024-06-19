---
title: IF
---

If `<cond1>` is TRUE, it returns `<expr1>`. Otherwise if `<cond2>` is TRUE, it returns `<expr2>`, and so on.

## Analyze Syntax

```python
func.if(<cond1>, <expr1>, [<cond2>, <expr2> ...], <expr_else>)
```

## Analyze Examples

```python
func.if((1 > 2), 3, (4 < 5), 6, 7)

┌────────────────────────────────────┐
│ func.if((1 > 2), 3, (4 < 5), 6, 7) │
├────────────────────────────────────┤
│                                  6 │
└────────────────────────────────────┘
```

## SQL Syntax

```sql
IF(<cond1>, <expr1>, [<cond2>, <expr2> ...], <expr_else>)
```

## SQL Examples

```sql
SELECT IF(1 > 2, 3, 4 < 5, 6, 7);

┌───────────────────────────────┐
│ if((1 > 2), 3, (4 < 5), 6, 7) │
├───────────────────────────────┤
│                             6 │
└───────────────────────────────┘
```