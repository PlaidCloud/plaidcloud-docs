---
title: VERSION (Lakehouse v2)
description: VERSION — gibt die MySQL-Protokollversion von StarRocks zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/version.md
---

Gibt die MySQL-Protokollversion von StarRocks zurück.

## Analyze-Syntax

```python
func.version()
```

## Analyze-Beispiele

```python
func.version()

┌─────────┐
│ '5.1.0'  │
└─────────┘
```

## SQL-Syntax

```sql
VERSION()
```

## SQL-Beispiele

```sql
SELECT VERSION();

┌───────┐
│ 5.1.0  │
└───────┘
```
