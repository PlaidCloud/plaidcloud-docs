---
title: JSON_ARRAY_FILTER (Lakehouse v1)
description: JSON_ARRAY_FILTER — 지정한 람다 식을 기준으로 JSON 배열의 요소를 필터링합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-filter.md
---

지정한 람다 식을 기준으로 JSON 배열의 요소를 필터링하여 조건을 만족하는 요소만 반환합니다. 람다 식에 대한 자세한 내용은 람다 식을 참조하십시오.

## SQL Syntax

```sql
JSON_ARRAY_FILTER(<json_array>, <lambda_expression>)
```

## 반환 타입

JSON 배열.

## SQL Examples

이 예제는 문자 `a`로 시작하는 문자열만 반환하도록 배열을 필터링하여 `["apple", "avocado"]`를 만듭니다.

```sql
SELECT JSON_ARRAY_FILTER(
    ['apple', 'banana', 'avocado', 'grape']::JSON,
    d -> d::String LIKE 'a%'
);

-[ RECORD 1 ]-----------------------------------
json_array_filter(['apple', 'banana', 'avocado', 'grape']::VARIANT, d -> d::STRING LIKE 'a%'): ["apple","avocado"]
```
