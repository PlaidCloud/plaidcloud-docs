---
title: "GET (Semi-Structured, Lakehouse v1)"
description: GET — ARRAY를 포함하는 Variant에서 인덱스로, 또는 OBJECT를 포함하는 Variant에서 필드 이름으로 값을 추출합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get.md
---

`ARRAY`를 포함하는 `Variant`에서는 `index`로, `OBJECT`를 포함하는 `Variant`에서는 `field_name`으로 값을 추출합니다.
값은 `Variant`로 반환되며, 인수 중 하나라도 `NULL`이면 `NULL`이 반환됩니다.

`GET`은 `field_name`에 대소문자를 구분하는 일치를 적용합니다. 대소문자를 구분하지 않고 일치시키려면 `GET_IGNORE_CASE`를 사용하십시오.

## Analyze Syntax

```python
func.get(<variant>, <index>)

or

func.get(<variant>, <field_name>)
```

## Analyze Examples

```python
func.get(func.parse_json('[2.71, 3.14]'), 0);
┌──────────────────────────────────────────────┐
│ func.get(func.parse_json('[2.71, 3.14]'), 0) │
├──────────────────────────────────────────────┤
│ 2.71                                         │
└──────────────────────────────────────────────┘


func.get(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa');
┌─────────────────────────────────────────────────────────────┐
│ func.get(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa') │
├─────────────────────────────────────────────────────────────┤
│ 1                                                           │
└─────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
GET( <variant>, <index> )

GET( <variant>, <field_name> )
```

## 인수

| 인수      | 설명                                                      |
|----------------|------------------------------------------------------------------|
| `<variant>`    | ARRAY 또는 OBJECT를 포함하는 VARIANT 값     |
| `<index>`      | ARRAY에서 값의 위치를 지정하는 Uint32 값    |
| `<field_name>` | OBJECT의 키-값 쌍에서 키를 지정하는 문자열 값 |

## 반환 타입

VARIANT

## SQL Examples

```sql
SELECT get(parse_json('[2.71, 3.14]'), 0);
┌────────────────────────────────────┐
│ get(parse_json('[2.71, 3.14]'), 0) │
├────────────────────────────────────┤
│ 2.71                               │
└────────────────────────────────────┘

SELECT get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa');
┌───────────────────────────────────────────────────┐
│ get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa') │
├───────────────────────────────────────────────────┤
│ 1                                                 │
└───────────────────────────────────────────────────┘

SELECT get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA');
┌───────────────────────────────────────────────────┐
│ get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├───────────────────────────────────────────────────┤
│ NULL                                              │
└───────────────────────────────────────────────────┘
```
