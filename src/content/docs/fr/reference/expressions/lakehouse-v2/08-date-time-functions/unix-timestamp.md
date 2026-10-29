---
title: UNIX_TIMESTAMP (Lakehouse v2)
description: UNIX_TIMESTAMP — convertit une date-heure en horodatage Unix.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/unix-timestamp.md
---

Convertit une date-heure en horodatage Unix.

## Syntaxe Analyze

```python
func.unix_timestamp([<datetime>])
```

## Exemples Analyze

```python
func.unix_timestamp('2024-01-01 00:00:00')

┌────────────┐
│ 1704067200  │
└────────────┘
```

## Syntaxe SQL

```sql
UNIX_TIMESTAMP([<datetime>])
```

## Exemples SQL

```sql
SELECT UNIX_TIMESTAMP('2024-01-01 00:00:00');

┌────────────┐
│ 1704067200  │
└────────────┘
```
