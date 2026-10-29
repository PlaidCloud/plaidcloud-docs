---
title: STR_TO_MAP (Lakehouse v2)
description: STR_TO_MAP — 문자열을 키-값 쌍으로 분할하여 맵을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/str-to-map.md
---

문자열을 키-값 쌍으로 분할하여 맵을 반환합니다.

## Analyze 구문

```python
func.str_to_map(<str>[, <pair_delim>, <kv_delim>])
```

## Analyze 예제

```python
func.str_to_map('a:1,b:2,c:3', ',', ':')

┌───────────────────────────┐
│ {'a':'1','b':'2','c':'3'}  │
└───────────────────────────┘
```

## SQL 구문

```sql
STR_TO_MAP(<str>[, <pair_delim>, <kv_delim>])
```

## SQL 예제

```sql
SELECT STR_TO_MAP('a:1,b:2,c:3', ',', ':');

┌───────────────────────────┐
│ {"a":"1","b":"2","c":"3"}  │
└───────────────────────────┘
```
