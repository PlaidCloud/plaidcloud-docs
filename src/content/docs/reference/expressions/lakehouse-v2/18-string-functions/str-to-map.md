---
title: STR_TO_MAP
description: STR_TO_MAP — Splits a string into key-value pairs and returns a map.
---

Splits a string into key-value pairs and returns a map.

## Analyze Syntax

```python
func.str_to_map(<str>[, <pair_delim>, <kv_delim>])
```

## Analyze Examples

```python
func.str_to_map('a:1,b:2,c:3', ',', ':')

┌───────────────────────────┐
│ {'a':'1','b':'2','c':'3'}  │
└───────────────────────────┘
```

## SQL Syntax

```sql
STR_TO_MAP(<str>[, <pair_delim>, <kv_delim>])
```

## SQL Examples

```sql
SELECT STR_TO_MAP('a:1,b:2,c:3', ',', ':');

┌───────────────────────────┐
│ {"a":"1","b":"2","c":"3"}  │
└───────────────────────────┘
```
