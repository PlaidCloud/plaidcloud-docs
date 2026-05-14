---
title: TODAY
description: "Learn how to use the TODAY datetime function in PlaidCloud Lakehouse. Returns current date. Includes detailed syntax, examples, and usage reference."
---

Returns current date.

## Analyze Syntax

```python
func.today()
```

## Analyze Examples

```python
func.today()
┌──────────────┐
│ func.today() │
├──────────────┤
│ 2021-09-03   │
└──────────────┘
```

## SQL Syntax

```sql
TODAY()
```

## Return Type

`DATE`, returns date in “YYYY-MM-DD” format.

## SQL Examples

```sql
SELECT TODAY();
┌────────────┐
│ TODAY()    │
├────────────┤
│ 2021-09-03 │
└────────────┘
```
