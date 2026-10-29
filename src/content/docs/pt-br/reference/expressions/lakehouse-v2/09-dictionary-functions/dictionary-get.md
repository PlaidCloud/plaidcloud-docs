---
title: DICTIONARY_GET (Lakehouse v2)
description: DICTIONARY_GET — retorna o valor de uma chave especificada em um objeto de dicionário.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/09-dictionary-functions/dictionary-get.md
---

Retorna o valor de uma chave especificada em um objeto de dicionário.

## Sintaxe do Analyze

```python
func.dictionary_get(<dict_name>, <key_column>, <key_value>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT DICTIONARY_GET('status_dict', status_code) FROM records;

┌────────┐
│ Active  │
└────────┘
```
