---
title: CURRENT_TIMEZONE (Lakehouse v2)
description: CURRENT_TIMEZONE — renvoie le fuseau horaire de la session en cours.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-timezone.md
---

Renvoie le fuseau horaire de la session en cours.

## Syntaxe Analyze

```python
func.current_timezone()
```

## Exemples Analyze

```python
func.current_timezone()

┌────────────────────┐
│ 'America/New_York'  │
└────────────────────┘
```

## Syntaxe SQL

```sql
CURRENT_TIMEZONE()
```

## Exemples SQL

```sql
SELECT CURRENT_TIMEZONE();

┌──────────────────┐
│ America/New_York  │
└──────────────────┘
```
