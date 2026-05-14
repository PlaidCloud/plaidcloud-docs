---
title: HUMANIZE_NUMBER
description: "Learn how to use the HUMANIZE_NUMBER utility function in PlaidCloud Lakehouse. Returns a readable number. Includes usage and syntax details."
---

Returns a readable number.

## Analyze Syntax

```python
func.humanize_number(x);
```

## Analyze Examples

```python
func.humanize_number(1000 * 1000)
┌─────────────────────────────────────┐
│ func.humanize_number((1000 * 1000)) │
├─────────────────────────────────────┤
│ 1 million                           │
└─────────────────────────────────────┘
```

## SQL Syntax

```sql
HUMANIZE_NUMBER(x);
```

## Arguments

| Arguments | Description                |
|-----------|----------------------------|
| x         | The numerical size.        |


## Return Type

String.

## SQL Examples

```sql
SELECT HUMANIZE_NUMBER(1000 * 1000)
┌─────────────────────────┐
│ HUMANIZE_NUMBER((1000 * 1000)) │
├─────────────────────────┤
│ 1 million               │
└─────────────────────────┘
```
