---
title: DATABASE
---

Returns the name of the currently selected database. If no database is selected, then this function returns `default`.

## Analyze Syntax

```python
func.database()
```

## Analyze Examples

```python
func.database()

┌─────────────────┐
│ func.database() │
├─────────────────┤
│ default         │
└─────────────────┘
```

## SQL Syntax

```sql
DATABASE()
```

## SQL Examples

```sql
SELECT DATABASE();

┌────────────┐
│ database() │
├────────────┤
│ default    │
└────────────┘
```