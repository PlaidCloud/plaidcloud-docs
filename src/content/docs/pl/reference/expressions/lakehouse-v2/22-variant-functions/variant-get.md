---
title: VARIANT_GET (Lakehouse v2)
description: VARIANT_GET — wyodrębnia wartość o określonym typie z obiektu VARIANT pod podaną ścieżką.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-get.md
---

Wyodrębnia wartość o określonym typie z obiektu VARIANT pod podaną ścieżką.

## Składnia Analyze

```python
func.variant_get(<variant>, <path>, <type>)
```

## Przykłady Analyze

```python
func.variant_get(get_column(table, 'data'), '$.name', 'STRING')

┌─────────┐
│ 'Alice'  │
└─────────┘
```

## Składnia SQL

```sql
VARIANT_GET(<variant>, <path>, <type>)
```

## Przykłady SQL

```sql
SELECT VARIANT_GET(data, '$.name', 'STRING') FROM events;

┌───────┐
│ Alice  │
└───────┘
```
