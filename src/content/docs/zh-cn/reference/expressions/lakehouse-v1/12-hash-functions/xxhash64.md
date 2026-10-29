---
title: XXHASH64 (Lakehouse v1)
description: XXHASH64：计算字符串的 xxHash64 64 位哈希值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/xxhash64.md
---

计算字符串的 xxHash64 64 位哈希值。返回值为 UInt64；如果参数为 NULL，则返回 NULL。

## Analyze 语法

```python
func.xxhash64(<expr>)
```

## Analyze 示例

```python
func.xxhash64('1234567890')

┌─────────────────────────────┐
│ func.xxhash64('1234567890') │
├─────────────────────────────┤
│        12237639266330420150 │
└─────────────────────────────┘
```

## SQL 语法

```sql
XXHASH64(<expr>)
```

## SQL 示例

```sql
SELECT XXHASH64('1234567890');

┌────────────────────────┐
│ xxhash64('1234567890') │
├────────────────────────┤
│   12237639266330420150 │
└────────────────────────┘
```
