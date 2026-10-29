---
title: JSON_EXISTS (Lakehouse v2)
description: JSON_EXISTS — JSONドキュメントの指定したパスに値が含まれているかどうかをチェックします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-exists.md
---

JSONドキュメントの指定したパスに値が含まれているかどうかをチェックします。

## Analyzeの構文

```python
func.json_exists(get_column(table, 'data'), '$.name')
```

## Analyzeの例

```python
func.json_exists(get_column(table, 'data'), '$.name')

┌───┐
│ 1 │
└───┘
```

## SQLの構文

```sql
JSON_EXISTS(<data>, '$.name')
```

## SQLの例

```sql
SELECT JSON_EXISTS(PARSE_JSON('{"name":"Alice"}'), '$.name');

┌───┐
│ 1 │
└───┘
```
