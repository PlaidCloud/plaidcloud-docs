---
title: MICROSECONDS_SUB (Lakehouse v2)
description: MICROSECONDS_SUB — soustrait un nombre donné de microsecondes d'une date-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/microseconds-sub.md
---

Soustrait un nombre donné de microsecondes d'une date-heure.

## Syntaxe Analyze

```python
func.microseconds_sub(<datetime>, <n>)
```

## Exemples Analyze

```python
func.microseconds_sub('2024-01-01 00:00:01', 1000000)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
MICROSECONDS_SUB(<datetime>, <n>)
```

## Exemples SQL

```sql
SELECT MICROSECONDS_SUB('2024-01-01 00:00:01', 1000000);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
