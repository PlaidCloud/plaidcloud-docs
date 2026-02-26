---
title: NVL
---

If `<expr1>` is NULL, returns `<expr2>`, otherwise returns `<expr1>`.

## Analyze Syntax

```python
func.nvl(<expr1>, <expr2>)
```

## Analyze Examples

```python
func.nvl(null, 'b'), func.nvl('a', 'b')

┌──────────────────────────────────────────┐
│ func.nvl(null, 'b') │ func.nvl('a', 'b') │
├─────────────────────┼────────────────────┤
│ b                   │ a                  │
└──────────────────────────────────────────┘

func.nvl(null, 2), func.nvl(1, 2)

┌────────────────────────────────────┐
│ func.nvl(null, 2) │ func.nvl(1, 2) │
├───────────────────┼────────────────┤
│                 2 │              1 │
└────────────────────────────────────┘
```

## SQL Syntax

```sql
NVL(<expr1>, <expr2>)
```

## Aliases

- [IFNULL](../ifnull)

## SQL Examples

```sql
SELECT NVL(NULL, 'b'), NVL('a', 'b');

┌────────────────────────────────┐
│ nvl(null, 'b') │ nvl('a', 'b') │
├────────────────┼───────────────┤
│ b              │ a             │
└────────────────────────────────┘

SELECT NVL(NULL, 2), NVL(1, 2);

┌──────────────────────────┐
│ nvl(null, 2) │ nvl(1, 2) │
├──────────────┼───────────┤
│            2 │         1 │
└──────────────────────────┘
```