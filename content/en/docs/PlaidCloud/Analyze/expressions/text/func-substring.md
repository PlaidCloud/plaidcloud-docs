---
title: func.substring
slug: func-substring
description: The SUBSTRING() extracts a substring with a specified length starting from a location in an input string
date: 2022-02-07T10:25:58
---

The SUBSTRING() extracts a substring with a specified length starting from a location in an input string

## Syntax
```python
func.substring(string, start, length)
```

## Examples
Example: Takes the first 5 characters from a 9 digit postal code  
```python
func.substring(table.ship_to_postal_code, 1, 5)
```
```python
func.substring('Plaidcloud_string', 1,10) --> Plaidcloud
```
