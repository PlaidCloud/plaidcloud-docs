---
title: URL_EXTRACT_PARAMETER（Lakehouse v2）
description: URL_EXTRACT_PARAMETER — URL文字列からクエリパラメーターの値を抽出します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-extract-parameter.md
---

URL文字列からクエリパラメーターの値を抽出します。

## Analyze 構文

```python
func.url_extract_parameter(<url>, <param>)
```

## Analyze の例

```python
func.url_extract_parameter('https://example.com?page=1&size=10', 'page')

┌─────┐
│ '1'  │
└─────┘
```

## SQL 構文

```sql
URL_EXTRACT_PARAMETER(<url>, <param>)
```

## SQL の例

```sql
SELECT URL_EXTRACT_PARAMETER('https://example.com?page=1&size=10', 'page');

┌───┐
│ 1  │
└───┘
```
