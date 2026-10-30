---
title: UTC_TIME (Lakehouse v2)
description: UTC_TIME — renvoie l'heure UTC actuelle.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/utc-time.md
---

Renvoie l'heure UTC actuelle.

## Syntaxe Analyze

```python
func.utc_time()
```

## Exemples Analyze

```python
func.utc_time()

┌────────────┐
│ '18:30:00'  │
└────────────┘
```

## Syntaxe SQL

```sql
UTC_TIME()
```

## Exemples SQL

```sql
SELECT UTC_TIME();

┌──────────┐
│ 18:30:00  │
└──────────┘
```
