---
title: DICTIONARY_GET (Lakehouse v2)
description: DICTIONARY_GET — 返回字典对象中指定键对应的值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/09-dictionary-functions/dictionary-get.md
---

返回字典对象中指定键对应的值。

## Analyze 语法

```python
func.dictionary_get(<dict_name>, <key_column>, <key_value>)
```

## Analyze 示例

```python
func.dictionary_get('status_dict', get_column(table, 'status_code'))

┌──────────┐
│ 'Active'  │
└──────────┘
```

## SQL 语法

```sql
DICTIONARY_GET(<dict_name>, <key_column>, <key_value>)
```

## SQL 示例

```sql
SELECT DICTIONARY_GET('status_dict', status_code) FROM records;

┌────────┐
│ Active  │
└────────┘
```
