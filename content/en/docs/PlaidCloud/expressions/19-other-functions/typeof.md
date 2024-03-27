---
title: TYPEOF
---

TYPEOF function is used to return the name of a data type.

## SQL Syntax

```sql
TYPEOF( <expr> )
```

## Arguments

| Arguments   | Description |
| ----------- | ----------- |
| `<expr>` | Any expression. <br /> This may be a column name, the result of another function, or a math operation.

## Return Type

String

## SQL Examples

```sql
SELECT typeof(1::INT);
+------------------+
| typeof(1::Int32) |
+------------------+
| INT              |
+------------------+
```
