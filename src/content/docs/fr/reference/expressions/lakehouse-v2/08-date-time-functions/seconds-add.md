---
title: SECONDS_ADD (Lakehouse v2)
description: SECONDS_ADD — ajoute un nombre donné de secondes à une date-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-add.md
---

Ajoute un nombre donné de secondes à une date-heure.

## Syntaxe Analyze

```python
func.seconds_add(<datetime>, <n>)
```

## Exemples Analyze

```python
func.seconds_add('2024-01-01 00:00:00', 90)

┌───────────────────────┐
│ '2024-01-01 00:01:30'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
SECONDS_ADD(<datetime>, <n>)
```

## Exemples SQL

```sql
SELECT SECONDS_ADD('2024-01-01 00:00:00', 90);

┌─────────────────────┐
│ 2024-01-01 00:01:30  │
└─────────────────────┘
```
