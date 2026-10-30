---
title: PARSE_JSON (Lakehouse v1)
description: 입력 JSON 문자열을 해석하여 VARIANT 값을 생성합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/parse-json.md
---

`parse_json`과 `try_parse_json`은 입력 문자열을 JSON 문서로 해석하여 VARIANT 값을 생성합니다.

`try_parse_json`은 파싱 중 오류가 발생하면 NULL 값을 반환합니다.

## Analyze Syntax

```python
func.parse_json(<json_string>)

or

func.try_parse_json(<json_string>)
```

## Analyze Examples

```python
func.parse_json('[-1, 12, 289, 2188, false]')

┌───────────────────────────────────────────────┐
│ func.parse_json('[-1, 12, 289, 2188, false]') │
├───────────────────────────────────────────────┤
│ [-1,12,289,2188,false]                        │
└───────────────────────────────────────────────┘

func.try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ')

┌──────────────────────────────────────────────────────────────┐
│ func.try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ') │
├──────────────────────────────────────────────────────────────┤
│ {"x":"abc","y":false,"z":10}                                 │
└──────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
PARSE_JSON(<expr>)
TRY_PARSE_JSON(<expr>)
```

## 인수

| 인수 | 설명                                                                    |
|-----------|--------------------------------------------------------------------------------|
| `<expr>`  | 유효한 JSON 정보를 담은 문자열 타입(예: VARCHAR)의 식입니다. |

## 반환 타입

VARIANT

## SQL Examples

```sql
SELECT parse_json('[-1, 12, 289, 2188, false]');
┌──────────────────────────────────────────┐
│ parse_json('[-1, 12, 289, 2188, false]') │
├──────────────────────────────────────────┤
│ [-1,12,289,2188,false]                   │
└──────────────────────────────────────────┘

SELECT try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ');
┌─────────────────────────────────────────────────────────┐
│ try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ') │
├─────────────────────────────────────────────────────────┤
│ {"x":"abc","y":false,"z":10}                            │
└─────────────────────────────────────────────────────────┘
```
