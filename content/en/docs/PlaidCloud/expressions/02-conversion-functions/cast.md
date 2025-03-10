---
title: "CAST, ::"
---

Converts a value from one data type to another. `::` is an alias for CAST.

See also: [TRY_CAST](../try-cast)

## Analyze Syntax

```python
func.cast( <expr>, <data_type> )
```

## Analyze Examples

```python
func.cast(1, string), func.to_string(1)

┌───────────────────────────────────────────┐
│ func.cast(1, string) │ func.to_string(1)  │
├──────────────────────┼────────────────────┤
│ 1                    │ 1                  │
└───────────────────────────────────────────┘
```

## SQL Syntax

```sql
CAST( <expr> AS <data_type> )

<expr>::<data_type>
```

## SQL Examples

```sql
SELECT CAST(1 AS VARCHAR), 1::VARCHAR;

┌───────────────────────────────┐
│ cast(1 as string) │ 1::string │
├───────────────────┼───────────┤
│ 1                 │ 1         │
└───────────────────────────────┘
```