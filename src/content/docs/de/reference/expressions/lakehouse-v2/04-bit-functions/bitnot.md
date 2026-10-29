---
title: BITNOT (Lakehouse v2)
description: BITNOT – gibt das bitweise NICHT eines numerischen Werts zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitnot.md
---

Gibt das bitweise NICHT eines numerischen Werts zurück.

## Analyze-Syntax

```python
func.bitnot(<x>)
```

## Analyze-Beispiele

```python
func.bitnot(0)

┌──────┐
│ '-1'  │
└──────┘
```

## SQL-Syntax

```sql
BITNOT(<x>)
```

## SQL-Beispiele

```sql
SELECT BITNOT(0);

┌────┐
│ -1  │
└────┘
```
