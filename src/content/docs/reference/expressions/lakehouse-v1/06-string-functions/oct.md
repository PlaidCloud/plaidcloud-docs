---
title: OCT (Lakehouse v1)
description: OCT — Returns a string representation of the octal value of N.
---

Returns a string representation of the octal value of N.

## Analyze Syntax

```python
func.oct(<expr>)
```

## Analyze Examples

```python
func.oct(12)
┌─────────────────┐
│ func.oct(12)    │
├─────────────────┤
│ 014             │
└─────────────────┘
```

## SQL Syntax

```sql
OCT(<expr>)
```

## SQL Examples

```sql
SELECT OCT(12);
┌─────────┐
│ OCT(12) │
├─────────┤
│ 014     │
└─────────┘
```
