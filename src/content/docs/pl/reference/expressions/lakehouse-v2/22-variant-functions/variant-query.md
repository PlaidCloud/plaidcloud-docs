---
title: VARIANT_QUERY (Lakehouse v2)
description: "Użyj funkcji wariantów VARIANT_QUERY w PlaidCloud Lakehouse. Odpytuje wartość z obiektu VARIANT za pomocą wyrażenia ścieżki i zwraca VARIANT."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-query.md
---

Odpytuje wartość z obiektu VARIANT za pomocą wyrażenia ścieżki i zwraca VARIANT.

## Składnia Analyze

```python
func.variant_query(<variant>, <path>)
```

## Przykłady Analyze

```python
func.variant_query(get_column(table, 'data'), '$.address.city')

┌──────────────┐
│ '"New York"'  │
└──────────────┘
```

## Składnia SQL

```sql
VARIANT_QUERY(<variant>, <path>)
```

## Przykłady SQL

```sql
SELECT VARIANT_QUERY(data, '$.address.city') FROM events;

┌────────────┐
│ "New York"  │
└────────────┘
```
