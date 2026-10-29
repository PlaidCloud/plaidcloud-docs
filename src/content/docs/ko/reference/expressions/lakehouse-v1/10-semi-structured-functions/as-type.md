---
title: "AS_<type> (Lakehouse v1)"
description: AS_<type> — VARIANT 값을 다른 데이터 타입으로 엄격하게 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/as-type.md
---

`VARIANT` 값을 다른 데이터 타입으로 엄격하게 변환합니다.
입력 데이터 타입이 `VARIANT`가 아니면 출력은 `NULL`입니다.
`VARIANT` 안의 값 타입이 출력 값 타입과 일치하지 않으면 출력은 `NULL`입니다.

## Analyze Syntax
```python
func.as_boolean( <variant> )
func.as_integer( <variant> )
func.as_float( <variant> )
func.as_string( <variant> )
func.as_array( <variant> )
func.as_object( <variant> )
```

## SQL Syntax

```sql
AS_BOOLEAN( <variant> )
AS_INTEGER( <variant> )
AS_FLOAT( <variant> )
AS_STRING( <variant> )
AS_ARRAY( <variant> )
AS_OBJECT( <variant> )
```

## 인수

| 인수   | 설명       |
|-------------|-------------------|
| `<variant>` | VARIANT 값 |

## 반환 타입

- AS_BOOLEAN: BOOLEAN
- AS_INTEGER: BIGINT
- AS_FLOAT:   DOUBLE
- AS_STRING:  VARCHAR
- AS_ARRAY:   배열을 포함하는 Variant
- AS_OBJECT:  객체를 포함하는 Variant

## SQL Examples

```sql
SELECT as_boolean(parse_json('true'));
┌────────────────────────────────┐
│ as_boolean(parse_json('true')) │
├────────────────────────────────┤
│ 1                              │
└────────────────────────────────┘

SELECT as_integer(parse_json('123'));
┌───────────────────────────────┐
│ as_integer(parse_json('123')) │
├───────────────────────────────┤
│ 123                           │
└───────────────────────────────┘

SELECT as_float(parse_json('12.34'));
┌───────────────────────────────┐
│ as_float(parse_json('12.34')) │
├───────────────────────────────┤
│ 12.34                         │
└───────────────────────────────┘

SELECT as_string(parse_json('"abc"'));
┌────────────────────────────────┐
│ as_string(parse_json('"abc"')) │
├────────────────────────────────┤
│ abc                            │
└────────────────────────────────┘

SELECT as_array(parse_json('[1,2,3]'));
┌─────────────────────────────────┐
│ as_array(parse_json('[1,2,3]')) │
├─────────────────────────────────┤
│ [1,2,3]                         │
└─────────────────────────────────┘

SELECT as_object(parse_json('{"k":"v","a":"b"}'));
┌────────────────────────────────────────────┐
│ as_object(parse_json('{"k":"v","a":"b"}')) │
├────────────────────────────────────────────┤
│ {"k":"v","a":"b"}                          │
└────────────────────────────────────────────┘

```
