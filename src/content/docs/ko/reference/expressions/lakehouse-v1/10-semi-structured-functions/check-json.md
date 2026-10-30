---
title: CHECK_JSON (Lakehouse v1)
description: CHECK_JSON — JSON 문서가 유효한지 검사합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/check-json.md
---

JSON 문서가 유효한지 검사합니다.
입력 문자열이 유효한 JSON 문서이거나 `NULL`이면 출력은 `NULL`입니다.
입력을 유효한 JSON 값으로 변환할 수 없으면 출력 문자열에 오류 메시지가 담깁니다.

## Analyze Syntax

```python
func.check_json(<expr>)
```

## Analyze Examples

```python
func.check_json('[1,2,3]');
┌────────────────────────────┐
│ func.check_json('[1,2,3]') │
├────────────────────────────┤
│ NULL                       │
└────────────────────────────┘
```

## SQL Syntax

```sql
CHECK_JSON( <expr> )
```

## 인수

| 인수 | 설명                  |
|-----------|------------------------------|
| `<expr>`  | 문자열 타입의 식 |

## 반환 타입

문자열

## SQL Examples

```sql
SELECT check_json('[1,2,3]');
┌───────────────────────┐
│ check_json('[1,2,3]') │
├───────────────────────┤
│ NULL                  │
└───────────────────────┘

SELECT check_json('{"key":"val"}');
┌─────────────────────────────┐
│ check_json('{"key":"val"}') │
├─────────────────────────────┤
│ NULL                        │
└─────────────────────────────┘

SELECT check_json('{"key":');
┌──────────────────────────────────────────────┐
│ check_json('{"key":')                        │
├──────────────────────────────────────────────┤
│ EOF while parsing a value at line 1 column 7 │
└──────────────────────────────────────────────┘
```
