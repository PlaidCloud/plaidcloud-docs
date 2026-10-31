---
title: DICT_MAPPING (Lakehouse v2)
description: DICT_MAPPING — devolve o valor associado a uma chave especificada numa tabela de dicionário.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/09-dictionary-functions/dict-mapping.md
---

Devolve o valor associado a uma chave especificada numa tabela de dicionário.

## Sintaxe de Analyze

```python
func.dict_mapping(<dict_table>, <key_column>, <key_value>)
```

## Exemplos de Analyze

```python
func.dict_mapping('city_dict', get_column(table, 'city_id'))

┌────────────┐
│ 'New York'  │
└────────────┘
```

## Sintaxe SQL

```sql
DICT_MAPPING(<dict_table>, <key_column>, <key_value>)
```

## Exemplos SQL

```sql
SELECT DICT_MAPPING('city_dict', city_id) FROM orders;

┌──────────┐
│ New York  │
└──────────┘
```
