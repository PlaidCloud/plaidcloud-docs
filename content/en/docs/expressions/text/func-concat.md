---
title: func.concat
slug: func-concat
description: The CONCAT function combines the text from multiple ranges and/or strings, but it doesn't provide delimiter or IgnoreEmpty arguments
date: 2022-02-02T10:25:58
---

The CONCAT function combines the text from multiple ranges and/or strings, but it doesn't provide delimiter or IgnoreEmpty arguments

## Syntax
```python
func.concat(string, string)
```

## Examples
```python
func.concat('www.','plaid','cloud','.com') --> www.plaidcloud.com
```
```python
func.concat(table.YEAR,'_', table.PERIOD)
```
```python
func.concat(table.ACCOUNT,' - ',table.ACCOUNT_NAME)
```
