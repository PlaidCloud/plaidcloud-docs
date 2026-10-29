---
title: JSON_EACH (Lakehouse v2)
description: JSON_EACH – erweitert das JSON-Objekt der obersten Ebene zu einer Menge von Schlüssel-Wert-Paaren.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-each.md
---

Erweitert das JSON-Objekt der obersten Ebene zu einer Menge von Schlüssel-Wert-Paaren.

## Analyze-Syntax

```python
func.json_each(get_column(table, 'data'))
```

## Analyze-Beispiele

```python
func.json_each(get_column(table, 'data'))
```

## SQL-Syntax

```sql
JSON_EACH(<data>)
```

## SQL-Beispiele

```sql
SELECT * FROM TABLE(JSON_EACH(PARSE_JSON('{"a":1,"b":2}')));

┌─────┬───────┐
│ key │ value │
├─────┼───────┤
│ a   │ 1     │
│ b   │ 2     │
└─────┴───────┘
```
