---
title: TO_ISO8601 (Lakehouse v2)
description: TO_ISO8601 — converte uma data ou data e hora em uma string no formato ISO 8601.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-iso8601.md
---

Converte uma data ou data e hora em uma string no formato ISO 8601.

## Sintaxe do Analyze

```python
func.to_iso8601(<datetime>)
```

## Exemplos do Analyze

```python
func.to_iso8601('2024-06-15 14:30:00')

┌───────────────────────┐
│ '2024-06-15T14:30:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
TO_ISO8601(<datetime>)
```

## Exemplos de SQL

```sql
SELECT TO_ISO8601('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15T14:30:00  │
└─────────────────────┘
```
