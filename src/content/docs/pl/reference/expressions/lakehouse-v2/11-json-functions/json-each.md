---
title: JSON_EACH (Lakehouse v2)
description: JSON_EACH — rozwija obiekt JSON najwyższego poziomu do zbioru par klucz-wartość.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-each.md
---

Rozwija obiekt JSON najwyższego poziomu do zbioru par klucz-wartość.

## Składnia Analyze

```python
func.json_each(get_column(table, 'data'))
```

## Przykłady Analyze

```python
func.json_each(get_column(table, 'data'))
```

## Składnia SQL

```sql
JSON_EACH(<data>)
```

## Przykłady SQL

```sql
SELECT * FROM TABLE(JSON_EACH(PARSE_JSON('{"a":1,"b":2}')));

┌─────┬───────┐
│ key │ value │
├─────┼───────┤
│ a   │ 1     │
│ b   │ 2     │
└─────┴───────┘
```
