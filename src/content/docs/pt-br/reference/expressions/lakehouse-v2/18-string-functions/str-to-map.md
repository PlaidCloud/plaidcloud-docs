---
title: STR_TO_MAP (Lakehouse v2)
description: STR_TO_MAP — Divide uma string em pares chave-valor e retorna um mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/str-to-map.md
---

Divide uma string em pares chave-valor e retorna um mapa.

## Sintaxe do Analyze

```python
func.str_to_map(<str>[, <pair_delim>, <kv_delim>])
```

## Exemplos do Analyze

```python
func.str_to_map('a:1,b:2,c:3', ',', ':')

┌───────────────────────────┐
│ {'a':'1','b':'2','c':'3'}  │
└───────────────────────────┘
```

## Sintaxe SQL

```sql
STR_TO_MAP(<str>[, <pair_delim>, <kv_delim>])
```

## Exemplos de SQL

```sql
SELECT STR_TO_MAP('a:1,b:2,c:3', ',', ':');

┌───────────────────────────┐
│ {"a":"1","b":"2","c":"3"}  │
└───────────────────────────┘
```
