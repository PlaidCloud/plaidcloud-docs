---
title: IS_STRING (Lakehouse v1)
description: IS_STRING — 입력 JSON 값이 문자열인지 검사합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-string.md
---

입력 JSON 값이 문자열인지 검사합니다.

## Analyze Syntax

```python
func.is_string(<expr>)
```

## Analyze Examples

```python

func.is_string(func.parse_json('"abc"')), func.is_string(func.parse_json('123'))
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_string(func.parse_json('"abc"'))      │ func.is_string(func.parse_json('123'))           │
├───────────────────────────────────────────────┼──────────────────────────────────────────────────┤
│ true                                          │ false                                            │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
IS_STRING( <expr> )
```

## 반환 타입

입력 JSON 값이 문자열이면 `true`, 그렇지 않으면 `false`를 반환합니다.

## SQL Examples

```sql
SELECT
  IS_STRING(PARSE_JSON('"abc"')),
  IS_STRING(PARSE_JSON('123'));

┌───────────────────────────────────────────────────────────────┐
│ is_string(parse_json('"abc"')) │ is_string(parse_json('123')) │
├────────────────────────────────┼──────────────────────────────┤
│ true                           │ false                        │
└───────────────────────────────────────────────────────────────┘
```
