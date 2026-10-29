---
title: FROM_DAYS (Lakehouse v2)
description: FROM_DAYS – wandelt eine Tagesanzahl in ein Datum um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/from-days.md
---

Wandelt eine Tagesanzahl in ein Datum um.

## Analyze-Syntax

```python
func.from_days(<n>)
```

## Analyze-Beispiele

```python
func.from_days(738886)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQL-Syntax

```sql
FROM_DAYS(<n>)
```

## SQL-Beispiele

```sql
SELECT FROM_DAYS(738886);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
