---
title: DICT_MAPPING (Lakehouse v2)
description: DICT_MAPPING – gibt den Wert zurück, der einem angegebenen Schlüssel in einer Dictionary-Tabelle zugeordnet ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/09-dictionary-functions/dict-mapping.md
---

Gibt den Wert zurück, der einem angegebenen Schlüssel in einer Dictionary-Tabelle zugeordnet ist.

## Analyze-Syntax

```python
func.dict_mapping(<dict_table>, <key_column>, <key_value>)
```

## Analyze-Beispiele

```python
func.dict_mapping('city_dict', get_column(table, 'city_id'))

┌────────────┐
│ 'New York'  │
└────────────┘
```

## SQL-Syntax

```sql
DICT_MAPPING(<dict_table>, <key_column>, <key_value>)
```

## SQL-Beispiele

```sql
SELECT DICT_MAPPING('city_dict', city_id) FROM orders;

┌──────────┐
│ New York  │
└──────────┘
```
