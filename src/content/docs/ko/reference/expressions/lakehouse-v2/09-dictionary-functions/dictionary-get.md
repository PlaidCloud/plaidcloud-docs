---
title: DICTIONARY_GET (Lakehouse v2)
description: DICTIONARY_GET — 딕셔너리 객체에서 지정한 키의 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/09-dictionary-functions/dictionary-get.md
---

딕셔너리 객체에서 지정한 키의 값을 반환합니다.

## Analyze 구문

```python
func.dictionary_get(<dict_name>, <key_column>, <key_value>)
```

## Analyze 예제

```python
func.dictionary_get('status_dict', get_column(table, 'status_code'))

┌──────────┐
│ 'Active'  │
└──────────┘
```

## SQL 구문

```sql
DICTIONARY_GET(<dict_name>, <key_column>, <key_value>)
```

## SQL 예제

```sql
SELECT DICTIONARY_GET('status_dict', status_code) FROM records;

┌────────┐
│ Active  │
└────────┘
```
