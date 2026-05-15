---
title: STRING_TO_H3 (Lakehouse v1)
description: STRING_TO_H3 — converts the string representation to H3 (uint64) representation.
---

Converts the string representation to [H3](https://eng.uber.com/h3/) (uint64) representation.

## Analyze Syntax

```python
func.string_to_h3(h3)
```

## Analyze Examples

```python
func.string_to_h3('8d11aa6a38826ff')

┌──────────────────────────────────────┐
│ func.string_to_h3('8d11aa6a38826ff') │
├──────────────────────────────────────┤
│                   635318325446452991 │
└──────────────────────────────────────┘
```

## SQL Syntax

```sql
STRING_TO_H3(h3)
```

## SQL Examples

```sql
SELECT STRING_TO_H3('8d11aa6a38826ff');

┌─────────────────────────────────┐
│ string_to_h3('8d11aa6a38826ff') │
├─────────────────────────────────┤
│              635318325446452991 │
└─────────────────────────────────┘
```
