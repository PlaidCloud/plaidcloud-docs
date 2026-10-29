---
title: JSON_CONTAINS (Lakehouse v2)
description: JSON_CONTAINS — JSONドキュメントのパスに特定の値が含まれているかどうかをチェックします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-contains.md
---

JSONドキュメントのパスに特定の値が含まれているかどうかをチェックします。

## Analyzeの構文

```python
func.json_contains(get_column(table, 'data'), '"Alice"', '$.name')
```

## Analyzeの例

```python
func.json_contains(get_column(table, 'data'), '"Alice"', '$.name')

┌───┐
│ 1 │
└───┘
```

## SQLの構文

```sql
JSON_CONTAINS(<data>, '"Alice"', '$.name')
```

## SQLの例

```sql
SELECT JSON_CONTAINS('{"name":"Alice"}', '"Alice"', '$.name');

┌───┐
│ 1 │
└───┘
```
