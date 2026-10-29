---
title: JSON_ARRAY_ELEMENTS (Lakehouse v1)
description: JSON_ARRAY_ELEMENTS — Extrahiert die Elemente eines JSON-Arrays als einzelne Zeilen; verschachtelte Arrays werden nicht rekursiv erweitert.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-elements.md
---

Extrahiert die Elemente eines JSON-Arrays und gibt sie als einzelne Zeilen der Ergebnismenge zurück. JSON_ARRAY_ELEMENTS erweitert verschachtelte Arrays nicht rekursiv, sondern behandelt sie als einzelne Elemente.


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

## Return Type

JSON_ARRAY_ELEMENTS gibt eine Menge von VARIANT-Werten zurück, von denen jeder ein aus dem JSON-Eingabearray extrahiertes Element darstellt.

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
