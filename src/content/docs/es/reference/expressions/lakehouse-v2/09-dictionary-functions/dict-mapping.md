---
title: DICT_MAPPING (Lakehouse v2)
description: DICT_MAPPING — devuelve el valor asignado a una clave específica en una tabla de diccionario.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/09-dictionary-functions/dict-mapping.md
---

Devuelve el valor asignado a una clave específica en una tabla de diccionario.

## Sintaxis de Analyze

```python
func.dict_mapping(<dict_table>, <key_column>, <key_value>)
```

## Ejemplos de Analyze

```python
func.dict_mapping('city_dict', get_column(table, 'city_id'))

┌────────────┐
│ 'New York'  │
└────────────┘
```

## Sintaxis de SQL

```sql
DICT_MAPPING(<dict_table>, <key_column>, <key_value>)
```

## Ejemplos de SQL

```sql
SELECT DICT_MAPPING('city_dict', city_id) FROM orders;

┌──────────┐
│ New York  │
└──────────┘
```
