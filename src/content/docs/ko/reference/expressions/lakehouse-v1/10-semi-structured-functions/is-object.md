---
title: IS_OBJECT (Lakehouse v1)
description: IS_OBJECT — 입력 값이 JSON 객체인지 검사합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-object.md
---

입력 값이 JSON 객체인지 검사합니다.

## Analyze Syntax

```python
func.is_object(<expr>)
```

## Analyze Examples

```python

func.is_object(func.parse_json('{"a":"b"}')), func.is_object(func.parse_json('["a","b","c"]'))
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_object(func.parse_json('{"a":"b"}'))  │ func.is_object(func.parse_json('["a","b","c"]')) │
├───────────────────────────────────────────────┼──────────────────────────────────────────────────┤
│ true                                          │ false                                            │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
IS_OBJECT( <expr> )
```

## 반환 타입

입력 JSON 값이 JSON 객체이면 `true`, 그렇지 않으면 `false`를 반환합니다.

## SQL Examples

```sql
SELECT
  IS_OBJECT(PARSE_JSON('{"a":"b"}')), -- JSON Object
  IS_OBJECT(PARSE_JSON('["a","b","c"]')); --JSON Array

┌─────────────────────────────────────────────────────────────────────────────┐
│ is_object(parse_json('{"a":"b"}')) │ is_object(parse_json('["a","b","c"]')) │
├────────────────────────────────────┼────────────────────────────────────────┤
│ true                               │ false                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```
