---
title: URL_EXTRACT_HOST (Lakehouse v2)
description: URL_EXTRACT_HOST：从 URL 字符串中提取主机名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-extract-host.md
---

从 URL 字符串中提取主机名。

## Analyze 语法

```python
func.url_extract_host(<url>)
```

## Analyze 示例

```python
func.url_extract_host('https://docs.starrocks.io/path')

┌─────────────────────┐
│ 'docs.starrocks.io'  │
└─────────────────────┘
```

## SQL 语法

```sql
URL_EXTRACT_HOST(<url>)
```

## SQL 示例

```sql
SELECT URL_EXTRACT_HOST('https://docs.starrocks.io/path');

┌───────────────────┐
│ docs.starrocks.io  │
└───────────────────┘
```
