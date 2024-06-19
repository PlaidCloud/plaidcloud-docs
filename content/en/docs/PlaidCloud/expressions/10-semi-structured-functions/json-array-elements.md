---
title: JSON_ARRAY_ELEMENTS
---

Extracts the elements from a JSON array, returning them as individual rows in the result set. JSON_ARRAY_ELEMENTS does not recursively expand nested arrays; it treats them as single elements.


## Analyze Syntax

```python
func.json_array_elements(<json_string>)
```

## Analyze Example

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

## Return Type

JSON_ARRAY_ELEMENTS returns a set of VARIANT values, each representing an element extracted from the input JSON array.

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