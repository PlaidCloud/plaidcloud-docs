---
title: TO_DATETIME (Lakehouse v2)
description: TO_DATETIME — convertit une valeur en date-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-datetime.md
---

Convertit une valeur en date-heure.

## Syntaxe Analyze

```python
func.to_datetime(<expr>)
```

## Exemples Analyze

```python
func.to_datetime('2024-06-15')

┌───────────────────────┐
│ '2024-06-15 00:00:00'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
TO_DATETIME(<expr>)
```

## Exemples SQL

```sql
SELECT TO_DATETIME('2024-06-15');

┌─────────────────────┐
│ 2024-06-15 00:00:00  │
└─────────────────────┘
```
