---
title: ADDDATE (Lakehouse v2)
description: ADDDATE — ajoute un intervalle de temps donné à une date. Alias de `DATE_ADD`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/adddate.md
---

Ajoute un intervalle de temps donné à une date. Alias de `DATE_ADD`.

## Syntaxe Analyze

```python
func.adddate(<date>, INTERVAL <n> <unit>)
```

## Exemples Analyze

```python
func.adddate('2024-01-01', text('INTERVAL 7 DAY'))

┌──────────────┐
│ '2024-01-08'  │
└──────────────┘
```

## Syntaxe SQL

```sql
ADDDATE(<date>, INTERVAL <n> <unit>)
```

## Exemples SQL

```sql
SELECT ADDDATE('2024-01-01', INTERVAL 7 DAY);

┌────────────┐
│ 2024-01-08  │
└────────────┘
```
