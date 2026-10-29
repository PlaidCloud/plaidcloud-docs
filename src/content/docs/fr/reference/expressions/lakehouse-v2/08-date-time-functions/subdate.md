---
title: SUBDATE (Lakehouse v2)
description: SUBDATE — soustrait un intervalle de temps d'une date. Alias de `DATE_SUB`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/subdate.md
---

Soustrait un intervalle de temps d'une date. Alias de `DATE_SUB`.

## Syntaxe Analyze

```python
func.subdate(<date>, INTERVAL <n> <unit>)
```

## Exemples Analyze

```python
func.subdate('2024-01-31', text('INTERVAL 7 DAY'))

┌──────────────┐
│ '2024-01-24'  │
└──────────────┘
```

## Syntaxe SQL

```sql
SUBDATE(<date>, INTERVAL <n> <unit>)
```

## Exemples SQL

```sql
SELECT SUBDATE('2024-01-31', INTERVAL 7 DAY);

┌────────────┐
│ 2024-01-24  │
└────────────┘
```
