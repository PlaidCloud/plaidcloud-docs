---
title: TO_BASE64 (Lakehouse v2)
description: TO_BASE64：将字符串编码为 base64 编码的字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/to-base64.md
---

将字符串编码为 base64 编码的字符串。

## Analyze 语法

```python
func.to_base64(<str>)
```

## Analyze 示例

```python
func.to_base64('Hello')

┌────────────┐
│ 'SGVsbG8='  │
└────────────┘
```

## SQL 语法

```sql
TO_BASE64(<str>)
```

## SQL 示例

```sql
SELECT TO_BASE64('Hello');

┌──────────┐
│ SGVsbG8=  │
└──────────┘
```
