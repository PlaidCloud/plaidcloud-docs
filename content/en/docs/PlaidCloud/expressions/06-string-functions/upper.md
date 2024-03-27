---
title: UPPER
---

Returns a string with all characters changed to uppercase.

## SQL Syntax

```sql
UPPER(<str>)
```

## Aliases

- [UCASE](ucase.md)

## Return Type

VARCHAR

## SQL Examples

```sql
SELECT UPPER('Hello, PlaidCloud Lakehouse!'), UCASE('Hello, PlaidCloud Lakehouse!');

┌───────────────────────────────────────────────────────┐
│ upper('hello, databend!') │ ucase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ HELLO, DATABEND!          │ HELLO, DATABEND!          │
└───────────────────────────────────────────────────────┘
```