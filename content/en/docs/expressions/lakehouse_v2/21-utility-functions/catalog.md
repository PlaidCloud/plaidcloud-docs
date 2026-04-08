---
title: CATALOG
description: "Learn how to use the CATALOG utility function in PlaidCloud Lakehouse. Returns the name of the current catalog - see syntax, examples, and output."
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
