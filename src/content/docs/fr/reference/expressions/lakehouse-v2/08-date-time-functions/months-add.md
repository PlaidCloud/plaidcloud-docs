---
title: MONTHS_ADD (Lakehouse v2)
description: MONTHS_ADD — ajoute un nombre donné de mois à une date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-add.md
---

Ajoute un nombre donné de mois à une date.

## Syntaxe Analyze

```python
func.months_add(<date>, <n>)
```

## Exemples Analyze

```python
func.months_add('2024-01-15', 3)

┌──────────────┐
│ '2024-04-15'  │
└──────────────┘
```

## Syntaxe SQL

```sql
MONTHS_ADD(<date>, <n>)
```

## Exemples SQL

```sql
SELECT MONTHS_ADD('2024-01-15', 3);

┌────────────┐
│ 2024-04-15  │
└────────────┘
```
