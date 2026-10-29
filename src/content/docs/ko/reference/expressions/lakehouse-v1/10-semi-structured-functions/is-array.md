---
title: IS_ARRAY (Lakehouse v1)
description: IS_ARRAY — 입력 값이 JSON 배열인지 검사합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-array.md
---

입력 값이 JSON 배열인지 검사합니다. 참고: JSON 배열은 ARRAY 데이터 타입과 다릅니다. JSON 배열은 JSON에서 흔히 쓰이는 데이터 구조로, 대괄호 `[ ]`로 묶은 순서가 있는 값의 모음입니다. 문자열, 숫자, 불리언, 객체, null을 비롯한 다양한 데이터 타입을 구성하고 교환하기 위한 유연한 형식입니다. 

```json title='JSON Array Example:'
[
  "Apple",
  42,
  true,
  {"name": "John", "age": 30, "isStudent": false},
  [1, 2, 3],
  null
]
```

## Analyze Syntax

```python
func.is_array(<expr>)
```

## Analyze Examples

```python

func.is_array(func.parse_json('true')), func.is_array(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_array(func.parse_json('true')) │ func.is_array(func.parse_json('[1,2,3]')) │
├────────────────────────────────────────┼───────────────────────────────────────────┤
│ false                                  │ true                                      │
└────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
IS_ARRAY( <expr> )
```

## 반환 타입

입력 값이 JSON 배열이면 `true`, 그렇지 않으면 `false`를 반환합니다.

## SQL Examples

```sql
SELECT
  IS_ARRAY(PARSE_JSON('true')),
  IS_ARRAY(PARSE_JSON('[1,2,3]'));

┌────────────────────────────────────────────────────────────────┐
│ is_array(parse_json('true')) │ is_array(parse_json('[1,2,3]')) │
├──────────────────────────────┼─────────────────────────────────┤
│ false                        │ true                            │
└────────────────────────────────────────────────────────────────┘
```
