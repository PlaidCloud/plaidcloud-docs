---
title: JSON_ARRAY (Lakehouse v2)
description: JSON_ARRAY — tworzy tablicę JSON z listy wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-array.md
---

Tworzy tablicę JSON z listy wartości.

## Składnia Analyze

```python
func.json_array(1, 'hello', None)
```

## Przykłady Analyze

```python
func.json_array(1, 'hello', None)

┌──────────────────┐
│ [1,"hello",null] │
└──────────────────┘
```

## Składnia SQL

```sql
JSON_ARRAY(1, 'hello', None)
```

## Przykłady SQL

```sql
SELECT JSON_ARRAY(1, 'hello', NULL);

┌──────────────────┐
│ [1,"hello",null] │
└──────────────────┘
```
