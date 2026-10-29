---
title: XX_HASH3_128 (Lakehouse v2)
description: XX_HASH3_128 — 返回值的 128 位 xxHash3 哈希。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/xx-hash3-128.md
---

返回值的 128 位 xxHash3 哈希。

## Analyze 语法

```python
func.xx_hash3_128(<expr>[, ...])
```

## Analyze 示例

```python
func.xx_hash3_128('hello')

┌────────────┐
│ (largeint)  │
└────────────┘
```

## SQL 语法

```sql
XX_HASH3_128(<expr>[, ...])
```

## SQL 示例

```sql
SELECT XX_HASH3_128('hello');

┌──────────────────────┐
│ (128-bit hash value)  │
└──────────────────────┘
```
