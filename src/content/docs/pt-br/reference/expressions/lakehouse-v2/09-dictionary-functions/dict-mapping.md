---
title: DICT_MAPPING (Lakehouse v2)
description: DICT_MAPPING — retorna o valor mapeado para uma chave especificada em uma tabela de dicionário.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/09-dictionary-functions/dict-mapping.md
---

Retorna o valor mapeado para uma chave especificada em uma tabela de dicionário.

## Sintaxe do Analyze

```python
func.dict_mapping(<dict_table>, <key_column>, <key_value>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT DICT_MAPPING('city_dict', city_id) FROM orders;

┌──────────┐
│ New York  │
└──────────┘
```
