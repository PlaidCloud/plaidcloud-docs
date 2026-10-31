---
title: JSON_KEYS (Lakehouse v2)
description: JSON_KEYS — トップレベルのJSONオブジェクトのキーをJSON配列として返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-keys.md
---

トップレベルのJSONオブジェクトのキーをJSON配列として返します。

## Analyzeの構文

```python
func.json_keys(get_column(table, 'data'))
```

## Analyzeの例

```python
func.json_keys(get_column(table, 'data'))

┌────────────────┐
│ ["name","age"] │
└────────────────┘
```

## SQLの構文

```sql
JSON_KEYS(<data>)
```

## SQLの例

```sql
SELECT JSON_KEYS(PARSE_JSON('{"name":"Alice","age":30}'));

┌────────────────┐
│ ["name","age"] │
└────────────────┘
```
