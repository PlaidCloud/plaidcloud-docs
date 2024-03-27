---
title: TO_INT8
---

Converts a value to INT8 data type.

## SQL Syntax

```sql
TO_INT8( <expr> )
```

## SQL Examples

```sql
SELECT TO_INT8('123');

┌────────────────┐
│ to_int8('123') │
│      UInt8     │
├────────────────┤
│            123 │
└────────────────┘
```