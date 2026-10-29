---
title: DATE_SUB (Lakehouse v2)
description: DATE_SUB — soustrait un intervalle de temps donné d'une date ou d'une date-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-sub.md
---

Soustrait un intervalle de temps donné d'une date ou d'une date-heure.

## Syntaxe Analyze

```python
func.date_sub(<date>, INTERVAL <n> <unit>)
```

## Exemples Analyze

```python
func.date_sub('2024-03-01', text('INTERVAL 1 MONTH'))

┌──────────────┐
│ '2024-02-01'  │
└──────────────┘
```

## Syntaxe SQL

```sql
DATE_SUB(<date>, INTERVAL <n> <unit>)
```

## Exemples SQL

```sql
SELECT DATE_SUB('2024-03-01', INTERVAL 1 MONTH);

┌────────────┐
│ 2024-02-01  │
└────────────┘
```
