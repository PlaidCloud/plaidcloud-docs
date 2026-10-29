---
title: JSON_EACH (Lakehouse v2)
description: JSON_EACH — トップレベルのJSONオブジェクトをキーと値のペアの集合に展開します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-each.md
---

トップレベルのJSONオブジェクトをキーと値のペアの集合に展開します。

## Analyzeの構文

```python
func.json_each(get_column(table, 'data'))
```

## Analyzeの例

```python
func.json_each(get_column(table, 'data'))
```

## SQLの構文

```sql
JSON_EACH(<data>)
```

## SQLの例

```sql
SELECT * FROM TABLE(JSON_EACH(PARSE_JSON('{"a":1,"b":2}')));

┌─────┬───────┐
│ key │ value │
├─────┼───────┤
│ a   │ 1     │
│ b   │ 2     │
└─────┴───────┘
```
