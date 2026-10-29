---
title: DICTIONARY_GET (Lakehouse v2)
description: DICTIONARY_GET — renvoie la valeur d'une clé spécifiée dans un objet dictionnaire.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/09-dictionary-functions/dictionary-get.md
---

Renvoie la valeur d'une clé spécifiée dans un objet dictionnaire.

## Syntaxe Analyze

```python
func.dictionary_get(<dict_name>, <key_column>, <key_value>)
```

## Exemples Analyze

```python
func.dictionary_get('status_dict', get_column(table, 'status_code'))

┌──────────┐
│ 'Active'  │
└──────────┘
```

## Syntaxe SQL

```sql
DICTIONARY_GET(<dict_name>, <key_column>, <key_value>)
```

## Exemples SQL

```sql
SELECT DICTIONARY_GET('status_dict', status_code) FROM records;

┌────────┐
│ Active  │
└────────┘
```
