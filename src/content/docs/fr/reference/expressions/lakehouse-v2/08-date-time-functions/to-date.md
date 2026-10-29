---
title: TO_DATE (Lakehouse v2)
description: TO_DATE — convertit une date-heure en date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-date.md
---

Convertit une date-heure en date.

## Syntaxe Analyze

```python
func.to_date(<datetime>)
```

## Exemples Analyze

```python
func.to_date('2024-06-15 14:30:00')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Syntaxe SQL

```sql
TO_DATE(<datetime>)
```

## Exemples SQL

```sql
SELECT TO_DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
