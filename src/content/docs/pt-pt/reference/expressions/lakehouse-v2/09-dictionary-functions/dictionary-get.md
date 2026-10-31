---
title: DICTIONARY_GET (Lakehouse v2)
description: DICTIONARY_GET — devolve o valor de uma chave especificada de um objeto de dicionário.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/09-dictionary-functions/dictionary-get.md
---

Devolve o valor de uma chave especificada de um objeto de dicionário.

## Sintaxe de Analyze

```python
func.dictionary_get(<dict_name>, <key_column>, <key_value>)
```

## Exemplos de Analyze

```python
func.dictionary_get('status_dict', get_column(table, 'status_code'))

┌──────────┐
│ 'Active'  │
└──────────┘
```

## Sintaxe SQL

```sql
DICTIONARY_GET(<dict_name>, <key_column>, <key_value>)
```

## Exemplos SQL

```sql
SELECT DICTIONARY_GET('status_dict', status_code) FROM records;

┌────────┐
│ Active  │
└────────┘
```
