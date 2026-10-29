---
title: JSON_ARRAY_ELEMENTS (Lakehouse v1)
description: JSON_ARRAY_ELEMENTS — extrai os elementos de uma matriz JSON como linhas individuais; as matrizes aninhadas não são expandidas recursivamente.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-elements.md
---

Extrai os elementos de uma matriz JSON e devolve-os como linhas individuais no conjunto de resultados. JSON_ARRAY_ELEMENTS não expande recursivamente as matrizes aninhadas; trata-as como elementos únicos.


## Sintaxe do Analyze

```python
func.json_array_elements(<json_string>)
```

## Exemplos do Analyze

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

## Sintaxe SQL

```sql
JSON_ARRAY_ELEMENTS(<json_string>)
```

## Tipo de retorno

JSON_ARRAY_ELEMENTS devolve um conjunto de valores VARIANT, cada um a representar um elemento extraído da matriz JSON de entrada.

## Exemplos de SQL

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
