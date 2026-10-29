---
title: URL_EXTRACT_HOST（Lakehouse v2）
description: URL_EXTRACT_HOST — URL文字列からホストを抽出します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-extract-host.md
---

URL文字列からホストを抽出します。

## Analyze 構文

```python
func.url_extract_host(<url>)
```

## Analyze の例

```python
func.url_extract_host('https://docs.starrocks.io/path')

┌─────────────────────┐
│ 'docs.starrocks.io'  │
└─────────────────────┘
```

## SQL 構文

```sql
URL_EXTRACT_HOST(<url>)
```

## SQL の例

```sql
SELECT URL_EXTRACT_HOST('https://docs.starrocks.io/path');

┌───────────────────┐
│ docs.starrocks.io  │
└───────────────────┘
```
