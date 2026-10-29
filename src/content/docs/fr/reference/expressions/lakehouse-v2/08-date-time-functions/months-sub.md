---
title: MONTHS_SUB (Lakehouse v2)
description: MONTHS_SUB — soustrait un nombre donné de mois d'une date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-sub.md
---

Soustrait un nombre donné de mois d'une date.

## Syntaxe Analyze

```python
func.months_sub(<date>, <n>)
```

## Exemples Analyze

```python
func.months_sub('2024-06-15', 3)

┌──────────────┐
│ '2024-03-15'  │
└──────────────┘
```

## Syntaxe SQL

```sql
MONTHS_SUB(<date>, <n>)
```

## Exemples SQL

```sql
SELECT MONTHS_SUB('2024-06-15', 3);

┌────────────┐
│ 2024-03-15  │
└────────────┘
```
