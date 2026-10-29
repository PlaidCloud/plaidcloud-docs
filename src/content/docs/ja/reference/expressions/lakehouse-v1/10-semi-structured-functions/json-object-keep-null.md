---
title: JSON_OBJECT_KEEP_NULL (Lakehouse v1)
description: JSON_OBJECT_KEEP_NULL — キーと値からJSONオブジェクトを作成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-keep-null.md
---

キーと値からJSONオブジェクトを作成します。

- 引数は、0個以上のキーと値のペアです（キーは文字列、値は任意の型）。
- キーがNULLの場合、そのキーと値のペアは結果のオブジェクトから除外されます。ただし、値がNULLの場合、そのキーと値のペアは保持されます。
- キーは互いに異なっている必要があります。また、結果のJSONでの順序は、指定した順序と異なる場合があります。
- `TRY_JSON_OBJECT_KEEP_NULL` は、オブジェクトの構築中にエラーが発生した場合にNULL値を返します。

関連項目：JSON_OBJECT

## SQL構文

```sql
JSON_OBJECT_KEEP_NULL(key1, value1[, key2, value2[, ...]])

TRY_JSON_OBJECT_KEEP_NULL(key1, value1[, key2, value2[, ...]])
```

## 戻り値の型

JSONオブジェクト。

## SQLの例

```sql
SELECT JSON_OBJECT_KEEP_NULL();
┌─────────────────────────┐
│ json_object_keep_null() │
├─────────────────────────┤
│ {}                      │
└─────────────────────────┘

SELECT JSON_OBJECT_KEEP_NULL('a', 3.14, 'b', 'xx', 'c', NULL);
┌────────────────────────────────────────────────────────┐
│ json_object_keep_null('a', 3.14, 'b', 'xx', 'c', null) │
├────────────────────────────────────────────────────────┤
│ {"a":3.14,"b":"xx","c":null}                           │
└────────────────────────────────────────────────────────┘

SELECT JSON_OBJECT_KEEP_NULL('fruits', ['apple', 'banana', 'orange'], 'vegetables', ['carrot', 'celery']);
┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ json_object_keep_null('fruits', ['apple', 'banana', 'orange'], 'vegetables', ['carrot', 'celery']) │
├────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ {"fruits":["apple","banana","orange"],"vegetables":["carrot","celery"]}                            │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT JSON_OBJECT_KEEP_NULL('key');
  |
1 | SELECT JSON_OBJECT_KEEP_NULL('key')
  |        ^^^^^^^^^^^^^^^^^^ The number of keys and values must be equal while evaluating function `json_object_keep_null('key')`


SELECT TRY_JSON_OBJECT_KEEP_NULL('key');
┌──────────────────────────────────┐
│ try_json_object_keep_null('key') │
├──────────────────────────────────┤
│ NULL                             │
└──────────────────────────────────┘
```
