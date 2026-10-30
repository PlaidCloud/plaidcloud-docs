---
title: JSON_PATH_EXISTS (Lakehouse v1)
description: JSON_PATH_EXISTS — JSON 데이터에 지정한 경로가 있는지 검사합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-exists.md
---

JSON 데이터에 지정한 경로가 있는지 검사합니다.

## Analyze Syntax

```python
func.json_path_exists(<json_data>, <json_path_expression)
```

## Analyze Examples

```python
func.json_path_exists(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ == 1)'), func.json_path_exists(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ > 1)')
┌─────────────────────────────┐
│       Item 1   │  Item 2    │
├────────────────┼────────────┤
│       True     │  False     │
└─────────────────────────────┘
```

## SQL Syntax

```sql
JSON_PATH_EXISTS(<json_data>, <json_path_expression>)
```

- json_data: 검색할 JSON 데이터를 지정합니다. JSON 객체 또는 배열일 수 있습니다.

- json_path_expression: JSON 데이터 안에서 확인할 경로를 `$`로 나타내는 JSON 데이터의 루트부터 시작해 지정합니다. 식 안에 조건을 포함할 수도 있으며, `@`로 현재 평가 중인 노드나 요소를 참조해 결과를 필터링할 수 있습니다.

## 반환 타입

이 함수는 다음을 반환합니다.

- 지정한 JSON 경로(및 조건이 있으면 그 조건)가 JSON 데이터에 있으면 `true`.
- 지정한 JSON 경로(및 조건이 있으면 그 조건)가 JSON 데이터에 없으면 `false`.
- json_data 또는 json_path_expression이 NULL이거나 올바르지 않으면 NULL.

## SQL Examples

```sql
SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ == 1)');

----
true


SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ > 1)');

----
false

SELECT JSON_PATH_EXISTS(NULL, '$.a');

----
NULL

SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), NULL);

----
NULL
```
