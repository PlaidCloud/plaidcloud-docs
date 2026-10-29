---
title: GET_IGNORE_CASE (Lakehouse v1)
description: GET_IGNORE_CASE — OBJECT를 포함하는 VARIANT에서 field_name으로 값을 추출합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get-ignore-case.md
---

`OBJECT`를 포함하는 `VARIANT`에서 field_name으로 값을 추출합니다.
값은 `Variant`로 반환되며, 인수 중 하나라도 `NULL`이면 `NULL`이 반환됩니다.

`GET_IGNORE_CASE`는 `GET`과 비슷하지만 필드 이름에 대소문자를 구분하지 않는 일치를 적용합니다.
먼저 정확히 같은 필드 이름을 찾고, 없으면 대소문자를 구분하지 않고 알파벳 순서로 필드 이름을 찾습니다.

## Analyze Syntax

```python
func.get_ignore_Case(<variant>, <field_name>)
```

## Analyze Examples

```python
func.get_ignore_case(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA')
┌─────────────────────────────────────────────────────────────────────────┐
│ func.get_ignore_case(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├─────────────────────────────────────────────────────────────────────────┤
│ 3                                                                       │
└─────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
GET_IGNORE_CASE( <variant>, <field_name> )
```

## 인수

| 인수      | 설명                                                      |
|----------------|------------------------------------------------------------------|
| `<variant>`    | ARRAY 또는 OBJECT를 포함하는 VARIANT 값     |
| `<field_name>` | OBJECT의 키-값 쌍에서 키를 지정하는 문자열 값 |

## 반환 타입

VARIANT

## SQL Examples

```sql
SELECT get_ignore_case(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA');
┌───────────────────────────────────────────────────────────────┐
│ get_ignore_case(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├───────────────────────────────────────────────────────────────┤
│ 3                                                             │
└───────────────────────────────────────────────────────────────┘
```
