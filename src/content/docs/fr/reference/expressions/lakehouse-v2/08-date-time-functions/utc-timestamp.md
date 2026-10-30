---
title: UTC_TIMESTAMP (Lakehouse v2)
description: UTC_TIMESTAMP — renvoie la date et l'heure UTC actuelles.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/utc-timestamp.md
---

Renvoie la date et l'heure UTC actuelles.

## Syntaxe Analyze

```python
func.utc_timestamp()
```

## Exemples Analyze

```python
func.utc_timestamp()

┌───────────────────────┐
│ '2024-06-15 18:30:00'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
UTC_TIMESTAMP()
```

## Exemples SQL

```sql
SELECT UTC_TIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 18:30:00  │
└─────────────────────┘
```
