---
title: SHA2 (Lakehouse v2)
description: SHA2：返回字符串在指定位长（224、256、384 或 512）下的 SHA-2 哈希。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/sha2.md
---

返回字符串在指定位长（224、256、384 或 512）下的 SHA-2 哈希。

## Analyze 语法

```python
func.sha2(<str>, <bit_length>)
```

## Analyze 示例

```python
func.sha2('hello', 256)

┌───────────────┐
│ '2cf24dba...'  │
└───────────────┘
```

## SQL 语法

```sql
SHA2(<str>, <bit_length>)
```

## SQL 示例

```sql
SELECT SHA2('hello', 256);

┌──────────────────────────────────────────────────────────────────┐
│ 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824  │
└──────────────────────────────────────────────────────────────────┘
```
