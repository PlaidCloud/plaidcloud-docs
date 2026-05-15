---
title: APPEND_TRAILING_CHAR_IF_ABSENT (Lakehouse v2)
description: "Use the APPEND_TRAILING_CHAR_IF_ABSENT string function in PlaidCloud Lakehouse. Appends a trailing character to a string if it is not already present."
---

Appends a trailing character to a string if it is not already present.

## Analyze Syntax

```python
func.append_trailing_char_if_absent(<str>, <char>)
```

## Analyze Examples

```python
func.append_trailing_char_if_absent('hello', '!')

┌──────────┐
│ 'hello!'  │
└──────────┘
```

## SQL Syntax

```sql
APPEND_TRAILING_CHAR_IF_ABSENT(<str>, <char>)
```

## SQL Examples

```sql
SELECT APPEND_TRAILING_CHAR_IF_ABSENT('hello', '!');

┌────────┐
│ hello!  │
└────────┘
```
