---
title: URL_DECODE（Lakehouse v2）
description: URL_DECODE — URLエンコードされた文字列をデコードします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-decode.md
---

URLエンコードされた文字列をデコードします。

## Analyze 構文

```python
func.url_decode(<str>)
```

## Analyze の例

```python
func.url_decode('hello%20world')

┌───────────────┐
│ 'hello world'  │
└───────────────┘
```

## SQL 構文

```sql
URL_DECODE(<str>)
```

## SQL の例

```sql
SELECT URL_DECODE('hello%20world');

┌─────────────┐
│ hello world  │
└─────────────┘
```
