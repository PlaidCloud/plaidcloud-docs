---
title: IS_NULL_VALUE (Lakehouse v1)
description: IS_NULL_VALUE — 입력 값이 JSON null인지 검사합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-null-value.md
---

입력 값이 JSON `null`인지 검사합니다. 참고: 이 함수는 SQL NULL이 아니라 JSON `null`을 검사합니다. 값이 SQL NULL인지 검사하려면 [IS_NULL](../../03-conditional-functions/is-null)을 사용하십시오.

```json title='JSON null Example:'
{
  "name": "John",
  "age": null
}   
```

## Analyze Syntax

```python
func.is_null_value(<expr>)
```

## Analyze Examples

```python

func.is_null_value(func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k5'))
┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_null_value(func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k5')) │
├─────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ true                                                                                                │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
IS_NULL_VALUE( <expr> )
```

## 반환 타입

입력 값이 JSON `null`이면 `true`, 그렇지 않으면 `false`를 반환합니다.

## SQL Examples

```sql
SELECT
  IS_NULL_VALUE(PARSE_JSON('{"name":"John", "age":null}') :age), --JSON null
  IS_NULL(NULL); --SQL NULL

┌──────────────────────────────────────────────────────────────────────────────┐
│ is_null_value(parse_json('{"name":"john", "age":null}'):age) │ is_null(null) │
├──────────────────────────────────────────────────────────────┼───────────────┤
│ true                                                         │ true          │
└──────────────────────────────────────────────────────────────────────────────┘
```
