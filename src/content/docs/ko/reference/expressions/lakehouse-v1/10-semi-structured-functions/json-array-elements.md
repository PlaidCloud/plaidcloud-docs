---
title: JSON_ARRAY_ELEMENTS (Lakehouse v1)
description: JSON_ARRAY_ELEMENTS — JSON 배열의 요소를 개별 행으로 추출합니다. 중첩된 배열은 재귀적으로 확장되지 않습니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-elements.md
---

JSON 배열의 요소를 추출해 결과 집합에 개별 행으로 반환합니다. JSON_ARRAY_ELEMENTS는 중첩된 배열을 재귀적으로 확장하지 않고 하나의 요소로 취급합니다.


## Analyze Syntax

```python
func.json_array_elements(<json_string>)
```

## Analyze Examples

```python

func.json_array_elements(func.parse_json('[ \n  {"product": "laptop", "brand": "apple", "price": 1500},\n  {"product": "smartphone", "brand": "samsung", "price": 800},\n  {"product": "headphones", "brand": "sony", "price": 150}\n]'))
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.json_array_elements(func.parse_json('[ \n  {"product": "laptop", "brand": "apple", "price": 1500},\n  {"product": "smartphone", "brand": "samsung", "price": 800},\n  {"product": "headphones", "brand": "sony", "price": 150}\n]')) │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ {"brand":"Apple","price":1500,"product":"Laptop"}                                                                                                                                                                                         │
│ {"brand":"Samsung","price":800,"product":"Smartphone"}                                                                                                                                                                                    │
│ {"brand":"Sony","price":150,"product":"Headphones"}                                                                                                                                                                                       │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
JSON_ARRAY_ELEMENTS(<json_string>)
```

## 반환 타입

JSON_ARRAY_ELEMENTS는 입력 JSON 배열에서 추출한 요소를 각각 나타내는 VARIANT 값의 집합을 반환합니다.

## SQL Examples

```sql
-- Extract individual elements from a JSON array containing product information
SELECT
  JSON_ARRAY_ELEMENTS(
    PARSE_JSON (
      '[ 
  {"product": "Laptop", "brand": "Apple", "price": 1500},
  {"product": "Smartphone", "brand": "Samsung", "price": 800},
  {"product": "Headphones", "brand": "Sony", "price": 150}
]'
    )
  );

┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ json_array_elements(parse_json('[ \n  {"product": "laptop", "brand": "apple", "price": 1500},\n  {"product": "smartphone", "brand": "samsung", "price": 800},\n  {"product": "headphones", "brand": "sony", "price": 150}\n]')) │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ {"brand":"Apple","price":1500,"product":"Laptop"}                                                                                                                                                                               │
│ {"brand":"Samsung","price":800,"product":"Smartphone"}                                                                                                                                                                          │
│ {"brand":"Sony","price":150,"product":"Headphones"}                                                                                                                                                                             │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Display data types of the extracted elements
SELECT
  TYPEOF (
    JSON_ARRAY_ELEMENTS(
      PARSE_JSON (
        '[ 
  {"product": "Laptop", "brand": "Apple", "price": 1500},
  {"product": "Smartphone", "brand": "Samsung", "price": 800},
  {"product": "Headphones", "brand": "Sony", "price": 150}
]'
      )
    )
  );

┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ typeof(json_array_elements(parse_json('[ \n  {"product": "laptop", "brand": "apple", "price": 1500},\n  {"product": "smartphone", "brand": "samsung", "price": 800},\n  {"product": "headphones", "brand": "sony", "price": 150}\n]'))) │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ VARIANT NULL                                                                                                                                                                                                                            │
│ VARIANT NULL                                                                                                                                                                                                                            │
│ VARIANT NULL                                                                                                                                                                                                                            │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
