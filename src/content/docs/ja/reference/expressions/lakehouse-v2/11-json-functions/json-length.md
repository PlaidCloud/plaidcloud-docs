---
title: JSON_LENGTH (Lakehouse v2)
description: JSON_LENGTH — JSONオブジェクトまたは配列の要素数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-length.md
---

JSONオブジェクトまたは配列の要素数を返します。

## Analyzeの構文

```python
func.json_length(get_column(table, 'data'))
```

## Analyzeの例

```python
func.json_length(get_column(table, 'data'))

┌───┐
│ 2 │
└───┘
```

## SQLの構文

```sql
JSON_LENGTH(<data>)
```

## SQLの例

```sql
SELECT JSON_LENGTH(PARSE_JSON('{"name":"Alice","age":30}'));

┌───┐
│ 2 │
└───┘
```
