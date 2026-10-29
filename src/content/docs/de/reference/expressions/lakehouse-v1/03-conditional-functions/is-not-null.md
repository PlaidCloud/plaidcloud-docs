---
title: IS_NOT_NULL (Lakehouse v1)
description: IS_NOT_NULL – prüft, ob ein Wert nicht NULL ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-not-null.md
---

Prüft, ob ein Wert nicht NULL ist.

## Analyze-Syntax

```python
func.is_not_null(<expr>)
```

## Analyze-Beispiele

```python
func.is_not_null(1)

┌─────────────────────┐
│ func.is_not_null(1) │
├─────────────────────┤
│ true                │
└─────────────────────┘
```

## SQL-Syntax

```sql
IS_NOT_NULL(<expr>)
```

## SQL-Beispiele

```sql
SELECT IS_NOT_NULL(1);

┌────────────────┐
│ is_not_null(1) │
├────────────────┤
│ true           │
└────────────────┘
```
