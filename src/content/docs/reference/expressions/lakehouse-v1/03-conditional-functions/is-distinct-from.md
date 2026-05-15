---
title: "IS [ NOT ] DISTINCT FROM (Lakehouse v1)"
description: IS [ NOT ] DISTINCT FROM — compares whether two expressions are equal (or not equal) with awareness of nullability, meaning it treats NULLs as known values.
---

Compares whether two expressions are equal (or not equal) with awareness of nullability, meaning it treats NULLs as known values for comparing equality.

## SQL Syntax

```sql
<expr1> IS [ NOT ] DISTINCT FROM <expr2>
```

## SQL Examples

```sql
SELECT NULL IS DISTINCT FROM NULL;

┌────────────────────────────┐
│ null is distinct from null │
├────────────────────────────┤
│ false                      │
└────────────────────────────┘
```
