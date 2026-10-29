---
title: DICT_MAPPING (Lakehouse v2)
description: DICT_MAPPING — zwraca wartość przypisaną do podanego klucza w tabeli słownikowej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/09-dictionary-functions/dict-mapping.md
---

Zwraca wartość przypisaną do podanego klucza w tabeli słownikowej.

## Składnia Analyze

```python
func.dict_mapping(<dict_table>, <key_column>, <key_value>)
```

## Przykłady Analyze

```python
func.dict_mapping('city_dict', get_column(table, 'city_id'))

┌────────────┐
│ 'New York'  │
└────────────┘
```

## Składnia SQL

```sql
DICT_MAPPING(<dict_table>, <key_column>, <key_value>)
```

## Przykłady SQL

```sql
SELECT DICT_MAPPING('city_dict', city_id) FROM orders;

┌──────────┐
│ New York  │
└──────────┘
```
