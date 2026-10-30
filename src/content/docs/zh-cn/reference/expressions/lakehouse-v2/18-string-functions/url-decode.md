---
title: URL_DECODE (Lakehouse v2)
description: URL_DECODE：解码经过 URL 编码的字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-decode.md
---

解码经过 URL 编码的字符串。

## Analyze 语法

```python
func.url_decode(<str>)
```

## Analyze 示例

```python
func.url_decode('hello%20world')

┌───────────────┐
│ 'hello world'  │
└───────────────┘
```

## SQL 语法

```sql
URL_DECODE(<str>)
```

## SQL 示例

```sql
SELECT URL_DECODE('hello%20world');

┌─────────────┐
│ hello world  │
└─────────────┘
```
