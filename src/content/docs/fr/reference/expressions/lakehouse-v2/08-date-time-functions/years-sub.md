---
title: YEARS_SUB (Lakehouse v2)
description: YEARS_SUB — soustrait un nombre donné d'années d'une date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-sub.md
---

Soustrait un nombre donné d'années d'une date.

## Syntaxe Analyze

```python
func.years_sub(<date>, <n>)
```

## Exemples Analyze

```python
func.years_sub('2029-01-01', 5)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## Syntaxe SQL

```sql
YEARS_SUB(<date>, <n>)
```

## Exemples SQL

```sql
SELECT YEARS_SUB('2029-01-01', 5);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
