---
title: MICROSECONDS_ADD (Lakehouse v2)
description: MICROSECONDS_ADD — ajoute un nombre donné de microsecondes à une date-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/microseconds-add.md
---

Ajoute un nombre donné de microsecondes à une date-heure.

## Syntaxe Analyze

```python
func.microseconds_add(<datetime>, <n>)
```

## Exemples Analyze

```python
func.microseconds_add('2024-01-01 00:00:00', 1000000)

┌───────────────────────┐
│ '2024-01-01 00:00:01'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
MICROSECONDS_ADD(<datetime>, <n>)
```

## Exemples SQL

```sql
SELECT MICROSECONDS_ADD('2024-01-01 00:00:00', 1000000);

┌─────────────────────┐
│ 2024-01-01 00:00:01  │
└─────────────────────┘
```
