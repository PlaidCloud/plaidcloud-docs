---
title: STR_TO_MAP (Lakehouse v2)
description: STR_TO_MAP：将字符串拆分为键值对，并返回映射。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/str-to-map.md
---

将字符串拆分为键值对，并返回映射。

## Analyze 语法

```python
func.str_to_map(<str>[, <pair_delim>, <kv_delim>])
```

## Analyze 示例

```python
func.str_to_map('a:1,b:2,c:3', ',', ':')

┌───────────────────────────┐
│ {'a':'1','b':'2','c':'3'}  │
└───────────────────────────┘
```

## SQL 语法

```sql
STR_TO_MAP(<str>[, <pair_delim>, <kv_delim>])
```

## SQL 示例

```sql
SELECT STR_TO_MAP('a:1,b:2,c:3', ',', ':');

┌───────────────────────────┐
│ {"a":"1","b":"2","c":"3"}  │
└───────────────────────────┘
```
