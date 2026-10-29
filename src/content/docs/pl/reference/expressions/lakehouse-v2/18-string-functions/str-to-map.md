---
title: STR_TO_MAP (Lakehouse v2)
description: STR_TO_MAP — dzieli ciąg na pary klucz-wartość i zwraca mapę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/str-to-map.md
---

Dzieli ciąg na pary klucz-wartość i zwraca mapę.

## Składnia Analyze

```python
func.str_to_map(<str>[, <pair_delim>, <kv_delim>])
```

## Przykłady Analyze

```python
func.str_to_map('a:1,b:2,c:3', ',', ':')

┌───────────────────────────┐
│ {'a':'1','b':'2','c':'3'}  │
└───────────────────────────┘
```

## Składnia SQL

```sql
STR_TO_MAP(<str>[, <pair_delim>, <kv_delim>])
```

## Przykłady SQL

```sql
SELECT STR_TO_MAP('a:1,b:2,c:3', ',', ':');

┌───────────────────────────┐
│ {"a":"1","b":"2","c":"3"}  │
└───────────────────────────┘
```
