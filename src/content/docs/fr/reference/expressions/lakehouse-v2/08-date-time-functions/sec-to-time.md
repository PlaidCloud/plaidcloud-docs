---
title: SEC_TO_TIME (Lakehouse v2)
description: SEC_TO_TIME — convertit des secondes en valeur d'heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/sec-to-time.md
---

Convertit des secondes en valeur d'heure.

## Syntaxe Analyze

```python
func.sec_to_time(<seconds>)
```

## Exemples Analyze

```python
func.sec_to_time(3661)

┌────────────┐
│ '01:01:01'  │
└────────────┘
```

## Syntaxe SQL

```sql
SEC_TO_TIME(<seconds>)
```

## Exemples SQL

```sql
SELECT SEC_TO_TIME(3661);

┌──────────┐
│ 01:01:01  │
└──────────┘
```
