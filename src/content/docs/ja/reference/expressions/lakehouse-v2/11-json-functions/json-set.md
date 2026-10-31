---
title: JSON_SET (Lakehouse v2)
description: JSON_SET — JSONドキュメントの指定したパスに値を設定します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-set.md
---

JSONドキュメントの指定したパスに値を設定します。

## Analyzeの構文

```python
func.json_set(get_column(table, 'data'), '$.age', 31)
```

## Analyzeの例

```python
func.json_set(get_column(table, 'data'), '$.age', 31)

┌──────────────┐
│ updated JSON │
└──────────────┘
```

## SQLの構文

```sql
JSON_SET(<data>, '$.age', 31)
```

## SQLの例

```sql
SELECT JSON_SET(PARSE_JSON('{"name":"Alice"}'), '$.age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
