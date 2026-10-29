---
title: GET_JSON_BOOL (Lakehouse v2)
description: GET_JSON_BOOL — 指定したパスでJSONオブジェクトからブール値を抽出します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-bool.md
---

指定したパスでJSONオブジェクトからブール値を抽出します。

## Analyzeの構文

```python
func.get_json_bool(get_column(table, 'data'), '$.active')
```

## Analyzeの例

```python
func.get_json_bool(get_column(table, 'data'), '$.active')

┌───┐
│ 1 │
└───┘
```

## SQLの構文

```sql
GET_JSON_BOOL(<data>, '$.active')
```

## SQLの例

```sql
SELECT GET_JSON_BOOL('{"active": true}', '$.active');

┌───┐
│ 1 │
└───┘
```
