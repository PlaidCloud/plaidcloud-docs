---
title: LOWER
description: "Learn how to use the LOWER string function in PlaidCloud Lakehouse. Returns a string with all characters changed to lowercase. Includes syntax and examples."
---

Returns a string with all characters changed to lowercase.

## Analyze Syntax

```python
func.lower(<str>)
```

## Analyze Examples

```python
func.lower('Hello, PlaidCloud!')
┌──────────────────────────────────┐
│ func.lower('Hello, PlaidCloud!') │
├──────────────────────────────────┤
│ hello, plaidcloud!               │
└──────────────────────────────────┘
```

## SQL Syntax

```sql
LOWER(<str>)
```

## Aliases

- [LCASE](../lcase)

## Return Type

VARCHAR

## SQL Examples

```sql
SELECT LOWER('Hello, Databend!'), LCASE('Hello, Databend!');

┌───────────────────────────────────────────────────────┐
│ lower('hello, databend!') │ lcase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ hello, databend!          │ hello, databend!          │
└───────────────────────────────────────────────────────┘
```