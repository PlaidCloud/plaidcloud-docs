---
title: JSON_OBJECT_KEEP_NULL (Lakehouse v1)
description: JSON_OBJECT_KEEP_NULL — 키와 값으로 JSON 객체를 만듭니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-keep-null.md
---

키와 값으로 JSON 객체를 만듭니다.

- 인수는 0개 이상의 키-값 쌍입니다(키는 문자열이고 값은 모든 타입일 수 있음).
- 키가 NULL이면 해당 키-값 쌍은 결과 객체에서 생략됩니다. 그러나 값이 NULL이면 키-값 쌍이 유지됩니다.
- 키는 서로 달라야 하며, 결과 JSON에서의 순서는 지정한 순서와 다를 수 있습니다.
- `TRY_JSON_OBJECT_KEEP_NULL`은 객체를 만드는 중 오류가 발생하면 NULL 값을 반환합니다.

함께 보기: JSON_OBJECT

## SQL Syntax

```sql
JSON_OBJECT_KEEP_NULL(key1, value1[, key2, value2[, ...]])

TRY_JSON_OBJECT_KEEP_NULL(key1, value1[, key2, value2[, ...]])
```

## 반환 타입

JSON 객체.

## SQL Examples

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
