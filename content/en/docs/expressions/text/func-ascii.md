---
title: func.ascii
slug: func-ascii
description: The ASCII function takes a single argument of any character data type and returns an integer based on the first character data
date: 2022-01-26T11:34:21
---

The ASCII function takes a single argument of any character data type and returns an integer based on the first character data

## Syntax
```python
func.ascii(text) → integer
```

Returns the numeric code of the first character of the argument. In UTF8 encoding, returns the Unicode code point of the character. In other multibyte encodings, the argument must be an ASCII character.

## Examples
```python
func.ascii(get_column(table, 'TAX_SEGMENT'))
```
```python
func.ascii('x') → 135
```
