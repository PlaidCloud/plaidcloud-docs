---
title: DICT_MAPPING
---

Returns the value mapped to a specified key in a dictionary table.

## Analyze Syntax

```python
func.dict_mapping(<dict_table>, <key_column>, <key_value>)
```

## Analyze Examples

```python
func.dict_mapping('city_dict', get_column(table, 'city_id'))

┌────────────┐
│ 'New York'  │
└────────────┘
```

## SQL Syntax

```sql
DICT_MAPPING(<dict_table>, <key_column>, <key_value>)
```

## SQL Examples

```sql
SELECT DICT_MAPPING('city_dict', city_id) FROM orders;

┌──────────┐
│ New York  │
└──────────┘
```
