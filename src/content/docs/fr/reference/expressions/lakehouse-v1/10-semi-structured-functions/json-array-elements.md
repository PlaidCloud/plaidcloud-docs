---
title: JSON_ARRAY_ELEMENTS (Lakehouse v1)
description: JSON_ARRAY_ELEMENTS extrait les éléments d'un tableau JSON sous forme de lignes distinctes ; les tableaux imbriqués ne sont pas développés récursivement.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-elements.md
---

Extrait les éléments d'un tableau JSON et les renvoie sous forme de lignes distinctes dans le jeu de résultats. JSON_ARRAY_ELEMENTS ne développe pas récursivement les tableaux imbriqués : il les traite comme des éléments uniques.


## Syntaxe Analyze

```python
func.json_array_elements(<json_string>)
```

## Exemples Analyze

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

## Syntaxe SQL

```sql
JSON_ARRAY_ELEMENTS(<json_string>)
```

## Type de retour

JSON_ARRAY_ELEMENTS renvoie un ensemble de valeurs VARIANT, chacune représentant un élément extrait du tableau JSON en entrée.

## Exemples SQL

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
