---
title: LOCATE (Lakehouse v2)
description: LOCATE：返回子字符串在字符串中首次出现的位置。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/locate.md
---

返回子字符串在字符串中首次出现的位置。

## Analyze 语法

```python
func.locate(<substr>, <str>[, <pos>])
```

## Analyze 示例

```python
func.locate('or', 'hello world')

┌───┐
│ 8  │
└───┘
```

## SQL 语法

```sql
LOCATE(<substr>, <str>[, <pos>])
```

## SQL 示例

```sql
SELECT LOCATE('or', 'hello world');

┌───┐
│ 8  │
└───┘
```
