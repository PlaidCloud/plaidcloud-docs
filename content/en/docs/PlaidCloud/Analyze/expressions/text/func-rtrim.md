---
title: func.rtrim
slug: func-rtrim
description: The rtrim() function removes whitespace or other predefined characters from the right side of a string
date: 2022-02-04T12:06:36
---

The rtrim() function removes whitespace or other predefined characters from the right side of a string

## Syntax
```python
func.rtrim(value_string, string_to_trim)
```

## Examples
```python
func.rtrim('Plaidcloud    ') --> Plaidcloud  
func.rtrim('PlaidcloudXXXXX','XXXXX') --> Plaidcloud
```
