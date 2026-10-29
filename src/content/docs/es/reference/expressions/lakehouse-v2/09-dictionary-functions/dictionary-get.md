---
title: DICTIONARY_GET (Lakehouse v2)
description: DICTIONARY_GET — devuelve el valor de una clave específica de un objeto de diccionario.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/09-dictionary-functions/dictionary-get.md
---

Devuelve el valor de una clave específica de un objeto de diccionario.

## Sintaxis de Analyze

```python
func.dictionary_get(<dict_name>, <key_column>, <key_value>)
```

## Ejemplos de Analyze

```python
func.dictionary_get('status_dict', get_column(table, 'status_code'))

┌──────────┐
│ 'Active'  │
└──────────┘
```

## Sintaxis de SQL

```sql
DICTIONARY_GET(<dict_name>, <key_column>, <key_value>)
```

## Ejemplos de SQL

```sql
SELECT DICTIONARY_GET('status_dict', status_code) FROM records;

┌────────┐
│ Active  │
└────────┘
```
