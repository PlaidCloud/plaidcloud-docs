---
title: DATE_TRUNC (Lakehouse v2)
description: DATE_TRUNC — tronque une valeur de date ou de date-heure à la précision indiquée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-trunc.md
---

Tronque une valeur de date ou de date-heure à la précision indiquée.

## Syntaxe Analyze

```python
func.date_trunc(<unit>, <datetime>)
```

## Exemples Analyze

```python
func.date_trunc('MONTH', '2024-06-15')

┌──────────────┐
│ '2024-06-01'  │
└──────────────┘
```

## Syntaxe SQL

```sql
DATE_TRUNC(<unit>, <datetime>)
```

## Exemples SQL

```sql
SELECT DATE_TRUNC('MONTH', '2024-06-15');

┌────────────┐
│ 2024-06-01  │
└────────────┘
```
