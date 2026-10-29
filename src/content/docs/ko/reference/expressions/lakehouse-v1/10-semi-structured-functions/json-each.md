---
title: JSON_EACH (Lakehouse v1)
description: JSON_EACH — JSON 객체에서 키-값 쌍을 추출하여 구조를 결과 집합의 개별 행으로 분해합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-each.md
---

JSON 객체에서 키-값 쌍을 추출하여 구조를 결과 집합의 개별 행으로 분해합니다. 각 행은 입력 JSON 식에서 파생된 고유한 키-값 쌍 하나를 나타냅니다.

## Analyze Syntax

```python
func.json_each(<json_string>)
```

## Analyze Examples

```python

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.json_each(func.parse_json('{"name": "john", "age": 25, "isstudent": false, "grades": [90, 85, 92]}')) │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ('age','25')                                                                                               │
│ ('grades','[90,85,92]')                                                                                    │
│ ('isStudent','false')                                                                                      │
│ ('name','"John"')                                                                                          │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
JSON_EACH(<json_string>)
```

## 반환 타입

JSON_EACH는 STRING 키와 그에 대응하는 VARIANT 값으로 구성된 튜플의 집합을 반환합니다.

## SQL Examples

```sql
-- Extract key-value pairs from a JSON object representing information about a person
SELECT
  JSON_EACH(
    PARSE_JSON (
      '{"name": "John", "age": 25, "isStudent": false, "grades": [90, 85, 92]}'
    )
  );


┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ json_each(parse_json('{"name": "john", "age": 25, "isstudent": false, "grades": [90, 85, 92]}')) │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ('age','25')                                                                                     │
│ ('grades','[90,85,92]')                                                                          │
│ ('isStudent','false')                                                                            │
│ ('name','"John"')                                                                                │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Display data types of the extracted values
SELECT
  TYPEOF (
    JSON_EACH(
      PARSE_JSON (
        '{"name": "John", "age": 25, "isStudent": false, "grades": [90, 85, 92]}'
      )
    )
  );

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ typeof(json_each(parse_json('{"name": "john", "age": 25, "isstudent": false, "grades": [90, 85, 92]}'))) │
├──────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ TUPLE(STRING, VARIANT) NULL                                                                              │
│ TUPLE(STRING, VARIANT) NULL                                                                              │
│ TUPLE(STRING, VARIANT) NULL                                                                              │
│ TUPLE(STRING, VARIANT) NULL                                                                              │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
