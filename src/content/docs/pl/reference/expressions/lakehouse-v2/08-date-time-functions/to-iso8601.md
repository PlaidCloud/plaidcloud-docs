---
title: TO_ISO8601 (Lakehouse v2)
description: TO_ISO8601 — konwertuje datę lub datę i godzinę na ciąg znaków w formacie ISO 8601.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-iso8601.md
---

Konwertuje datę lub datę i godzinę na ciąg znaków w formacie ISO 8601.

## Składnia Analyze

```python
func.to_iso8601(<datetime>)
```

## Przykłady Analyze

```python
func.to_iso8601('2024-06-15 14:30:00')

┌───────────────────────┐
│ '2024-06-15T14:30:00'  │
└───────────────────────┘
```

## Składnia SQL

```sql
TO_ISO8601(<datetime>)
```

## Przykłady SQL

```sql
SELECT TO_ISO8601('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15T14:30:00  │
└─────────────────────┘
```
