---
title: DICT_MAPPING (Lakehouse v2)
description: DICT_MAPPING — 返回字典表中指定键所映射的值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/09-dictionary-functions/dict-mapping.md
---

返回字典表中指定键所映射的值。

## Analyze 语法

```python
func.dict_mapping(<dict_table>, <key_column>, <key_value>)
```

## Analyze 示例

```python
func.dict_mapping('city_dict', get_column(table, 'city_id'))

┌────────────┐
│ 'New York'  │
└────────────┘
```

## SQL 语法

```sql
DICT_MAPPING(<dict_table>, <key_column>, <key_value>)
```

## SQL 示例

```sql
SELECT DICT_MAPPING('city_dict', city_id) FROM orders;

┌──────────┐
│ New York  │
└──────────┘
```
