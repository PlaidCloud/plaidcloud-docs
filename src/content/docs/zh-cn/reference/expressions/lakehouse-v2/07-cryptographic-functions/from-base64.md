---
title: FROM_BASE64 (Lakehouse v2)
description: FROM_BASE64：解码 base64 编码的字符串，是 `BASE64_DECODE_STRING` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/from-base64.md
---

解码 base64 编码的字符串，是 `BASE64_DECODE_STRING` 的别名。

## Analyze 语法

```python
func.from_base64(<str>)
```

## Analyze 示例

```python
func.from_base64('SGVsbG8=')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL 语法

```sql
FROM_BASE64(<str>)
```

## SQL 示例

```sql
SELECT FROM_BASE64('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
