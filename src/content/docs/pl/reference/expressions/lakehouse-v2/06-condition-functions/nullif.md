---
title: NULLIF (Lakehouse v2)
description: NULLIF — zwraca NULL, jeśli dwa wyrażenia są równe; w przeciwnym razie zwraca pierwsze wyrażenie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/nullif.md
---

Zwraca NULL, jeśli dwa wyrażenia są równe; w przeciwnym razie zwraca pierwsze wyrażenie.

## Składnia Analyze

```python
func.nullif(get_column(table, 'value'), 0)
```

## Przykłady Analyze

```python
func.nullif(get_column(table, 'divisor'), 0)
```

## Składnia SQL

```sql
NULLIF(<value>, 0)
```

## Przykłady SQL

```sql
SELECT 100 / NULLIF(divisor, 0) AS safe_division FROM calculations;

┌───────────────┐
│ safe_division │
├───────────────┤
│         50.00 │
│          NULL │
│         25.00 │
└───────────────┘
```
