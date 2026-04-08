---
title: OCTET_LENGTH
description: "Learn how to use the OCTET_LENGTH string function in PlaidCloud Lakehouse. OCTET_LENGTH() is a synonym for LENGTH(). Includes syntax and examples."
---

OCTET_LENGTH() is a synonym for LENGTH().

## Analyze Syntax

```python
func.octet_length(<str>)
```

## Analyze Examples

```python
func.octet_length('databend')
┌───────────────────────────────┐
│ func.octet_length('databend') │
├───────────────────────────────┤
│                             8 │
└───────────────────────────────┘
```

## SQL Syntax

```sql
OCTET_LENGTH(<str>)
```

## SQL Examples

```sql
SELECT OCTET_LENGTH('databend');
┌──────────────────────────┐
│ OCTET_LENGTH('databend') │
├──────────────────────────┤
│                        8 │
└──────────────────────────┘
```


