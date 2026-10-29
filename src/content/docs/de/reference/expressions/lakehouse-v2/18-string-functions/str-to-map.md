---
title: STR_TO_MAP (Lakehouse v2)
description: STR_TO_MAP — Zerlegt eine Zeichenfolge in Schlüssel-Wert-Paare und gibt eine Map zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/str-to-map.md
---

Zerlegt eine Zeichenfolge in Schlüssel-Wert-Paare und gibt eine Map zurück.

## Analyze-Syntax

```python
func.str_to_map(<str>[, <pair_delim>, <kv_delim>])
```

## Analyze-Beispiele

```python
func.str_to_map('a:1,b:2,c:3', ',', ':')

┌───────────────────────────┐
│ {'a':'1','b':'2','c':'3'}  │
└───────────────────────────┘
```

## SQL-Syntax

```sql
STR_TO_MAP(<str>[, <pair_delim>, <kv_delim>])
```

## SQL-Beispiele

```sql
SELECT STR_TO_MAP('a:1,b:2,c:3', ',', ':');

┌───────────────────────────┐
│ {"a":"1","b":"2","c":"3"}  │
└───────────────────────────┘
```
