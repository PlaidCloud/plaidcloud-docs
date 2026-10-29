---
title: JSON_REMOVE (Lakehouse v2)
description: JSON_REMOVE — JSONドキュメントの指定したパスから要素を削除します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-remove.md
---

JSONドキュメントの指定したパスから要素を削除します。

## Analyzeの構文

```python
func.json_remove(get_column(table, 'data'), '$.temp')
```

## Analyzeの例

```python
func.json_remove(get_column(table, 'data'), '$.temp')

┌──────────────────────┐
│ JSON without element │
└──────────────────────┘
```

## SQLの構文

```sql
JSON_REMOVE(<data>, '$.temp')
```

## SQLの例

```sql
SELECT JSON_REMOVE(PARSE_JSON('{"name":"Alice","temp":1}'), '$.temp');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
