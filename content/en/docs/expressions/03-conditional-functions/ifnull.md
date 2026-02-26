---
title: IFNULL
---

If `<expr1>` is NULL, returns `<expr2>`, otherwise returns `<expr1>`.

## Analyze Syntax

```python
func.ifnull(<expr1>, <expr2>)
```

## Analyze Examples

```python
func.ifnull(null, 'b'), func.ifnull('a', 'b')

┌────────────────────────────────────────────────┐
│ func.ifnull(null, 'b') │ func.ifnull('a', 'b') │
├────────────────────────┼───────────────────────┤
│ b                      │ a                     │
└────────────────────────────────────────────────┘

func.ifnull(null, 2), func.ifnull(1, 2)

┌──────────────────────────────────────────┐
│ func.ifnull(null, 2) │ func.ifnull(1, 2) │
├──────────────────────┼───────────────────┤
│                    2 │                 1 │
└──────────────────────────────────────────┘
```

## SQL Syntax

```sql
IFNULL(<expr1>, <expr2>)
```

## Aliases

- [NVL](../nvl)

## SQL Examples

```sql
SELECT IFNULL(NULL, 'b'), IFNULL('a', 'b');

┌──────────────────────────────────────┐
│ ifnull(null, 'b') │ ifnull('a', 'b') │
├───────────────────┼──────────────────┤
│ b                 │ a                │
└──────────────────────────────────────┘

SELECT IFNULL(NULL, 2), IFNULL(1, 2);

┌────────────────────────────────┐
│ ifnull(null, 2) │ ifnull(1, 2) │
├─────────────────┼──────────────┤
│               2 │            1 │
└────────────────────────────────┘
```