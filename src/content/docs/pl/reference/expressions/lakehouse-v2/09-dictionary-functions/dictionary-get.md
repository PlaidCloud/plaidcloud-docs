---
title: DICTIONARY_GET (Lakehouse v2)
description: DICTIONARY_GET — zwraca wartość dla podanego klucza z obiektu słownika.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/09-dictionary-functions/dictionary-get.md
---

Zwraca wartość dla podanego klucza z obiektu słownika.

## Składnia Analyze

```python
func.dictionary_get(<dict_name>, <key_column>, <key_value>)
```

## Przykłady Analyze

```python
func.dictionary_get('status_dict', get_column(table, 'status_code'))

┌──────────┐
│ 'Active'  │
└──────────┘
```

## Składnia SQL

```sql
DICTIONARY_GET(<dict_name>, <key_column>, <key_value>)
```

## Przykłady SQL

```sql
SELECT DICTIONARY_GET('status_dict', status_code) FROM records;

┌────────┐
│ Active  │
└────────┘
```
