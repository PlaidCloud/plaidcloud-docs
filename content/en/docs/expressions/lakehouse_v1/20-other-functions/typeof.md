---
title: TYPEOF
description: "Learn how to use the TYPEOF utility function in PlaidCloud Lakehouse. TYPEOF function is used to return the name of a data type. Includes syntax and examples."
---

TYPEOF function is used to return the name of a data type.

## Analyze Syntax

```python
func.typeof( <expr> )
```

## Analyze Examples

```python
func.typeof(1)
┌──────────────────┐
│ func.typeof(1)   │
├──────────────────┤
│ INT              │
└──────────────────┘
```

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
┌──────────────────┐
│ typeof(1::Int32) │
├──────────────────┤
│ INT              │
└──────────────────┘
```
