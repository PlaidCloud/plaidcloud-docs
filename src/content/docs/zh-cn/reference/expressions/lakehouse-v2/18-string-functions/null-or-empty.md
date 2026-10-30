---
title: NULL_OR_EMPTY (Lakehouse v2)
description: NULL_OR_EMPTY：检查字符串是否为 NULL 或空。为真时返回 1，否则返回 0。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/null-or-empty.md
---

检查字符串是否为 NULL 或空。为真时返回 1，否则返回 0。

## Analyze 语法

```python
func.null_or_empty(<str>)
```

## Analyze 示例

```python
func.null_or_empty('')

┌───┐
│ 1  │
└───┘
```

## SQL 语法

```sql
NULL_OR_EMPTY(<str>)
```

## SQL 示例

```sql
SELECT NULL_OR_EMPTY('');

┌───┐
│ 1  │
└───┘
```
