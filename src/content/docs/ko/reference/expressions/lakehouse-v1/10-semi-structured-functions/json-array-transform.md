---
title: JSON_ARRAY_TRANSFORM (Lakehouse v1)
description: JSON_ARRAY_TRANSFORM — 지정한 변환 람다 식을 사용하여 JSON 배열의 각 요소를 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-transform.md
---

지정한 변환 람다 식을 사용하여 JSON 배열의 각 요소를 변환합니다. 람다 식에 대한 자세한 내용은 람다 식을 참조하십시오.

## SQL Syntax

```sql
JSON_ARRAY_TRANSFORM(<json_array>, <lambda_expression>)
```

## 별칭

- [JSON_ARRAY_APPLY](../json-array-apply)
- [JSON_ARRAY_MAP](../json-array-map)

## 반환 타입

JSON 배열.

## SQL Examples

이 예제에서는 배열의 각 숫자 요소에 10을 곱해 원래 배열을 `[10, 20, 30, 40]`으로 변환합니다.

```sql
SELECT JSON_ARRAY_TRANSFORM(
    [1, 2, 3, 4]::JSON,
    data -> (data::Int * 10)
);

-[ RECORD 1 ]-----------------------------------
json_array_transform([1, 2, 3, 4]::VARIANT, data -> data::Int32 * 10): [10,20,30,40]
```
