---
title: URL_EXTRACT_PARAMETER (Lakehouse v2)
description: URL_EXTRACT_PARAMETER：从 URL 字符串中提取查询参数的值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-extract-parameter.md
---

从 URL 字符串中提取查询参数的值。

## Analyze 语法

```python
func.url_extract_parameter(<url>, <param>)
```

## Analyze 示例

```python
func.url_extract_parameter('https://example.com?page=1&size=10', 'page')

┌─────┐
│ '1'  │
└─────┘
```

## SQL 语法

```sql
URL_EXTRACT_PARAMETER(<url>, <param>)
```

## SQL 示例

```sql
SELECT URL_EXTRACT_PARAMETER('https://example.com?page=1&size=10', 'page');

┌───┐
│ 1  │
└───┘
```
