---
title: TRY_CAST
description: "Learn how to use the TRY_CAST conversion function in PlaidCloud Lakehouse. Converts a value from one data type to another. Includes syntax and examples."
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