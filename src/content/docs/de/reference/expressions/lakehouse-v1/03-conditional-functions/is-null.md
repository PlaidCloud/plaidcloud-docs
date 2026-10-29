---
title: IS_NULL (Lakehouse v1)
description: IS_NULL – prüft, ob ein Wert NULL ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-null.md
---

Prüft, ob ein Wert NULL ist.

## Analyze-Syntax

```python
func.is_null(<expr>)
```

## Analyze-Beispiele

```python
func.is_null(1)

┌─────────────────┐
│ func.is_null(1) │
├─────────────────┤
│ false           │
└─────────────────┘
```

## SQL-Syntax

```sql
IS_NULL(<expr>)
```

## SQL-Beispiele

```sql
SELECT IS_NULL(1);

┌────────────┐
│ is_null(1) │
├────────────┤
│ false      │
└────────────┘
```
