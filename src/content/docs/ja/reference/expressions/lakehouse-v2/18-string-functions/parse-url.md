---
title: PARSE_URL（Lakehouse v2）
description: PARSE_URL — URL文字列から指定した部分を抽出します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/parse-url.md
---

URL文字列から指定した部分を抽出します。

## Analyze 構文

```python
func.parse_url(<url>, <part>)
```

## Analyze の例

```python
func.parse_url('https://example.com/path?q=1', 'HOST')

┌───────────────┐
│ 'example.com'  │
└───────────────┘
```

## SQL 構文

```sql
PARSE_URL(<url>, <part>)
```

## SQL の例

```sql
SELECT PARSE_URL('https://example.com/path?q=1', 'HOST');

┌─────────────┐
│ example.com  │
└─────────────┘
```
