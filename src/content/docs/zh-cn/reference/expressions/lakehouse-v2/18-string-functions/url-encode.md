---
title: URL_ENCODE (Lakehouse v2)
description: URL_ENCODE：对字符串进行编码，以便在 URL 中使用。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-encode.md
---

对字符串进行编码，以便在 URL 中使用。

## Analyze 语法

```python
func.url_encode(<str>)
```

## Analyze 示例

```python
func.url_encode('hello world')

┌─────────────────┐
│ 'hello%20world'  │
└─────────────────┘
```

## SQL 语法

```sql
URL_ENCODE(<str>)
```

## SQL 示例

```sql
SELECT URL_ENCODE('hello world');

┌───────────────┐
│ hello%20world  │
└───────────────┘
```
