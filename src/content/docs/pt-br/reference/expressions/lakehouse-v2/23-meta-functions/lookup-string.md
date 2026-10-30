---
title: LOOKUP_STRING (Lakehouse v2)
description: LOOKUP_STRING — procura uma string em um dicionário e retorna o ID correspondente.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/lookup-string.md
---

Procura uma string em um dicionário e retorna o ID correspondente.

## Sintaxe do Analyze

```python
func.lookup_string(<dict_table>, <value>)
```

## Exemplos do Analyze

```python
func.lookup_string('status_dict', 'Active')

┌───┐
│ 1  │
└───┘
```

## Sintaxe SQL

```sql
LOOKUP_STRING(<dict_table>, <value>)
```

## Exemplos de SQL

```sql
SELECT LOOKUP_STRING('status_dict', 'Active');

┌───┐
│ 1  │
└───┘
```
