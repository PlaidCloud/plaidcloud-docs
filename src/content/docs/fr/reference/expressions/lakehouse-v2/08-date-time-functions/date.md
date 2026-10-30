---
title: DATE (Lakehouse v2)
description: DATE — extrait la partie date d'une expression de date-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date.md
---

Extrait la partie date d'une expression de date-heure.

## Syntaxe Analyze

```python
func.date(<datetime>)
```

## Exemples Analyze

```python
func.date('2024-06-15 14:30:00')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Syntaxe SQL

```sql
DATE(<datetime>)
```

## Exemples SQL

```sql
SELECT DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
