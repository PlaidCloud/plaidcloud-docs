---
title: TRANSLATE (Lakehouse v2)
description: TRANSLATE — Replaces characters in a string based on a character mapping.
---

Replaces characters in a string based on a character mapping.

## Analyze Syntax

```python
func.translate(<str>, <from>, <to>)
```

## Analyze Examples

```python
func.translate('hello', 'el', 'ip')

┌─────────┐
│ 'hippo'  │
└─────────┘
```

## SQL Syntax

```sql
TRANSLATE(<str>, <from>, <to>)
```

## SQL Examples

```sql
SELECT TRANSLATE('hello', 'el', 'ip');

┌───────┐
│ hippo  │
└───────┘
```
