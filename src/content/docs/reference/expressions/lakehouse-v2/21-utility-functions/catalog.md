---
title: CATALOG (Lakehouse v2)
description: CATALOG — returns the name of the current catalog.
---

Returns the name of the current catalog.

## Analyze Syntax

```python
func.catalog()
```

## Analyze Examples

```python
func.catalog()

┌───────────────────┐
│ 'default_catalog'  │
└───────────────────┘
```

## SQL Syntax

```sql
CATALOG()
```

## SQL Examples

```sql
SELECT CATALOG();

┌─────────────────┐
│ default_catalog  │
└─────────────────┘
```
