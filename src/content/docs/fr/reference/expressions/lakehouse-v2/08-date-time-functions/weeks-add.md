---
title: WEEKS_ADD (Lakehouse v2)
description: WEEKS_ADD — ajoute un nombre donné de semaines à une date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-add.md
---

Ajoute un nombre donné de semaines à une date.

## Syntaxe Analyze

```python
func.weeks_add(<date>, <n>)
```

## Exemples Analyze

```python
func.weeks_add('2024-01-01', 2)

┌──────────────┐
│ '2024-01-15'  │
└──────────────┘
```

## Syntaxe SQL

```sql
WEEKS_ADD(<date>, <n>)
```

## Exemples SQL

```sql
SELECT WEEKS_ADD('2024-01-01', 2);

┌────────────┐
│ 2024-01-15  │
└────────────┘
```
