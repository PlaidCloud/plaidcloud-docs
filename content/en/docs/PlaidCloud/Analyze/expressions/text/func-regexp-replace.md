---
title: func.regexp_replace
slug: func-regexp-replace
description: This function returns a new string with the substrings, which match a regular expression pattern, replaced by a new substring
date: 2022-02-04T11:09:26
---

This function returns a new string with the substrings, which match a regular expression pattern, replaced by a new substring

## Syntax
```python
func.regexp_replace(value, search, replace)
```

## Examples
```python
func.regexp_replace('plaidcloud', 'p', 'P') --> Plaidcloud  
```
```python
func.regexp_replace('remove12345alphabets','[[:alpha:]]','','g') --> 12345  
```
```python
func.regexp_replace('remove12345digits','[[:digit:]]','','g') --> removedigits  
```
