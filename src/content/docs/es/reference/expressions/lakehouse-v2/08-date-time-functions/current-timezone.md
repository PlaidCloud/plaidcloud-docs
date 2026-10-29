---
title: CURRENT_TIMEZONE (Lakehouse v2)
description: CURRENT_TIMEZONE — devuelve la zona horaria de la sesión actual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-timezone.md
---

Devuelve la zona horaria de la sesión actual.

## Sintaxis de Analyze

```python
func.current_timezone()
```

## Ejemplos de Analyze

```python
func.current_timezone()

┌────────────────────┐
│ 'America/New_York'  │
└────────────────────┘
```

## Sintaxis de SQL

```sql
CURRENT_TIMEZONE()
```

## Ejemplos de SQL

```sql
SELECT CURRENT_TIMEZONE();

┌──────────────────┐
│ America/New_York  │
└──────────────────┘
```
