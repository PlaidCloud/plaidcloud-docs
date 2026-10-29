---
title: YEARS_ADD (Lakehouse v2)
description: YEARS_ADD — ajoute un nombre donné d'années à une date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-add.md
---

Ajoute un nombre donné d'années à une date.

## Syntaxe Analyze

```python
func.years_add(<date>, <n>)
```

## Exemples Analyze

```python
func.years_add('2024-01-01', 5)

┌──────────────┐
│ '2029-01-01'  │
└──────────────┘
```

## Syntaxe SQL

```sql
YEARS_ADD(<date>, <n>)
```

## Exemples SQL

```sql
SELECT YEARS_ADD('2024-01-01', 5);

┌────────────┐
│ 2029-01-01  │
└────────────┘
```
