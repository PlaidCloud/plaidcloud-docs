---
title: URL_ENCODE（Lakehouse v2）
description: URL_ENCODE — URLで使用できるように文字列をエンコードします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-encode.md
---

URLで使用できるように文字列をエンコードします。

## Analyze 構文

```python
func.url_encode(<str>)
```

## Analyze の例

```python
func.url_encode('hello world')

┌─────────────────┐
│ 'hello%20world'  │
└─────────────────┘
```

## SQL 構文

```sql
URL_ENCODE(<str>)
```

## SQL の例

```sql
SELECT URL_ENCODE('hello world');

┌───────────────┐
│ hello%20world  │
└───────────────┘
```
