---
title: JSON_OBJECT_AGG (Lakehouse v1)
description: JSON_OBJECT_AGG — 키-값 쌍을 JSON 객체로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-json-object-agg.md
---

키-값 쌍을 JSON 객체로 변환합니다. 입력의 각 행마다 키는 `<key_expression>`에서, 값은 `<value_expression>`에서 가져와 키-값 쌍을 생성합니다. 그런 다음 이 키-값 쌍을 하나의 JSON 객체로 결합합니다.

관련 항목: [JSON_ARRAY_AGG](../aggregate-json-array-agg)

## Analyze 구문

```python
func.json_object_agg(<key_expression>, <value_expression>)
```

## Analyze 예제
자세한 내용은 SQL 예제를 참조하십시오.

## SQL 구문

```sql
JSON_OBJECT_AGG(<key_expression>, <value_expression>)
```

| 매개변수        | 설명                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| key_expression   | JSON 객체의 키를 지정합니다. **문자열** 식만 지원합니다. `key_expression`이 NULL로 평가되면 해당 키-값 쌍은 건너뜁니다.  |
| value_expression | JSON 객체의 값을 지정합니다. 지원되는 모든 데이터 형식을 사용할 수 있습니다. `value_expression`이 NULL로 평가되면 해당 키-값 쌍은 건너뜁니다. |

## 반환 형식

JSON 객체입니다.

## SQL 예제

이 예제는 JSON_OBJECT_AGG로 소수, 정수, JSON variant, 배열 등 서로 다른 유형의 데이터를 JSON 객체로 집계하는 방식을 보여 줍니다. 각 JSON 객체의 키로는 열 b를 사용합니다.

```sql
CREATE TABLE d (
    a DECIMAL(10, 2), 
    b STRING, 
    c INT, 
    d VARIANT, 
    e ARRAY(STRING)
);

INSERT INTO d VALUES
    (20, 'abc', NULL, '{"k":"v"}', ['a','b']),
    (10, 'de', 100, 'null', []),
    (4.23, NULL, 200, '"uvw"', ['x','y']),
    (5.99, 'xyz', 300, '[1,2,3]', ['z']);

SELECT
    json_object_agg(b, a) AS json_a,
    json_object_agg(b, c) AS json_c,
    json_object_agg(b, d) AS json_d,
    json_object_agg(b, e) AS json_e
FROM
    d;

-[ RECORD 1 ]-----------------------------------
json_a: {"abc":20.0,"de":10.0,"xyz":5.99}
json_c: {"de":100,"xyz":300}
json_d: {"abc":{"k":"v"},"de":null,"xyz":[1,2,3]}
json_e: {"abc":["a","b"],"de":[],"xyz":["z"]}
```
