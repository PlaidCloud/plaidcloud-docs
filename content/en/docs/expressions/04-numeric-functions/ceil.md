---
title: CEIL
---

Rounds the number up.

## Analyze Syntax

```python
func.ceil( <x> )
```

## Analyze Examples

```python
func.ceil((- 1.23))

┌─────────────────────┐
│ func.ceil((- 1.23)) │
├─────────────────────┤
│                  -1 │ 
└─────────────────────┘
```

## SQL Syntax

```sql
CEIL( <x> )
```

## Aliases

- [CEILING](../ceiling)

## SQL Examples

```sql
SELECT CEILING(-1.23), CEIL(-1.23);

┌────────────────────────────────────┐
│ ceiling((- 1.23)) │ ceil((- 1.23)) │
├───────────────────┼────────────────┤
│                -1 │             -1 │
└────────────────────────────────────┘
```