---
title: WEEKS_SUB (Lakehouse v2)
description: WEEKS_SUB — soustrait un nombre donné de semaines d'une date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-sub.md
---

Soustrait un nombre donné de semaines d'une date.

## Syntaxe Analyze

```python
func.weeks_sub(<date>, <n>)
```

## Exemples Analyze

```python
func.weeks_sub('2024-01-15', 2)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## Syntaxe SQL

```sql
WEEKS_SUB(<date>, <n>)
```

## Exemples SQL

```sql
SELECT WEEKS_SUB('2024-01-15', 2);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
