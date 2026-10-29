---
title: TIMESTAMP (Lakehouse v2)
description: TIMESTAMP — convertit une date ou une chaîne en date-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestamp.md
---

Convertit une date ou une chaîne en date-heure.

## Syntaxe Analyze

```python
func.timestamp(<expr>)
```

## Exemples Analyze

```python
func.timestamp('2024-06-15')

┌───────────────────────┐
│ '2024-06-15 00:00:00'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
TIMESTAMP(<expr>)
```

## Exemples SQL

```sql
SELECT TIMESTAMP('2024-06-15');

┌─────────────────────┐
│ 2024-06-15 00:00:00  │
└─────────────────────┘
```
