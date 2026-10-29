---
title: FROM_UNIXTIME (Lakehouse v2)
description: FROM_UNIXTIME — convertit un horodatage Unix en chaîne de date-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/from-unixtime.md
---

Convertit un horodatage Unix en chaîne de date-heure.

## Syntaxe Analyze

```python
func.from_unixtime(<timestamp>[, <format>])
```

## Exemples Analyze

```python
func.from_unixtime(1704067200)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
FROM_UNIXTIME(<timestamp>[, <format>])
```

## Exemples SQL

```sql
SELECT FROM_UNIXTIME(1704067200);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
