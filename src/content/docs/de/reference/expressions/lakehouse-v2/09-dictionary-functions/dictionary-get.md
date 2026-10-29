---
title: DICTIONARY_GET (Lakehouse v2)
description: DICTIONARY_GET – gibt den Wert für einen angegebenen Schlüssel aus einem Dictionary-Objekt zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/09-dictionary-functions/dictionary-get.md
---

Gibt den Wert für einen angegebenen Schlüssel aus einem Dictionary-Objekt zurück.

## Analyze-Syntax

```python
func.dictionary_get(<dict_name>, <key_column>, <key_value>)
```

## Analyze-Beispiele

```python
func.dictionary_get('status_dict', get_column(table, 'status_code'))

┌──────────┐
│ 'Active'  │
└──────────┘
```

## SQL-Syntax

```sql
DICTIONARY_GET(<dict_name>, <key_column>, <key_value>)
```

## SQL-Beispiele

```sql
SELECT DICTIONARY_GET('status_dict', status_code) FROM records;

┌────────┐
│ Active  │
└────────┘
```
