---
title: TO_ISO8601 (Lakehouse v2)
description: TO_ISO8601 — convertit une date ou une date-heure en chaîne au format ISO 8601.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-iso8601.md
---

Convertit une date ou une date-heure en chaîne au format ISO 8601.

## Syntaxe Analyze

```python
func.to_iso8601(<datetime>)
```

## Exemples Analyze

```python
func.to_iso8601('2024-06-15 14:30:00')

┌───────────────────────┐
│ '2024-06-15T14:30:00'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
TO_ISO8601(<datetime>)
```

## Exemples SQL

```sql
SELECT TO_ISO8601('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15T14:30:00  │
└─────────────────────┘
```
