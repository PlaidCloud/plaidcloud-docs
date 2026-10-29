---
title: TO_DAYS (Lakehouse v2)
description: TO_DAYS – wandelt ein Datum in eine Tageszahl um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-days.md
---

Wandelt ein Datum in eine Tageszahl um.

## Analyze-Syntax

```python
func.to_days(<date>)
```

## Analyze-Beispiele

```python
func.to_days('2024-01-01')

┌────────┐
│ 738886  │
└────────┘
```

## SQL-Syntax

```sql
TO_DAYS(<date>)
```

## SQL-Beispiele

```sql
SELECT TO_DAYS('2024-01-01');

┌────────┐
│ 738886  │
└────────┘
```
