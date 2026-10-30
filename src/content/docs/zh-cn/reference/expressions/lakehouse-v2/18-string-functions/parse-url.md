---
title: PARSE_URL (Lakehouse v2)
description: PARSE_URL：从 URL 字符串中提取指定部分。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/parse-url.md
---

从 URL 字符串中提取指定部分。

## Analyze 语法

```python
func.parse_url(<url>, <part>)
```

## Analyze 示例

```python
func.parse_url('https://example.com/path?q=1', 'HOST')

┌───────────────┐
│ 'example.com'  │
└───────────────┘
```

## SQL 语法

```sql
PARSE_URL(<url>, <part>)
```

## SQL 示例

```sql
SELECT PARSE_URL('https://example.com/path?q=1', 'HOST');

┌─────────────┐
│ example.com  │
└─────────────┘
```
