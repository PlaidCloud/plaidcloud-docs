---
title: CURRENT_VERSION (Lakehouse v2)
description: CURRENT_VERSION — gibt die aktuelle Version von StarRocks zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-version.md
---

Gibt die aktuelle Version von StarRocks zurück.

## Analyze-Syntax

```python
func.current_version()
```

## Analyze-Beispiele

```python
func.current_version()

┌─────────┐
│ '4.1.0'  │
└─────────┘
```

## SQL-Syntax

```sql
CURRENT_VERSION()
```

## SQL-Beispiele

```sql
SELECT CURRENT_VERSION();

┌──────────────┐
│ 4.1.0-xxxxxx  │
└──────────────┘
```
