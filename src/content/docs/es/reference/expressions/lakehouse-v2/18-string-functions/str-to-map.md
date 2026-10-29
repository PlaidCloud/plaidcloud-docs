---
title: STR_TO_MAP (Lakehouse v2)
description: STR_TO_MAP — Divide una cadena en pares clave-valor y devuelve un mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/str-to-map.md
---

Divide una cadena en pares clave-valor y devuelve un mapa.

## Sintaxis de Analyze

```python
func.str_to_map(<str>[, <pair_delim>, <kv_delim>])
```

## Ejemplos de Analyze

```python
func.str_to_map('a:1,b:2,c:3', ',', ':')

┌───────────────────────────┐
│ {'a':'1','b':'2','c':'3'}  │
└───────────────────────────┘
```

## Sintaxis de SQL

```sql
STR_TO_MAP(<str>[, <pair_delim>, <kv_delim>])
```

## Ejemplos de SQL

```sql
SELECT STR_TO_MAP('a:1,b:2,c:3', ',', ':');

┌───────────────────────────┐
│ {"a":"1","b":"2","c":"3"}  │
└───────────────────────────┘
```
