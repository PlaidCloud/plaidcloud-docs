---
title: JSON_KEYS (Lakehouse v2)
description: JSON_KEYS — zwraca klucze obiektu JSON najwyższego poziomu jako tablicę JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-keys.md
---

Zwraca klucze obiektu JSON najwyższego poziomu jako tablicę JSON.

## Składnia Analyze

```python
func.json_keys(get_column(table, 'data'))
```

## Przykłady Analyze

```python
func.json_keys(get_column(table, 'data'))

┌────────────────┐
│ ["name","age"] │
└────────────────┘
```

## Składnia SQL

```sql
JSON_KEYS(<data>)
```

## Przykłady SQL

```sql
SELECT JSON_KEYS(PARSE_JSON('{"name":"Alice","age":30}'));

┌────────────────┐
│ ["name","age"] │
└────────────────┘
```
