---
title: func.lpad
slug: func-lpad
description: LPAD function pads the left-side of a string with a specific set of characters (when string1 is not null).
date: 2022-02-03T09:59:11
---

LPAD function pads the left-side of a string with a specific set of characters (when string1 is not null).

## Syntax
```python
func.lpad(value_string, force_length, fill_string)
```

## Examples
```python
func.lpad('stringtofillup', 20, 'X') --> XXXXXXstringtofillup  
```
```python
func.lpad('stringtofillup', 10, 'X') --> stringtofi
```
