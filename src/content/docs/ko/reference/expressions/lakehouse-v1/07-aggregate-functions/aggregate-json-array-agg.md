---
title: JSON_ARRAY_AGG (Lakehouse v1)
description: JSON_ARRAY_AGG — NULL을 건너뛰면서 값을 JSON 배열로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-json-array-agg.md
---

NULL을 건너뛰면서 값을 JSON 배열로 변환합니다.

관련 항목: [JSON_OBJECT_AGG](../aggregate-json-object-agg)

## Analyze 구문

```python
func.json_array_agg(<expr>)
```

## Analyze 예제
자세한 내용은 SQL 예제를 참조하십시오.

## SQL 구문

```sql
JSON_ARRAY_AGG(<expr>)
```

## 반환 형식

JSON 배열입니다.

## 예제

이 예제는 JSON_ARRAY_AGG가 각 열의 값을 JSON 배열로 집계하는 방식을 보여 줍니다.

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
    json_array_agg(a) AS aggregated_a, 
    json_array_agg(b) AS aggregated_b, 
    json_array_agg(c) AS aggregated_c, 
    json_array_agg(d) AS aggregated_d, 
    json_array_agg(e) AS aggregated_e
FROM d;

-[ RECORD 1 ]-----------------------------------
aggregated_a: [20.0,10.0,4.23,5.99]
aggregated_b: ["abc","de","xyz"]
aggregated_c: [100,200,300]
aggregated_d: [{"k":"v"},null,"uvw",[1,2,3]]
aggregated_e: [["a","b"],[],["x","y"],["z"]]
```
