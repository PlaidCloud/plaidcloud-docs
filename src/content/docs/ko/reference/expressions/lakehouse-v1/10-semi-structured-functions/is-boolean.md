---
title: IS_BOOLEAN (Lakehouse v1)
description: IS_BOOLEAN — 입력 JSON 값이 불리언인지 검사합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-boolean.md
---

입력 JSON 값이 불리언인지 검사합니다.

## Analyze Syntax

```python
func.is_boolean(<expr>)
```

## Analyze Examples

```python

func.is_boolean(func.parse_json('true')), func.is_boolean(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_boolean(func.parse_json('true')) │ func.is_boolean(func.parse_json('[1,2,3]')) │
├──────────────────────────────────────────┼─────────────────────────────────────────────┤
│ true                                     │ false                                       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
IS_BOOLEAN( <expr> )
```

## 반환 타입

입력 JSON 값이 불리언이면 `true`, 그렇지 않으면 `false`를 반환합니다.

## SQL Examples

```sql
SELECT
  IS_BOOLEAN(PARSE_JSON('true')),
  IS_BOOLEAN(PARSE_JSON('[1,2,3]'));

┌────────────────────────────────────────────────────────────────────┐
│ is_boolean(parse_json('true')) │ is_boolean(parse_json('[1,2,3]')) │
├────────────────────────────────┼───────────────────────────────────┤
│ true                           │ false                             │
└────────────────────────────────────────────────────────────────────┘
```
