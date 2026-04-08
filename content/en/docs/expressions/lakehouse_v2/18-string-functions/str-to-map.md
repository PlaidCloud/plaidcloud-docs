---
title: STR_TO_MAP
description: "Learn how to use the STR_TO_MAP string function in PlaidCloud Lakehouse. Splits a string into key-value pairs and returns a map - with syntax and examples."
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
