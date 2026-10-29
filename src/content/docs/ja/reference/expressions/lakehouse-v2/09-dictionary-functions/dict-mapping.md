---
title: DICT_MAPPING (Lakehouse v2)
description: DICT_MAPPING — 辞書テーブル内で指定したキーにマッピングされた値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/09-dictionary-functions/dict-mapping.md
---

辞書テーブル内で指定したキーにマッピングされた値を返します。

## Analyzeの構文

```python
func.dict_mapping(<dict_table>, <key_column>, <key_value>)
```

## Analyzeの例

```python
func.dict_mapping('city_dict', get_column(table, 'city_id'))

┌────────────┐
│ 'New York'  │
└────────────┘
```

## SQLの構文

```sql
DICT_MAPPING(<dict_table>, <key_column>, <key_value>)
```

## SQLの例

```sql
SELECT DICT_MAPPING('city_dict', city_id) FROM orders;

┌──────────┐
│ New York  │
└──────────┘
```
