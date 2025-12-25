---
title: GET
---

Returns an element from an array by index (1-based).

## Analyze Syntax

```python
func.get( <array>, <index> )
```

## Analyze Examples

```python
func.get([1, 2], 2)

┌─────────────────────┐
│ func.get([1, 2], 2) │
├─────────────────────┤
│                   2 │
└─────────────────────┘
```

## SQL Syntax

```sql
GET( <array>, <index> )
```

## Aliases

- [ARRAY_GET](../array-get)

## SQL Examples

```sql
SELECT GET([1, 2], 2), ARRAY_GET([1, 2], 2);

┌───────────────────────────────────────┐
│ get([1, 2], 2) │ array_get([1, 2], 2) │
├────────────────┼──────────────────────┤
│              2 │                    2 │
└───────────────────────────────────────┘
```