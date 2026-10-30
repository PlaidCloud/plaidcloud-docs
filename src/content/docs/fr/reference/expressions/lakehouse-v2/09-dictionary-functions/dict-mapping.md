---
title: DICT_MAPPING (Lakehouse v2)
description: DICT_MAPPING — renvoie la valeur associée à une clé spécifiée dans une table de dictionnaire.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/09-dictionary-functions/dict-mapping.md
---

Renvoie la valeur associée à une clé spécifiée dans une table de dictionnaire.

## Syntaxe Analyze

```python
func.dict_mapping(<dict_table>, <key_column>, <key_value>)
```

## Exemples Analyze

```python
func.dict_mapping('city_dict', get_column(table, 'city_id'))

┌────────────┐
│ 'New York'  │
└────────────┘
```

## Syntaxe SQL

```sql
DICT_MAPPING(<dict_table>, <key_column>, <key_value>)
```

## Exemples SQL

```sql
SELECT DICT_MAPPING('city_dict', city_id) FROM orders;

┌──────────┐
│ New York  │
└──────────┘
```
