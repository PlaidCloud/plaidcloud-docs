---
title: func.ltrim
slug: func-ltrim
description: LTRIM() function helps to return remove all the space characters found on the left-hand side of the string
date: 2022-02-03T10:18:40
---

LTRIM() function helps to return remove all the space characters found on the left-hand side of the string

## Syntax
```python
func.ltrim(value_string, string_to_trim)
```

## Examples
```python
func.ltrim('texttotrimplaidcloud', 'texttotrim') --> plaidcloud  
```
```python
func.ltrim('      plaidcloud')                   --> plaidcloud
```
