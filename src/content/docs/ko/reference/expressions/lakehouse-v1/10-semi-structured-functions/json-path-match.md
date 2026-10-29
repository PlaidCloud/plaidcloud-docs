---
title: JSON_PATH_MATCH (Lakehouse v1)
description: JSON_PATH_MATCH — 지정한 JSON 경로 식이 JSON 데이터의 특정 조건과 일치하는지 검사합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-match.md
---

지정한 JSON 경로 식이 JSON 데이터 안의 특정 조건과 일치하는지 검사합니다. 참고: `@@` 연산자는 이 함수와 같은 의미입니다. 자세한 내용은 JSON 연산자를 참조하십시오.


## Analyze Syntax

```python
func.json_path_match(<json_data>, <json_path_expression)
```

## Analyze Examples

```python
func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1')
┌──────────────────────────────────────────────────────────────────────────┐
│ func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1') │
├──────────────────────────────────────────────────────────────────────────┤
│ true                                                                     │
└──────────────────────────────────────────────────────────────────────────┘

func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1')
┌────────────────────────────────────────────────────────────────────────────┐
│ func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1') │
├────────────────────────────────────────────────────────────────────────────┤
│ false                                                                      │
└────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
JSON_PATH_MATCH(<json_data>, <json_path_expression>)
```

- `json_data`: 검사할 JSON 데이터를 지정합니다. JSON 객체 또는 배열일 수 있습니다.
- `json_path_expression`: JSON 데이터 안에서 확인할 조건을 지정합니다. 이 식은 일치시킬 구체적인 경로나 기준을 기술하며, 예를 들어 JSON 구조의 특정 필드 값이 일정한 조건을 충족하는지 확인할 수 있습니다. `$` 기호는 JSON 데이터의 루트를 나타냅니다. 경로 식을 시작하는 데 사용하며 JSON 구조의 최상위 객체를 가리킵니다.

## 반환 타입

이 함수는 다음을 반환합니다.

- 지정한 JSON 경로 식이 JSON 데이터 안의 조건과 일치하면 `true`.
- 지정한 JSON 경로 식이 JSON 데이터 안의 조건과 일치하지 않으면 `false`.
- `json_data` 또는 `json_path_expression`이 NULL이거나 올바르지 않으면 NULL.

## SQL Examples

```sql
-- Check if the value at JSON path $.a is equal to 1
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1');

┌────────────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1') │
├────────────────────────────────────────────────────────────────┤
│ true                                                           │
└────────────────────────────────────────────────────────────────┘

-- Check if the first element in the array at JSON path $.b is greater than 1
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1');

┌──────────────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1') │
├──────────────────────────────────────────────────────────────────┤
│ false                                                            │
└──────────────────────────────────────────────────────────────────┘

-- Check if any element in the array at JSON path $.b
-- from the second one to the last are greater than or equal to 2
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[1 to last] >= 2');

┌───────────────────────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[1 to last] >= 2') │
├───────────────────────────────────────────────────────────────────────────┤
│ true                                                                      │
└───────────────────────────────────────────────────────────────────────────┘

-- NULL is returned if either the json_data or json_path_expression is NULL or invalid.
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), NULL);

┌──────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), null) │
├──────────────────────────────────────────────────────────┤
│ NULL                                                     │
└──────────────────────────────────────────────────────────┘

SELECT JSON_PATH_MATCH(NULL, '$.a == 1');

┌───────────────────────────────────┐
│ json_path_match(null, '$.a == 1') │
├───────────────────────────────────┤
│ NULL                              │
└───────────────────────────────────┘
```
