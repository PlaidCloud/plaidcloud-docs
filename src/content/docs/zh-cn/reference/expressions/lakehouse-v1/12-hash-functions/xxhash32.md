---
title: XXHASH32 (Lakehouse v1)
description: XXHASH32：计算字符串的 xxHash32 32 位哈希值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/xxhash32.md
---

计算字符串的 xxHash32 32 位哈希值。返回值为 UInt32；如果参数为 NULL，则返回 NULL。

## Analyze 语法

```python
func.xxhash32(<expr>)
```

## Analyze 示例

```python
func.xxhash32('1234567890')

┌─────────────────────────────┐
│ func.xxhash32('1234567890') │
├─────────────────────────────┤
│                  3896585587 │
└─────────────────────────────┘
```

## SQL 语法

```sql
XXHASH32(<expr>)
```

## SQL 示例

```sql
SELECT XXHASH32('1234567890');

┌────────────────────────┐
│ xxhash32('1234567890') │
├────────────────────────┤
│             3896585587 │
└────────────────────────┘
```
