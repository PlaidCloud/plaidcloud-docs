---
title: TRANSLATE
description: "Learn how to use the TRANSLATE string function in PlaidCloud Lakehouse. Replaces characters in a string based on a character mapping - with syntax and examples."
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
