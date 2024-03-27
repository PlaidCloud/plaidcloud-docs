---
title: LOWER
---

Returns a string with all characters changed to lowercase.

## SQL Syntax

```sql
LOWER(<str>)
```

## Aliases

- [LCASE](lcase.md)

## Return Type

VARCHAR

## SQL Examples

```sql
SELECT LOWER('Hello, PlaidCloud Lakehouse!'), LCASE('Hello, PlaidCloud Lakehouse!');

┌───────────────────────────────────────────────────────┐
│ lower('hello, databend!') │ lcase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ hello, databend!          │ hello, databend!          │
└───────────────────────────────────────────────────────┘
```