---
title: JSON_STRIP_NULLS (Lakehouse v1)
description: JSON_STRIP_NULLS — JSONオブジェクトから、値がnullのプロパティをすべて削除します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-strip-nulls.md
---

JSONオブジェクトから、値がnullのプロパティをすべて削除します。

## Analyze構文

```python
func.json_strip_nulls(<json_string>)
```

## Analyzeの例

```python
func.json_strip_nulls(func.parse_json('{"name": "alice", "age": 30, "city": null}'))

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.json_strip_nulls(func.parse_json('{"name": "alice", "age": 30, "city": null}'))            │
│                                         String                                                  │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ {"age":30,"name":"Alice"}                                                                       │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL構文

```sql
JSON_STRIP_NULLS(<json_string>)
```

## 戻り値の型

入力のJSON値と同じ型の値を返します。

## SQLの例

```sql
SELECT JSON_STRIP_NULLS(PARSE_JSON('{"name": "Alice", "age": 30, "city": null}'));

json_strip_nulls(parse_json('{"name": "alice", "age": 30, "city": null}'))|
--------------------------------------------------------------------------+
{"age":30,"name":"Alice"}                                                 |
```
