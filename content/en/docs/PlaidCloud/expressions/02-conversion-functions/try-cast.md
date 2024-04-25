---
title: TRY_CAST
---

Converts a value from one data type to another. Returns NULL on error.

See also: [CAST](../cast)

## Analyze Syntax

```python
func.try_cast( <expr>, <data_type> )
```

## Analyze Examples

```python
func.try_cast(1, string)

┌──────────────────────────┐
│ func.try_cast(1, string) │
├──────────────────────────┤
│ 1                        │
└──────────────────────────┘
```

## SQL Syntax

```sql
TRY_CAST( <expr> AS <data_type> )
```

## SQL Examples

```sql
SELECT TRY_CAST(1 AS VARCHAR);

┌───────────────────────┐
│ try_cast(1 as string) │
├───────────────────────┤
│ 1                     │
└───────────────────────┘
```