---
title: STR_TO_MAP（Lakehouse v2）
description: STR_TO_MAP — 文字列をキーと値のペアに分割し、マップを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/str-to-map.md
---

文字列をキーと値のペアに分割し、マップを返します。

## Analyze 構文

```python
func.str_to_map(<str>[, <pair_delim>, <kv_delim>])
```

## Analyze の例

```python
func.str_to_map('a:1,b:2,c:3', ',', ':')

┌───────────────────────────┐
│ {'a':'1','b':'2','c':'3'}  │
└───────────────────────────┘
```

## SQL 構文

```sql
STR_TO_MAP(<str>[, <pair_delim>, <kv_delim>])
```

## SQL の例

```sql
SELECT STR_TO_MAP('a:1,b:2,c:3', ',', ':');

┌───────────────────────────┐
│ {"a":"1","b":"2","c":"3"}  │
└───────────────────────────┘
```
