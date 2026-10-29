---
title: LOOKUP_STRING (Lakehouse v2)
description: LOOKUP_STRING — Busca una cadena en un diccionario y devuelve el ID correspondiente.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/lookup-string.md
---

Busca una cadena en un diccionario y devuelve el ID correspondiente.

## Sintaxis de Analyze

```python
func.lookup_string(<dict_table>, <value>)
```

## Ejemplos de Analyze

```python
func.lookup_string('status_dict', 'Active')

┌───┐
│ 1  │
└───┘
```

## Sintaxis de SQL

```sql
LOOKUP_STRING(<dict_table>, <value>)
```

## Ejemplos de SQL

```sql
SELECT LOOKUP_STRING('status_dict', 'Active');

┌───┐
│ 1  │
└───┘
```
