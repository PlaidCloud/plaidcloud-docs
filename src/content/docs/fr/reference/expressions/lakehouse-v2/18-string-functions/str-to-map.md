---
title: STR_TO_MAP (Lakehouse v2)
description: STR_TO_MAP — découpe une chaîne en paires clé-valeur et renvoie une map.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/str-to-map.md
---

Découpe une chaîne en paires clé-valeur et renvoie une map.

## Syntaxe Analyze

```python
func.str_to_map(<str>[, <pair_delim>, <kv_delim>])
```

## Exemples Analyze

```python
func.str_to_map('a:1,b:2,c:3', ',', ':')

┌───────────────────────────┐
│ {'a':'1','b':'2','c':'3'}  │
└───────────────────────────┘
```

## Syntaxe SQL

```sql
STR_TO_MAP(<str>[, <pair_delim>, <kv_delim>])
```

## Exemples SQL

```sql
SELECT STR_TO_MAP('a:1,b:2,c:3', ',', ':');

┌───────────────────────────┐
│ {"a":"1","b":"2","c":"3"}  │
└───────────────────────────┘
```
