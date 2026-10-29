---
title: DICTIONARY_GET (Lakehouse v2)
description: DICTIONARY_GET — 辞書オブジェクトから指定したキーの値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/09-dictionary-functions/dictionary-get.md
---

辞書オブジェクトから指定したキーの値を返します。

## Analyzeの構文

```python
func.dictionary_get(<dict_name>, <key_column>, <key_value>)
```

## Analyzeの例

```python
func.dictionary_get('status_dict', get_column(table, 'status_code'))

┌──────────┐
│ 'Active'  │
└──────────┘
```

## SQLの構文

```sql
DICTIONARY_GET(<dict_name>, <key_column>, <key_value>)
```

## SQLの例

```sql
SELECT DICTIONARY_GET('status_dict', status_code) FROM records;

┌────────┐
│ Active  │
└────────┘
```
